#!/usr/bin/python3
"""
This is a command intepreter console for AirBnB clone project
"""
import cmd
import sys


class commandIntepreter(cmd.Cmd):
    """ This is the console for the project interface
    having many use cases on objects
    to update, create and destroy"""

    prompt = '(hbtn) '
    """ This is a comment, i dnt yet know how to make it
    work in a loop in non-interactive mode, although it
    works but it immediately exists once it runs.
    But maybe thats how its suppose to work"""
    def emptyline(self):
        """Returns an emoty line"""
        pass

    def do_quit(self, line):
        """Quits the console: ctrl+C"""
        sys.exit()

    def do_EOF(self, line):
        """This method handles the EOF or ctrl+D"""
        print('\n')
        return True


if __name__ == '__main__':
    commandIntepreter().cmdloop()
