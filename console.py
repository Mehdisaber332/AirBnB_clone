#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class definition for the command interpreter"""

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

    def do_create(self, arg):
        '''Create a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)
    
    def do_show(self, arg):
        '''Print the string representation of an instance'''

        args = arg.split()
        
        if arg is None or arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
