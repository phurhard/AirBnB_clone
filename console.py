#!/usr/bin/python3
"""
This is a command intepreter console for AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ This is the console for the project interface
    having many use cases on objects
    to update, create and destroy"""

    prompt = '(hbnb) '
    """ This is a comment, i dnt yet know how to make it
    work in a loop in non-interactive mode, although it
    works but it immediately exists once it runs.
    But maybe thats how its suppose to work"""
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
        '''Creates a new instance of BaseModel,
        saves it to the JSO file and prints the id'''
        classes = ['BaseModel']
        command = self.parseline(line)[0]
        if command in classes:
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance.id)
        elif command == None:
            print('** class name missing **')
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
