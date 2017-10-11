
Great Resourses for getting started with anaconda, jupyter, python:

  - [Intro to Anaconda on Udacity](https://classroom.udacity.com/courses/ud1111/lessons/c6a12f2e-63f2-4007-a2c3-dd3e5f06f3cb/concepts/4cdc5a26-1e54-4a69-8eb4-f15e37aaab7b)
    - I found this quick tutorial to be pretty good for helping understand whats possible and getting anaconda set up well.
  - [Intro to Jupyter on Udacity]


My Steps:

  - Install Anaconda
    - Looks like it is at anaconda 5.0.0, but it will still install to a folder names anaconda3. huh
    - I chose the download for python 3.6 from the [anaconda website](https://www.anaconda.com/download/#macos)
    - Go through all the steps in the install window.
    - This put anacoda3 into my home folder.
    - This has anaconda-navigator, a gui for choosing tools.
    - It even has Rstudio. interesitng.
  - get conda working
    - Just need to add anaconda3 to the path. this is simple but a little annoying that the installation does not do this
    - Run this in the command line
    - `export PATH=~/anaconda3/bin:$PATH`
    - Then try `conda list` to see all the packages and `conda --version` to see the version. These should both work now.
  - create an environment for your first project
    - `conda create -n python_datacamp python=3`
    - `source activate python_datacamp`
    - It will just install some default packages
    - I need to install the packages I want to work with. It will just install them for this environment
    - `conda install numpy pandas matplotlib`
    - Then I still need to get jupyter package for some reason
    - `conda install jupyter notebook`
    - This comes with a bunch of things that let the notebook work




Conda Notes:

  - Conda will "make your life 1000 times easier" according to udacity instructor. Its simply an package and environment editor.
  - Becuase there are so many different versions of python and packages that work with different versions its a sure thing that you will eventually find yourself in some kind of broken dependency hell. So using environments for projects is a must. This lets you keep that python version and packages independent of other projects so each project will work.
    - this might be something that I should just be using docker for since it gives even more control. But I still want to learn a little bit about how conda controls environemnts.
  - conda is foces on data science where pip is generally for all python packages
    - also conda is not python specific. you can install packages for R or other languages
  - You could install a specific version if needed with
    - `conda install numpy=1.10.`
  - dependencies will be automatically installed as needed
  - removing an updating packages is easy with conda `remove` and `update`
    - `conda update -all` will update all packages and is useful
  - `conda search` can help you find a package if you don't remember its name
  - you can create a new envoronment and install packages into it all in one
    - `conda create -n [env_name] [list of packages]`
  - you can set the python version for the environment
    - `conda create -n py3 python=3`
  - `source activate my_env` to enter an env
    - when in an environment the name will show in the terminal prompt
  - `source deactivate` to leave an environment
  - you can use a yaml file to save an environment definition
    - `conda env export > environment.yaml`
  - create an env from a yaml file
    - `conda env create -f environment.yaml`
  - `conda env list` will let you see all the envs you have
  - `conda env remove -n env_name` to remove old environments
  - it common to set up an envorinment for each project.
  - I have created one for the datacamp classes. I'll see how it goes.
  - Its good practice to include an environment file in code repos on github
    - you can use a pip `requirements.txt` file using `pip freeze` for people not using conda
    - [pip feeze documentation](https://pip.pypa.io/en/stable/reference/pip_freeze/)
  - Other recommended readings
    - [Conda: Myths and Misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)
    - [Conda documentation](https://conda.io/docs/user-guide/tasks/index.html)
    
Jupyter Notes:

  - [jupyter.org](http://jupyter.org/)
  - [Example notebook that shows many of the notebook features](https://github.com/mcleonard/blog_posts/blob/master/body_fat_percentage.ipynb)
  - ipynb Notebooks are automatically rendered on github which is a nifty feature
  - [nbviewer](http://nbviewer.jupyter.org/) will let you view notebooks from other sites.
    - This is neat. But you can also just view them in github so I'm not really sure why this is needed.
  - jupyter stands for julia python R because those were the first languages with kernals for jupyter
    - but there are a ton of kernals now. [here](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) is the list.
  - the kernals can be run anywhere and access via the web through the notebook server. This is handy
    - Its similar to how rstudio-server works
  - The easiest way to install jupyter is with anaconda
    - type `conda install jupyter notebook` inside a conda env to add jupyter
  - type `jupyter notebook` to start a notebook kernals
    - you will need to copy.paste the url with the token into the url to access
    - this keeps your files a little bit private I guess
    - you will see your file directory from where you started the notebook
    - this should be your project directory
    - your terminal window will now be tied up running the kernal
  - You should consider installing Notebook Conda to help manage your environments. Run the following command:
    - `conda install nb_conda`
    - This just lets you manage your conda environments and packages from inside jupyter
    - However I read that this is not yet available for python 3.6. lame
  - If I wanted to get out of the web notebooks I could try using [hydrogen](https://atom.io/packages/hydrogen)
    - This tool lets you run python kernals and see out puts (just like lighttable) from in side atom code editor. Cool!
  - I definitely need to get familiar with the command pallete and short cuts if I don't want to be mouse clicking all day
  -
