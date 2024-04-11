Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Creating a class
>>> class Person:
...     def_init_(self,name,age,gender)
...     self.name=name
...     self.age=age
...     self.gender=gender
...     #creating method introduction
...     def introduction(self):
...         print(f'Hello,my name is{self.name},I am{self.age}years old,and I am{self.gender}')
...         #Create an instance of the person class
...         person1=Person('Lebo',22,'Female')
...         person2=Person('Koketjo',30,'Female')
...         person3=Person('Jeff',43,'Male')
...         #invoking the introduce method to display the person information
...         person1.introduce()
... 
...         
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    class Person:
  File "<pyshell#15>", line 2, in Person
    def_init_(self,name,age,gender)
NameError: name 'def_init_' is not defined
