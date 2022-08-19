>>> t=(1,2,3,4,5,6)
>>> print(t)
(1, 2, 3, 4, 5, 6)
>>> type(t)
<class 'tuple'>
>>> x=list(t)
>>> type(t)
<class 'tuple'>
>>> x
[1, 2, 3, 4, 5, 6]
>>> x[0]=888
>>> print(t)
(1, 2, 3, 4, 5, 6)
>>> print(x)
[888, 2, 3, 4, 5, 6]
>>> t=tuple(x)
>>> print(t)
(888, 2, 3, 4, 5, 6)
 
 SET OPERATIONS:
s={1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> s1={4,7,8}
>>> s1
{8, 4, 7}
>>> s1.union(s)
{1, 2, 3, 4, 5, 7, 8}
>>> s.intersection(s1)
{4}
>>> s.difference(s1)
{1, 2, 3, 5}
>>> s1.difference(s)
{8, 7}
>>> s1
{8, 4, 7}
>>> s
{1, 2, 3, 4, 5}
>>> s1.update({9})
>>> s1

{8, 9, 4, 7}
>>> s.copy()
{1, 2, 3, 4, 5}
>>> s1.copy()
{8, 9, 4, 7}
>>> s1.update({2,5,7})
>>> s1
{2, 4,5, 7, 8, 9}
>>> s1.update({2,5,7})
>>> s1
{2, 4, 5, 7, 8, 9}
>>> {2, 4, 5, 7, 8, 9}
{2, 4, 5, 7, 8, 9}
>>> 
>>> s1={1,2,3,4,5,6}
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s3={1,2}
>>> s3
{1, 2}
>>> s3.pop()
1
>>> s1.remove(4)
>>> s1
{1, 2, 3, 5, 6}
>>> s1.difference_update(s3)
>>> s1
{1, 3, 5, 6}
>>> s3.clear()
>>> s3
set()
>>> s1.discard(5)
>>> s1
{1, 3, 6}
>>> s1.discard(3)
>>> s1
{1, 2, 4, 5, 6}
>>> s1={1,2,3,4,5,6}
{8, 9, 4, 7}
