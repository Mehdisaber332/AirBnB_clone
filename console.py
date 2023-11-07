#!/usr/bin/python3
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Class definition"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        ''' Command to exit '''
        return True

    def help_quit(self):
        """Change help message for the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        ''' EOF Exit the program with CTRL+D '''
        return True

    def emptyline(self):
        ''' Do nothing on an empty input line '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
