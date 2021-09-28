#2.8.1.7-Composition-vs-Inheritance-LAB

###Estimated time

45 minutes

###Level of difficulty

Medium

###Objectives

•	improving the student's skills in operating with inheritance and composition

###Scenario

Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :

•	define classes representing:

o	tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size

o	engine; methods available: start(), stop(), get_state(); attribute available: fuel type

o	vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN

•	based on the classes defined above, create the following objects:

o	two sets of tires: city tires (size: 15), off-road tires (size: 18)

o	two engines: electric engine, petrol engine

•	instantiate two objects representing cars:

o	the first one is a city car, built of an electric engine and city tires

o	the second one is an all-terrain car build of a petrol engine and off-road tires

•	play with the cars by calling methods responsible for interaction with components.
