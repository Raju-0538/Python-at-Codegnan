Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ls
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
a,b,c = 10,20,30
b
20
print(num2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(num2)
NameError: name 'num2' is not defined
print(b)
20
name = 'Raj kumar'
name
'Raj kumar'
course = Codegnan
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    course = Codegnan
NameError: name 'Codegnan' is not defined
course = "Codegnan"
course
'Codegnan'
del name,course
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c']
id(b)
140708731880968
id(a)
140708731880648
c = 10
id(c)
140708731880648
a = b+c
a
30
a,b,c
(30, 20, 10)

id(a)
140708731881288
b = c*3
b
30
id(b)
140708731881288
x = y = z = 277
x,y,z
(277, 277, 277)
id(x)
1976593161712
id(y)
1976593161712
del a,b,c
a,b = 10,20
a,b
(10, 20)
b,a = a,b
a,b
(20, 10)
>>> q = int("500")
>>> w = int("500")
>>> id(q)
1976593161488
>>> id(w)
1976593161744
>>> del q,w
>>> q = int("6")
>>> w = int("6")
>>> q is w
True
>>> a = 6
>>> a is w
True
>>> a is q
True
>>>  f = 199
...  
SyntaxError: unexpected indent
>>> f = 499
>>> g = 499
>>> f is g
False
>>> bool(1)
True
>>> bool(10)
True
>>> bool(-9)
True
>>> bool(hi)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    bool(hi)
NameError: name 'hi' is not defined
>>> bool('hi')
True
>>> bool([0])
True
>>> a=10,b=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a == 10, b==20
(False, False)
