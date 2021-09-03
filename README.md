# EITN School 2021 : TVB project

## Git-repo

1. Clone this repo in your laptop

   1. Open the terminal and run the command 

   2. ```
      git clone 
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

1. Windows Linux Subsystem (WSL): You can repeat the step above in the new WSL terminal if installed in windows --> See https://docs.microsoft.com/en-us/windows/wsl/install-win10#simplified-installation-for-windows-insiders
2. You can import the environment in Anaconda
3. Test the tutorials (.ipynb file) by pressing Shift + Enter with your keyboard
4. Enjoy