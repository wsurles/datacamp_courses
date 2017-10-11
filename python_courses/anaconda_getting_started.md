
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


Notes:

  - Conda will "make your life 1000 times easier" according to udacity instructor. Its simply an package and environment editor.
  - Becuase there are so many different versions of python and packages that work with different versions its a sure thing that you will eventually find yourself in some kind of broken dependency hell. So using environments for projects is a must. This lets you keep that python version and packages independent of other projects so each project will work.
    - this might be something that I should just be using docker for since it gives even more control. But I still want to learn a little bit about how conda controls environemnts.
