#2.7.1.5-Properties-getter-setter-delete-LAB

###Estimated time
30-60 minutes
###Level of difficulty
Medium
###Objectives

•	improving the student's skills in operating with the getter, setter, and deleter methods;

•	improving the student's skills in creating their own exceptions.

###Scenario

•	Implement a class representing an account exception,

•	Implement a class representing a single bank account,

•	This class should control access to the account number and account balance attributes by implementing the properties:

    o	it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
    o	it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
    o	when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
    o	it should not be possible to delete an account as long as the balance is not zero;

•	test your class behavior by:

    o	setting the balance to 1000;
    o	trying to set the balance to -200;
    o	trying to set a new value for the account number;
    o	trying to deposit 1.000.000;
    o	trying to delete the account attribute containing a non-zero balance.
