Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class User:
...     name = 'No Name Provided'
...     email = ''
...     password = '1234abcd'
...     account_number = 0
... 
>>> class Employee(User):
...     base_pay = 11.00
...     department = 'General'
... 
>>> class Customer(User):
...     mailing_address = ''
