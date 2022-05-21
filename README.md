# SIMPLE TOY ROBOT GAME

This simple toy robot game is build with python 3.10.2, although it should be runnable with python 3 in general

## Introduction

The toy robot is running in a 5 x 5 grid

The robot can:
1. Move 1 space toward the direction it is currently facing
2. Rotate (90 Degree) to the left or to the right
3. Report its current position

## Features

- Toy Robot Car Console Application
- Unit testing

## Tech

- Python 3.10.2 (Lower version of Python 3 should be able to run this program as well)


## How to run

```sh
pip install .
```

The program runs with an input file of a .txt format. The sample file has been provided (data.txt)

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

## How to test

- After you have updated your code, you can run the test with.
- To add more tests, please checkout the test files in /toy_car/tests

```sh
python setup.py test
```

