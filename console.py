#!/usr/bin/python3
"""
This is a command intepreter console for AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel
import models
import json


class HBNBCommand(cmd.Cmd):
    """ This is the console for the project interface
    having many use cases on objects
    to update, create and destroy"""

    prompt = '(hbnb) '
    """ This is a comment, i dnt yet know how to make it
    work in a loop in non-interactive mode, although it
    works but it immediately exists once it runs.
    But maybe thats how its suppose to work"""
    classes = ['BaseModel']
    
    def emptyline(self):
        """Returns an empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, line):
        """This method handles the EOF or ctrl+D"""
        print('\n')
        return True

    def do_create(self, line):
        '''Creates an instance of BaseModel saves it to json n print its id'''

        if  not line:
            print('** class name missing **')
        elif not (line in self.classes):
            print('** class doesn\'t exist **')
        else:
            command = self.parseline(line)[0]
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class name and id'''
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        print(self.parseline(line))
        if command == None:
            print("** class name is missing **")

        elif not (command in self.classes):
            print("** class doesn't exist **")
        elif arg == None:
            print("** instance id missing **")
        else:
            inst = models.storage.all().get(command+'.'+arg)
            if inst == None:
                print("** no instance found **")
            else:
                print(inst)

    def do_destroy(self, line):
        '''Deletes a class based on its id and instamce namr'''
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        print(self.parseline(line))
        if command == None:
            print("** class name is missing **")
        elif not (command in self.classes):
            print("** class doesn't exist **")
        elif arg == None:
            print("** instance id missing **")
        else:
            inst = models.storage.all().get(command+'.'+arg)
            if inst == None:
                print("** no instance found **")
            else:
                del models.storage.all()[inst]
                models.storage.save()

    def do_all(self, line):
        '''Prints all instances regardless of class name'''
        return models.storage.all()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
