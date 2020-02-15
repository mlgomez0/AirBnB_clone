#!/usr/bin/python3
""" This module contains out line command tnterpreter for the ABNB projecrt
"""


import models
from models import storage
from cmd import Cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(Cmd):
    """ Class to create the command line interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, inp):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and 
            prints the id. Ex: $ create BaseModel
        """
        if inp == "":
            print("** class name missing **")
        elif inp != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
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
        elif list_args[0] != "BaseModel":
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
