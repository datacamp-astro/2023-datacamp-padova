# Data reading and handling

The purpose of this hands-on is to get familiar with the real astronomical data.

## Introduction
Data is a very generic word for a file or set of files that contain information from a datataking from an experiment. However, each instrument has its own data format and a data format and data model must be decided when developing an instrument. Generally speaking data from an experiments are assembled from many inputs in a stage called 'reconstruction'. At the end of the reconstruction phase data should be in a 'high level' format that can in principle be distributed also to external scientists for further analysis.

In the framework of this workshop we will use data in the so-called Data Level 3 format (DL3). This means that DL0, DL1, DL2 are earlier stages of the analysis and that DL4 and further can be successive stages in the analysis. We need to be able to open DL3 files and check their content. This is the purpose of this hands-on

## Requirements
* Basic packages: `astropy, numpy, scipy, matplotlib`


## Set up

1) Open the "Terminal" on your PC

2) type and run:
   `conda activate datacamp-padova`
   or
   `mamba activate datacamp-padova`

3) Download the github repo of the school with `git clone git@github.com:datacamp-astro/2023-datacamp-padova.git`
4) Download the dataset with `cd  2023-datacamp-padova` and then  `gammapy download datasets`
5) Let's set the variable `GAMMAPY_DATA`.
   
   Copy the output of `pwd` (You should get something like /blabla/blabla/2023-datacamp-padova) and paste it inside
 the  `~/.bashrc` in a new line:

`export GAMMAPY_DATA=/blabla/blabla/2023-datacamp-padova/gammapy-datasets`

6) Close the terminal and repeat poin 1 and 2. Finally you can launch the notebook with `jupyter-notebook &` or `jupyter-lab &` 
