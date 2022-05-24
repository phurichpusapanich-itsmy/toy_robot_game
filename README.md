# SIMPLE TOY ROBOT GAME

This simple toy robot game is build with python 3.10.2, although it should be runnable with python 3 in general

## Introduction

The toy robot is running in a 5 x 5 grid

The robot can:
1. Move 1 space toward the direction it is currently facing
2. Rotate (90 Degree) to the left or to the right
3. Report its current position

## Features

- Command reader for controlling toy robot car
- Debug mode
- Unit testing


## Install Python

This program is build with python 3.10.4, however lower python 3 versions should be able to run this application

You can use Anaconda which allows you to create and switch python version easily.

Find the suitable installer for your OS in https://www.anaconda.com/products/distribution

Once install, launch Anaconda prompt to install required Python version.

```
conda create -n myenv python=3.10.4
```

Activate new conda environment by

```
conda activate myenv
```

From now, you can use the new environment you have just created to run this program, or use it as a base for another virtual environment.

## How to run

Fork and clone this repository, or download the zip file and extract it.

Then, you will need to move into the folder you've just cloned/extracted then run the pip install command.

```sh
pip install .
```

The program runs with an input file of a .txt format. The sample file has been provided (data.txt)

The program only accepts these commands,

- PLACE x, y, <NORTH|WEST|EAST|SOUTH>
- MOVE
- LEFT
- RIGHT
- REPORT

Sample input file

```sh
# data.txt
PLACE 0,0,NORTH
MOVE
LEFT
REPORT
```

Run the drive command with the input file as an argument.

```sh
drive [INPUT_FILE]
```

Run the command with --verbose to show more debug information

```sh
drive [INPUT_FILE] --verbose
```

## How to test

- After you have updated your code, you can run the test with.
- To add more tests, please checkout the test files in /tests

```sh
python setup.py test
```

