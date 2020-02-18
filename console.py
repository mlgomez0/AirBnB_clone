#!/usr/bin/python3
""" This module contains out line command tnterpreter for the ABNB projecrt
"""

from ast import literal_eval
import models
from models import storage
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import shlex


class HBNBCommand(Cmd):
    """ Class to create the command line interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, inp):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id. Ex: $ create BaseModel
        """
        if inp == "":
            print("** class name missing **")
        elif inp.split(' ')[0] not in globals().keys():
            print("** class doesn't exist **")
        else:
            new_obj = globals()[inp]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, inp):
        """ Prints the string representation of an instance based on the class
            name and id.
        """
        flag = 0
        list_args = inp.split(' ')
        if list_args[0] == "":
            print("** class name missing **")
        elif list_args[0] not in globals().keys():
            print("** class doesn't exist **")
        elif len(list_args) <= 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                splitted = k.split('.')[1]
                if splitted == list_args[1]:
                    print(v)
                    flag = 1
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id (save the
           change into the JSON file).
        """
        flag = 0
        list_args = inp.split(' ')
        if list_args[0] == "":
            print("** class name missing **")
        elif list_args[0] not in globals().keys():
            print("** class doesn't exist **")
        elif len(list_args) <= 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                splitted = k.split('.')[1]
                if splitted == list_args[1]:
                    del all_objs[k]
                    flag = 1
                    storage.save()
                    break
            if flag == 0:
                print("** no instance found **")

    def do_all(self, inp):
        """Prints all string representation of all
           instances based or not on the class name.
        """

        my_list = []
        if inp != "" and inp.split(' ')[0] not in globals().keys():
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                if inp == "":
                    my_list.append(v.__str__())
                elif k.split('.')[0] == inp.split(' ')[0]:
                    my_list.append(v.__str__())
            print(my_list)

    def do_update(self, inp):
        """Updates an instance based on the class name and id by
           adding or updating attribute
        """

        flag = 0
        letters_count = 0
        list_args = shlex.split(inp)
        if list_args[0] == "":
            print("** class name missing **")
        elif list_args[0] not in globals().keys():
            print("** class doesn't exist **")
        elif len(list_args) == 1:
            print("** instance id missing **")
        elif len(list_args) == 2:
            print("** attribute name missing **")
        elif len(list_args) <= 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            for i in list_args[3]:
                if i.isalpha():
                    letters_count += 1
            for k, v in all_objs.items():
                splitted = k.split('.')[1]
                if splitted == list_args[1]:
                    flag = 1
                    if (list_args[3].isdigit()):
                        setattr(v, list_args[2], int(list_args[3]))
                    elif (list_args[3].isalpha() is False
                          and list_args[3].count('.') == 1
                          and letters_count == 0):
                        setattr(v, list_args[2], float(list_args[3]))
                    else:
                        setattr(v, list_args[2], list_args[3])
                    storage.save()
                    break

            if flag == 0:
                print("** no instance found **")

    def do_quit(self, inp):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(quit):
        print('Quit command to exit the program')

    def emptyline(self):
        pass

    do_EOF = do_quit
    help_EOF = help_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
