Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> c=a+b
>>> c
30
>>> print(a)
10
>>> print(b)
20
>>> c=a>b
>>> print(c)
False
>>> type(a)
<class 'int'>
>>> a=10.5
>>> type(a)
<class 'float'>
>>> ord("a")
97
a=0,1,2,3
>>> a
(0, 1, 2, 3)
>>> type(a)
<class 'tuple'>
 a="string"
>>> a
'string'
>>> type(a)
<class 'str'>
a="a"
>>> a
'a'
>>> type(a)
<class 'str'>
len(a)
1
>>> a=1
>>> b=3
>>> c=a
>>> a=b
>>> b=c
>>> print(a)
3
>>> print(b)
1
c=1+2*3/3*4/5
>>> c
2.6
>>> print(c)
2.6
 c=5*5/5*5
>>> c
25.0
>>> c=10%3
>>> c
1
>>> c=-10%3
>>> c
2
>>> c=10%-3
>>> c
-2
>>> c=-10%-3
>>> c
-1
name=("data science with python")
>>> print(name)
data science with python
>>> print("name=",name)
name= data science with python
print(name[5])
s
>>> print(name[-1])
n
>>> print(name[-2])
o
>>> s1="hell0"
>>> s2="world"
>>> print(s1+s2)
hell0world
>>> s1.upper()
'HELL0'
>>> s2.lower()
'world'
>>> s1.isupper()
False
>>> s2.islower()
True
>>> s1.title()
'Hell0'
>>> s1=s2
>>> s1
'world'
>>> s2=s1
>>> s2
'world'
