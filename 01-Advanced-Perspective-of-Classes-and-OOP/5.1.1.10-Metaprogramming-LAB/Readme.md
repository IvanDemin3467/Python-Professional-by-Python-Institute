#5.1.1.10-Metaprogramming-LAB

###Estimated time

45 minutes

###Level of difficulty

Medium

###Objectives
1. improving the student's skills in operating with metaclasses;
2. improving the student's skills in operating with class variables and class methods.

###Scenario

1. Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code; 
2. The system was created by a group of volunteers who worked with no clear “clean coding” rules; 
3. The system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems; 
4. Your task is to prepare a metaclass that is responsible for:
   1. equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time; 
   2. equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.

```* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).```
5. Your metaclass should be used to create a few distinct legacy classes; 
6. Create objects based on the classes; 
7. List the class names that are instantiated by your metaclass.
