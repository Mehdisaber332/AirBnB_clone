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
import ast


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

    def do_count(self, arg):
        ''' Count the number of instances of a specified class using <class_name> '''
        class_name = arg.strip()
        if class_name in HBNBCommand.class_names:
            count = 0
            for instance in models.storage.all().values():
                if instance.__class__.__name__ == class_name:
                    count += 1
            print(count)
        else:
            print("** Class doesn't exist **")

    def precmd(self, line):
        ''' custom commands handled '''
        parts = line.split('.')
        if len(parts) == 2:
            if parts[1] == 'all()' or parts[1] == 'count()':
                parts[0] = parts[0].strip()
                parts[1] = parts[1].translate(
                    str.maketrans('', '', '()')).strip()
                method_name = f"do_{parts[1]}"
                getattr(self, method_name)(f"{parts[0]}")

            if len(parts) == 2 and '(' in parts[1] and parts[1].endswith(')'):
                class_name = parts[0].strip()
                command, args = parts[1].split('(', 1)

                if command == 'update':
                    method_name = f"do_{command}"
                    if ',' not in args:
                        print("** attribute name missing **")
                        return ""
                    id, attr = args.split(',', 1)
                    id = id.strip('"')
                    attr = attr.strip(')').strip()
                    attr = attr.replace('"', "'")
                    attr = ast.literal_eval(attr)
                    if isinstance(attr, dict):
                        for key, value in attr.items():
                            getattr(self, method_name)(
                                f"{class_name} {id} {key} {repr(value)}")
                    else:
                        if isinstance(attr, tuple):
                            attr = list(attr)
                            attr_name, attr_value = attr[0], repr(attr[1])
                        else:
                            attr_name = attr
                            attr_value = ""
                        getattr(self, method_name)(
                            f"{class_name} {id} {attr_name} {attr_value}")

                elif command in {'show', 'destroy', }:
                    args = args.strip(')')
                    args = args.strip('"')
                    method_name = f"do_{command}"
                    getattr(self, method_name)(f"{class_name} {args}")
                else:
                    return ""
            return ""

        else:
            return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
