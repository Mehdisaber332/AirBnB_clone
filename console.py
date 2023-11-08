#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def do_all(self, arg):
        '''Print all instances'''
        args = arg.split()
        obj_list = []

        if not arg:
            for obj_id, obj in storage.all().items():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for obj_id, obj in storage.all().items():
                if obj.__class__.__name__ == args[0]:
                    obj_list.append(str(obj))
            if obj_list:
                print(obj_list)
            else:
                print("** no instance found **")

    def do_show(self, arg):
        '''Print the string representation of an instance'''
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        '''Delete an instance based on the class name and id'''
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_update(self, arg):
        '''Update an instance based on the class name and id'''
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
