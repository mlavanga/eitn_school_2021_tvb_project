from tvb.basic.neotraits.api import HasTraits, Attr, NArray, List
from ipywidgets import interact, FloatSlider, Dropdown, ToggleButton
import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
from tvb.simulator.lab import integrators

def phase_plane_interactive(model, integrator):
    
    
    NUMBEROFGRIDPOINTS = 42
    TRAJ_STEPS = 4096

    
    def plot_phase_plane(**param_kwargs):
        # defaults, to be changed
        svx = param_kwargs.pop('svx') #x-axis: 1st state variable
        svy = param_kwargs.pop('svy') #y-axis: 2nd state variable
        
        
        mode = param_kwargs.pop('mode')

        
        # set model params
        for k, v in param_kwargs.items():
            setattr(model, k, np.r_[v])

        # state vector
        sv_mean = np.array([param_kwargs[key] for key in model.state_variables])
        sv_mean = sv_mean.reshape((model.nvar, 1, 1))
        default_sv = sv_mean.repeat(model.number_of_modes, axis=2)
        no_coupling = np.zeros((model.nvar, 1, model.number_of_modes))


        # mesh grid
        xlo = model.state_variable_range[svx][0]
        xhi = model.state_variable_range[svx][1]
        ylo = model.state_variable_range[svy][0]
        yhi = model.state_variable_range[svy][1]

        X = np.mgrid[xlo:xhi:(NUMBEROFGRIDPOINTS*1j)]
        Y = np.mgrid[ylo:yhi:(NUMBEROFGRIDPOINTS*1j)]


        # Calculate the vector field.
        svx_ind = model.state_variables.index(svx)
        svy_ind = model.state_variables.index(svy)


        #Calculate the vector field discretely sampled at a grid of points
        grid_point = default_sv.copy()
        U = np.zeros((NUMBEROFGRIDPOINTS, NUMBEROFGRIDPOINTS,
                              model.number_of_modes))
        V = np.zeros((NUMBEROFGRIDPOINTS, NUMBEROFGRIDPOINTS,
                              model.number_of_modes))
        for ii in range(NUMBEROFGRIDPOINTS):
            grid_point[svy_ind] = Y[ii]
            for jj in range(NUMBEROFGRIDPOINTS):
                #import pdb; pdb.set_trace()
                grid_point[svx_ind] = X[jj]

                d = model.dfun(grid_point, no_coupling)

                for kk in range(model.number_of_modes):
                    U[ii, jj, kk] = d[svx_ind, 0, kk]
                    V[ii, jj, kk] = d[svy_ind, 0, kk]


        # plot
        f = plt.figure( figsize=(10,8+model.nvar))
        gs0 = gridspec.GridSpec(2,1, figure=f, wspace=0.1, height_ratios=(8,model.nvar))
        gs = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[0], hspace=0.05)
        
        
        # Top (unshared) axes
        ax = f.add_subplot(gs[0])
        ax.set(
            xlabel = "State Variable " + svx,
            ylabel = "State Variable " + svy,
            title = model.__class__.__name__ + " mode " + str(mode)
        )
        
        if np.all(U[:, :, mode] + V[:, :, mode]  == 0):
            ax.set(title = model_name + " mode " + mode + ": NO MOTION IN THIS PLANE")
            X, Y = np.meshgrid(X, Y)
            pp_quivers = ax.scatter(X, Y, s=8, marker=".", c="k")
        else:
            pp_quivers = ax.quiver(X, Y,
                                                U[:, :, mode],
                                                V[:, :, mode],
                                                width=0.001, headwidth=8)

        #Plot the nullclines
        nullcline_x = ax.contour(X, Y,
                                              U[:, :, mode],
                                              [0], colors="r")
        nullcline_y = ax.contour(X, Y,
                                              V[:, :, mode],
                                              [0], colors="g")
        
        
        
        if param_kwargs['trajectory']:
            if isinstance(integrator, integrators.IntegratorStochastic):
                if integrator.noise.ntau > 0.0:
                    integrator.noise.configure_coloured(integrator.dt,
                                                             (1, model.nvar, 1,
                                                              model.number_of_modes))
                else:
                    integrator.noise.configure_white(integrator.dt,
                                                          (1, model.nvar, 1,
                                                           model.number_of_modes))
            
            svx_ind = model.state_variables.index(svx)
            svy_ind = model.state_variables.index(svy)

            #Calculate an example trajectory
            state = default_sv.copy()
            integrator.clamped_state_variable_indices = np.setdiff1d(
                np.r_[:len(model.state_variables)], np.r_[svx_ind, svy_ind])
            integrator.clamped_state_variable_values = default_sv[integrator.clamped_state_variable_indices]
            scheme = integrator.scheme
            traj = np.zeros((TRAJ_STEPS+1, model.nvar, 1,
                                model.number_of_modes))
            traj[0, :] = state
            for step in range(TRAJ_STEPS):
                state = scheme(state, model.dfun, no_coupling, 0.0, 0.0)
                traj[step+1, :] = state

            ax.scatter(default_sv[svx_ind], default_sv[svy_ind], s=42, c='g', marker='o', edgecolor=None)
            ax.plot(traj[:, svx_ind, 0, mode],
                            traj[:, svy_ind, 0, mode])

            #Plot the selected state variable trajectories as a function of time
            gs = gridspec.GridSpecFromSubplotSpec(model.nvar, 1, subplot_spec=gs0[1], hspace=0.1)
            for i, svar in enumerate(model.state_variables):
                ax = f.add_subplot(gs[i])
                ax.plot(np.arange(TRAJ_STEPS+1) * integrator.dt, traj[:, i, 0, mode])
                ax.set(ylabel=svar)
                if i < model.nvar-1:
                    ax.axes.xaxis.set_ticks([])
                else:
                    ax.set(xlabel="time (ms)")

        
    # setup widgets 
    param_kwargs = {}
    for param_name in type(model).declarative_attrs:            
            param_def = getattr(type(model), param_name)
            if not isinstance(param_def, NArray) or not param_def.dtype == np.float :
                continue
            param_range = param_def.domain
            if param_range is None:
                continue
            param_value = getattr(model, param_name).item()
            param_kwargs[param_name] = FloatSlider(
                min=param_range.lo, max=param_range.hi, value=param_value)
            
    for svar, svar_range in model.state_variable_range.items():
        param_kwargs[svar] = FloatSlider(
                min=svar_range[0], max=svar_range[1], value=np.mean(svar_range)
        )
    
    param_kwargs['svx'] = Dropdown(
        #options=[(v,i) for i, v in enumerate(model.state_variables)],
        options = model.state_variables,
        value=model.state_variables[0],
        description='X axis'
    )
    param_kwargs['svy'] = Dropdown(
        #options=[(v,i) for i, v in enumerate(model.state_variables)],
        options = model.state_variables,
        value=model.state_variables[1],
        description='Y axis'
    )
    param_kwargs['mode'] = Dropdown(
        options=list(range(model.number_of_modes)),
        value=0,
        description='Mode'
    ) 
    

    param_kwargs['trajectory'] = ToggleButton(
        value=False,
        description='Show trajectory'
    )
    
    
    w = interact(plot_phase_plane, **param_kwargs)
    return w
