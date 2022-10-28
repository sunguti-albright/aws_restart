-- create a table
CREATE table employees(Id int primary key,name char, department char);
INSERT into employees values (1,"Albright", "IT");
INSERT into employees values (2,"Jane", "Sales");
INSERT into employees values (3, "Newton", "IT");
INSERT into employees values (4, "Luna", "Procurement");
INSERT into employees values (5, "Alice", "Sales");

SELECT * from employees where department = "IT";