import subprocess
import sys

print("This file installs the requirements for the project.")

def install(package):
    print('Installing '+package)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install_list=['graphviz','scipy','numpy==1.18.1','pandas==1.0.1','python-git','matplotlib','seaborn','plotly','cytoolz','lz4','ipywidgets','dask-labextension==1.0.3','graphviz']

for i in install_list:
    install(i)