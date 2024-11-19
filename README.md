# python_exercises

## Day 00

### Ex00

A Python script that can take some text from its standard input and then print only the lines that start with exactly 5 zeros.

### Ex01

Decyphering the sentence by taking first letter of every word and putting them to one string

### Ex02

Finding M pattern in files

## Day 01

### Ex00

Functions add_ingot(purse), get_ingot(purse), and empty(purse) that take a purse (a dictionary, which is strictly speaking a typing.Dict[str, int]) and return a purse (an empty dict in the case of empty(purse)). 

### Ex01

Function called split_booty that takes any number of purses (dictionaries) as argumentsand returns three purses (dictionaries) such that in any two of the three purses the difference between the number of ingots is not greater than 1. 

### Ex02

Decorator to print SQUEAK when calling other functions

## Day 02

### Ex00

A funny custom class to pass some assertions

### Ex 01

A little morality game with cheating and collaborating options, 5 builtin and 1 custom strategies

## Day 03

### Ex 00

Change an html file using python script and beautiful soup

### Ex 01

Producer creates a list of transactions, cunsumer tracks "bad guys" using redis

### Ex 02

A Python script called gen_ansible.py that reads a todo list from todo.yml and generates a corresponding Ansible playbook file deploy.yml, which includes tasks for installing packages, copying files, and executing them on a remote server using Python.

## Day 04

### Ex 00

A function fix_wiring() that takes three iterables (cables, sockets, plugs) and returns a generator of string commands to connect them.

### Ex 01

A function turrets_generator() that dynamically generates turret objects with five random personality traits (neuroticism, openness, conscientiousness, extraversion, agreeableness) that sum to 100.

### Ex 02

A generator function emit_gel() that simulates liquid pressure values between 0 and 100 with random step increments, and another function valve() that controls the pressure.

## Day 05

### Exercise 00

A WSGI server that listens on port 8888, processes GET requests, and returns JSON responses with species-specific credentials.

### Exercise 01

A web application (WSGI server) to manage audio files. Users can upload audio files (checked via MIME type), which will be stored on the server and displayed in a list on the web interface.

### Exercise 02

Simulation of  five Time Lords (threads) sharing screwdrivers in a variation of the "Dining Philosophers" problem.

## Day 07

### Exercise 00

A Voight-Kampff Test program that asks 10 questions stored in a JSON or SQLite file, with each answer followed by manual input of physiological variables (respiration, heart rate, blushing level, pupillary dilation). After all responses, the program outputs a binary decision of "human" or "replicant," with all logic split across appropriately modular files, initiated via main.py as a command-line interface.

### Exercise 01

Extended the Voight-Kampff Test with robust unit tests using Pytest to cover edge cases, such as empty or invalid question files, incorrect inputs, and invalid physiological measurements.

### Exercise 02
Generated comprehensive project documentation for the Voight-Kampff Test using Sphinx. The documentation includes a Quickstart guide for users (written in Markdown or RST) and an auto-generated API reference created using docstrings for all modules, classes, and functions. 
