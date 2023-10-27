#!/usr/bin/python3
"""
This is a command intepreter console for AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models import storage
import json
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """ This is the console for the project interface
    having many use cases on objects
    to update, create and destroy"""

    prompt = '(hbnb) '
    """ This is a comment, i dnt yet know how to make it
    work in a loop in non-interactive mode, although it
    works but it immediately exists once it runs.
    But maybe thats how its suppose to work"""
    classes = ['BaseModel', 'User', 'Place', 'Review', 'State', 'City', 'Amenity']
    
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
        command = self.parseline(line)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.classes:
            print('** class doesn\'t exist **')
        else:
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class name and id'''
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print("** class name is missing **")

        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            inst = storage.all().get(f'{command}.{arg}')
            if inst is None:
                print("** no instance found **")
            else:
                print(inst)

    def do_destroy(self, line):
        '''Deletes a class based on its id and instance name'''
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print("** class name is missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            inst = storage.all().get(f'{command}.{arg}')
            if inst is None:
                print("** no instance found **")
            else:
                del storage.all()[f'{command}.{arg}']
                storage.save()

    def do_all(self, line):
        '''Prints all instances regardless of class name'''
        baseModels = storage.all()
        model = self.parseline(line)[0]
        lst = []
        if model is None:
            lst.extend(str(i) for i in baseModels.values())
            print(lst)
        elif model not in self.classes:
            print("** class doesn't exist **")
        else:
            lst.extend(str(baseModels[i]) for i in baseModels if i.startswith(model))
            print(lst)

    def do_update(self, line):
        "Updates an instance based on class name and id"

        model = self.parseline(line)[0]
        attrbs = self.parseline(line)[1]
        if attrbs is not None:
            attrbs = shlex.split(attrbs)
            inst = attrbs[0]
            instnf = storage.all().get(f'{model}.{inst}')
        if model is None:
            print("** class name missing **")
        elif model not in self.classes:
            print("** class doesn't exist **")
        elif inst == '':
            print("** instance id missing **")
        elif instnf is None:
            print("** instance not found **")
        elif len(attrbs) < 2:
            print("** attribute name missing **")
        elif len(attrbs) < 3:
                print("** value missing **")
        else:
            if attrbs[2].isdigit():
                attrbs[2] = int(attrbs[2])
            elif attrbs[2].replace('.', '', 1).isdigit():
                attrbs[2] = float(attrbs[2])
            setattr(instnf, attrbs[1], attrbs[2])
            storage.save()

    def get_instances(self, instance=''):
        objects = storage.all()
        lst = []
        if instance:
            lst.extend(str(v) for k, v in objects.items() if k.startswith(instance))
        else:
            lst.extend(str(v) for k, v in objects.items())
        return lst
    def default(self, line):
        '''Enables calking a ckass with dot notation'''
        if '.' not in line:
            return
        linesplit = re.split(r'\.|\(|\)', line)
        command = linesplit[0]
        method = linesplit[1]
        instId = linesplit[2].strip('"')
        if command in self.classes:
            if method == 'all':
                print(self.get_instances(command))
            elif method == 'count':
                print(len(self.get_instances(command)))
            elif method == 'destroy':
                self.do_destroy(f'{command} {instId}')
            elif method == 'show':
                self.do_show(f'{command} {instId}')
            elif method == 'update':
                attr = linesplit[2]
                if '{' in line:
                    attrb = re.split(r'\, |\{}', attr)
                    print(attrb)
                    print(len(attrb))
                    print(type(attrb))
                else:
                    attrb = re.split(r'\,', attr)
                    Id = attrb[0].strip(' "')
                    attrbName = attrb[1].strip(' "')
                    attrbValue = attrb[2].strip(' "')
                    self.do_update(f'{command} {Id} {attrbName} {attrbValue}')





if __name__ == '__main__':
    HBNBCommand().cmdloop()
