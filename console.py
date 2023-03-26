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
        if command == None:
            print('** class name missing **')
        elif not (command in self.classes):
            print('** class doesn\'t exist **')
        else:
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class name and id'''
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command == None:
            print("** class name is missing **")

        elif not (command in self.classes):
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            inst = storage.all().get(command+'.'+arg)
            if inst == None:
                print("** no instance found **")
            else:
                print(inst)

    def do_destroy(self, line):
        '''Deletes a class based on its id and instance name'''
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command == None:
            print("** class name is missing **")
        elif not (command in self.classes):
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            inst = storage.all().get(command+'.'+arg)
            if inst == None:
                print("** no instance found **")
            else:
                del storage.all()[command+'.'+arg]
                storage.save()

    def do_all(self, line):
        '''Prints all instances regardless of class name'''
        baseModels = storage.all()
        model = self.parseline(line)[0]
        lst = []
        if model == None:
            for i in baseModels.values():
                lst.append(str(i))
            print(lst)
        elif not (model in self.classes):
            print("** class doesn't exist **")
        else:
            for i in baseModels:
                if i.startswith(model):
                    lst.append(str(baseModels[i]))
            print(lst)

    def do_update(self, line):
        "Updates an instance based on class name and id"

        model = self.parseline(line)[0]
        attrbs = self.parseline(line)[1]
        if not (attrbs == None):
            attrbs = shlex.split(attrbs)
            inst = attrbs[0]
            instnf = storage.all().get(model+'.'+inst)
        if model == None:
            print("** class name missing **")
        elif not (model in self.classes):
            print("** class doesn't exist **")
        elif inst == '':
            print("** instance id missing **")
        elif instnf == None:
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
            for k,v in objects.items():
                if k.startswith(instance):
                    lst.append(str(v))
        else:
            for k,v in objects.items():
                lst.append(str(v))
        return lst
    def default(self, line):
        '''Enables calking a ckass with dot notation'''
        if '.' in line:
            linesplit = re.split(r'\.|\(|\)', line)
            command = linesplit[0]
            method = linesplit[1]
            instId = linesplit[2].strip('"')
            if command in self.classes:
                if method == 'all':
                    print(self.get_instances(command))
                if method == 'count':
                    print(len(self.get_instances(command)))
                if method == 'show':
                    self.do_show(command+' '+instId)
                if method == 'destroy':
                    print(self.do_destroy(command+' '+instId))
                if method == 'update':
                    if '{' in line:
                        attr = linesplit[2]
                        attrb = re.split(r'\, |\{}', attr)
                        print(attrb)
                        print(len(attrb))
                        print(type(attrb))
                    else:
                        attr = linesplit[2]
                        attrb = re.split(r'\,', attr)
                        Id = attrb[0].strip(' "')
                        attrbName = attrb[1].strip(' "')
                        attrbValue = attrb[2].strip(' "')
                        self.do_update(command+' '+Id+' '+attrbName+' '+attrbValue)





if __name__ == '__main__':
    HBNBCommand().cmdloop()
