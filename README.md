# Docker Projects Template

This is a repository space for a template docker setup that can be built to run Jupyter Notebooks for various projects. Reading through the instructions should help to solidify the idea.

**Step 1) git clone https://github.com/pmleffers/Docker_Projects_Template**

**Step 2) Modify requirements.py**

_Add any additional packages you would like to install and have available for the docker container. So for example if you want to make the container designed for Tensorflow, add the Tensorflow installation packagas. Or if you want to make the container designed to run Dask, add dask installation instructions for building the container. Including any additional packages you might require for running the projects beyond simply a jupyter notebook with python._

**Step 3) docker build -t new_project .**

_Once the modification to reqiurements.py is complete, run the the **"docker build -t <new_project> ."** command._

**Step 4) docker run --rm -it -v ${PWD}/project_files:/src/project_files -p 8888:8888 <new_project>**

_Once the container and images have been built the running the command above will start the container and launch a jupyter notebook instance inside the container. Copy the token created from jupyter notebook and navigate to "localhost:8888" in your browser of choice and enter the token information into the login page. Once here you can start or continue working on your projects._

Explanations:
+ "**data**" folder - This is where data you want to use should be stored.
+ "**project_files**" folder - This is a folder linked to the location "**/src/project_files**" within the container which is the default working location for jupyter notebooks. 
+ **module.py** - Executing this file in python should include all the data cleaning procedures needed before starting the project. The docker build command should execute this file so when you finally get to the jupyter notebook launch everything is ready to go.
 




          



