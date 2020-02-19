# AirBnB clone - The console

## Description

The goal of this project is to deploy  in our own server a simple copy of the AirBnB website. It is the first step towards the building of the ABnB web application. By the end, our project will have the following capabilities:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`, `Amenity`, `Review`) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage
- create all unittests to validate all our classes and storage engine

## Command Interpreter
The command interpreter is like the prompt of the shell, once executed you'll be expected to type some specific commands for our project to manage its objects.
For example: 

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Directories:
- tests/test_models/test_engine
- models/engine

## Files in tests:
- \_\_init__.py
## Files in tests/test_models
- \_\_init__.py
- test_amenity.py
- test_base_model.py
- test_city.py
- test_console.py
- test_place.py
- test_review.py
- test_state.py
- test_user.py

## Files in tests/test_models/test_engine
- \_\_init__.py
- test_file_storage.py

## Files in models
- \_\_init__.py
- base_model.py
- user.py
- amenity.py
- city.py
- place.py
- review.py
- state.py

## Files in models/engine:
- \_\_init__.py
- file_storage.py

# Files in main folder:
- \_\_init__.py
- console.py

## How to install:
```git clone https://github.com/DiegoAlar/AirBnB_clone.git```

### How to execute:
```python3 console.py```

## How to use the console:

- To dinamically use the console, see the example below:
```python3 console.py```
 ```
  (hbnb) help
 Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
 ```
 - to quit the console, type quit. i.e:
 - ```(hbnb) quit```

Let's see what commands you can use by executing the console and typing help:
```python3 console.py```

 ```
  (hbnb) help
 Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
 ```
 
 As you can see, there are some commands that you can use to manage objects of our project such as: all, create, destroy, help, quit, show and update. Let's review each one of them

## For non-interactive use of the console:

```
echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update


```

### All
This command is used whenever you want the console to show all the objects stored in our abstract storage.
```(hbnb) all```
```
["[City] (b0d6d339-1999-4015-8561-0c2980ca7eb6) {'id': 'b0d6d339-1999-4015-8561-0c2980ca7eb6', 'created_at': datetime.datetime(2020, 2, 18, 19, 34, 52, 400185), 'updated_at': datetime.datetime(2020, 2, 18, 19, 34, 52, 400195), 'name': 'fdsfds'}"]
```
As you can see, there is only one object of the class City.
Now, if you want to specifically see all objects strored of an specific class, you type: all <class_name>. See below:
```(hbnb) all City```
```
["[City] (b0d6d339-1999-4015-8561-0c2980ca7eb6) {'id': 'b0d6d339-1999-4015-8561-0c2980ca7eb6', 'created_at': datetime.datetime(2020, 2, 18, 19, 34, 52, 400185), 'updated_at': datetime.datetime(2020, 2, 18, 19, 34, 52, 400195), 'name': 'fdsfds'}"]
```
The result is the same, because we type all City, but what if we type all User? Let's see:
```(hbnb) all User```
You'll see nothing, because it'll only show you the results of User and there are no instances (yet) of the class User.
## Create

With this command we will create objects by specifying the class. i.e:
Let's create an User object:
```
(hbnb) create User
fcca66a7-d032-4ef8-9b69-e3b2419473e7
```
Once you type create User, the console will show you the id of the new created object of class User.
## Show

The show command is useful when you want the console to show you an specific object given the class and the ID. i.e:
```
(hbnb) show User fcca66a7-d032-4ef8-9b69-e3b2419473e7
[User] (fcca66a7-d032-4ef8-9b69-e3b2419473e7) {'id': 'fcca66a7-d032-4ef8-9b69-e3b2419473e7', 'created_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562027), 'updated_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562034)}
```

## Destroy
The destroy command is used when you want to destroy an specific object given the class and the ID of the object you want to delete. i.e:
```
(hbnb) destroy City b0d6d339-1999-4015-8561-0c2980ca7eb6
(hbnb) all
["[User] (fcca66a7-d032-4ef8-9b69-e3b2419473e7) {'id': 'fcca66a7-d032-4ef8-9b69-e3b2419473e7', 'created_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562027), 'updated_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562034)}"]
```
Notice that the object of class City is not longer in our storage after using destroy command by typing all command!

## Update
The update command is used in order to add or create new attributes for an specific instance of a class and its ID. i.e:
- To create a new attribute for the User object:

```
(hbnb) update User fcca66a7-d032-4ef8-9b69-e3b2419473e7 town "Madison"
(hbnb) all User
["[User] (fcca66a7-d032-4ef8-9b69-e3b2419473e7) {'id': 'fcca66a7-d032-4ef8-9b69-e3b2419473e7', 'created_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562027), 'updated_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562034), 'town': 'Madison'}"]
(hbnb) 
```

A new attribute (town) was added to our User's instance¡

- To update an existing attribute given the class instance and its ID. i.e:

```
(hbnb) update User fcca66a7-d032-4ef8-9b69-e3b2419473e7 town "Patterson"
(hbnb) all User
["[User] (fcca66a7-d032-4ef8-9b69-e3b2419473e7) {'id': 'fcca66a7-d032-4ef8-9b69-e3b2419473e7', 'created_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562027), 'updated_at': datetime.datetime(2020, 2, 19, 11, 50, 31, 562034), 'town': 'Patterson'}"]
```
The attribute town was updated with the value Patterson!
 
## Authors:

This project is written and mantain by **Mary Luz Gómez Mejía** (1163@holbertonschool.com) and **Diego A. Alarcón V.** (1153@holbertonschool.com)

