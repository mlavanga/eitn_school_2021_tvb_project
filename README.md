# EITN School 2021 : TVB project

## Git-repo

1. Clone this repo in your laptop

   1. Open the terminal and run the command 

   2. ```
      git clone https://github.com/mlavanga/eitn_school_2021_tvb_project.git
      ```

2. You can always download this folder from the website

## Linux and MacOS

1. Open the terminal and verify to have python3 by running

```
python3
```

The version should be < 3.9 if possible

2. Change directory to the eitn_fall_school folder. Run the following commands. 

```
rm -rf env
python3 -mvenv env
. env/bin/activate
pip3 install --upgrade pip
pip3 install wheel
pip3 install -r requirements.txt
pip3 install tvb-data
pip3 install neurokit
pip3 install sklearn
pip3 install anytree
pip3 install ipywidgets
pip3 install pandas
pip3 install seaborn
pip3 install jupyterlab
```

3. Test the environment. Open a new tab on the terminal and run the following commands

```
. env/bin/activate
jupyter-lab
```

4. Copy the paste the locahost link in your favourite browser or use the deafult opening session
5. Test the tutorials (.ipynb file) by pressing Shift + Enter with your keyboard
6. Enjoy

## Windows

1. Create an Anaconda environment

2. Download an anaconda from the website

   1. https://www.anaconda.com/products/individual-d

3. Download the zip folder from the github website and unzip it. We suggest to place it in the documents folder

   1. https://github.com/mlavanga/eitn_school_2021_tvb_project

4. Open the Anaconda prompt

5. Move to the folder of the project by running the command (modify accordingly)

6. ```
   cd C:\Users\<Username>\Documents\eitn_school_2021_tvb_project
   ```

7. Run the following commands in the terminal

8. ```
   conda create -n env python=3.6
   conda activate env
   pip3 install wheel
   pip3 install -r requirements.txt
   pip3 install tvb-data
   pip3 install neurokit
   pip3 install sklearn
   pip3 install anytree
   pip3 install ipywidgets
   pip3 install pandas
   pip3 install seaborn
   pip3 install jupyterlab
   ```

9. Run the following command:

10. ```
    conda deactivate env
    conda activate env
    jupyter-lab
    ```

11. Copy the paste the locahost link in your favourite browser or use the deafult opening session

12. Test the tutorials (.ipynb file) by pressing Shift + Enter with your keyboard

13. Enjoy

## WINDOWS (if you are kind of GEEKY)

1. Windows Linux Subsystem (WSL): You can repeat the step above in the new WSL terminal if installed in windows --> See https://docs.microsoft.com/en-us/windows/wsl/install-win10#simplified-installation-for-windows-insiders
2. Enjoy again

## PROJECT PITCH: BRAIN LATERALIZATION WITH TVB

1. Gslide link: https://docs.google.com/presentation/d/1YpiHleC8f8lZhKPKnpfugt4eJYZsPDnQ0pxA8P6aRmY/edit?usp=sharing

## BIBLIOGRAPHY

1. **Whole-brain modelling**
   1.  https://www.nature.com/articles/nn.4497
   2. https://www.jneurosci.org/content/33/27/11239 

2. **Brain lateralization**: 
   1. https://www.pnas.org/content/116/52/26961 
3. **TVB simulator**: 
   1. https://internal-journal.frontiersin.org/articles/10.3389/fninf.2013.00010/full
   2. https://www.sciencedirect.com/science/article/pii/S1053811915000051
   3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5489253/ 

4. **Mouse Data**
   1. https://www.pnas.org/content/116/52/26961 

