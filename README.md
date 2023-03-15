# AirBnB Clone - The Console                                                                                                     ![HolBnB clone](https://github.com/monoprosito/AirBnB_clone/blob/feature/console/hBnB.png?raw=true)                              Welcome to the AirBnB clone project! (The Holberton B&B)


## Description of the Project
- This repository contains the code for AirBnB cloning, this is part of the team project required by alx swe programme as a requirement for learning the higher level language

## Description of the command interpreter
- The command interpreter is an interface that aids in controlling all objects created by the user, it serves as a great debugging and monitoring tool for the developer.
- The command interpreter enables us to manage the objects of our project by: 
* Create a new object(ex. a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

### How to start the command interpreter:
- This repo can be cloned onto your system and run the file console.py.This file will automatically run the command interpreter and can run in both interactive and non-interactive mode
### How to use the command interpreter:
- Type help once the commad interpreter starts up to view a list of available commands.
- help command prints the help for that specific command. calling quit exits the command interpreter
### Examples:
In interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

