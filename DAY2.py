Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Welcome to day2')
Welcome to day2
>>> Hours='thirty'
>>> print(Hours)
thirty
>>> Days='Thirty days'
>>> print(Days[0])
T
>>> 
>>> Challenge= 'I will win'
>>> print(Challenge[0:5])
I wil
>>> print(len(Challenge))
10
>>> print(Challenge.upper())
I WILL WIN
>>> a= '30 days 30 hours'
>>> b= 'I will win'
>>> c=a+b
>>> print(c)
30 days 30 hoursI will win
>>> c= a+ ' ' +b
>>> print(c)
30 days 30 hours I will win
>>> text='Thirty days and Thirty hours'
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> x=text.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> print(text.find('T'))
0
>>> print(text.find('t'))
4
>>> print(text.isalpha())
False
>>> text=ThirtyDaysThirtyHours
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    text=ThirtyDaysThirtyHours
NameError: name 'ThirtyDaysThirtyHours' is not defined
>>> text='ThirtyDaysThirtyHours'
>>> print(text.isalpha())
True
>>> print(text.isalnum())
True
>>> text='Thirty days thirty hours'
>>> print(text.isalnum())
False
>>> 