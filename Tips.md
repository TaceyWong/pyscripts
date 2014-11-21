#Hidden features of Python

##What are the lesser-known but useful features of the Python programming language?

* Try to limit answers to Python core.
* One feature per answer.
* Give an example and short description of the feature, not just a link to documentation.
* Label the feature using a title as the first line.

##Quick links to answers:


* ***Argument Unpacking***
> *Function argument unpacking*
You can unpack a list or a dictionary as function arguments using * and **.  
For example:
```python
def draw_point(x, y):
    # do some magic
point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}
draw_point(*point_foo)
draw_point(**point_bar)
```
Very useful shortcut since lists, tuples and dicts are widely used as containers.

* Braces
>If you don't like using whitespace to denote scopes, you can use the C-style {} by issuing:
```python
from __future__ import braces
```


* Chaining Comparison Operators
> *Chaining comparison operators*:
```python
>>> x = 5
>>> 1 < x < 10
True
>>> 10 < x < 20 
False
>>> x < 10 < x*10 < 100
True
>>> 10 > x <= 9
True
>>> 5 == x > 4
True
```
In case you're thinking it's doing `1 < x`, which comes out as True, and then comparing `True < 10`, which is also True, then no, that's really not what happens (see the last example.) It's really translating into` 1 < x `and `x < 10`, and `x < 10` and `10 < x * 10 `and` x*10 < 100`, but with less typing and each term is only evaluated once.


* Decorators
>  **Decorators** allow to wrap a function or method in another function that can add functionality, modify arguments or results, etc. You write decorators one line above the function definition, beginning with an "at" sign (`@`).  
Example shows a print_args decorator that prints the decorated function's arguments before calling it:
```python
>>> def print_args(function):
>>>     def wrapper(*args, **kwargs):
>>>         print 'Arguments:', args, kwargs
>>>         return function(*args, **kwargs)
>>>     return wrapper
>>> @print_args
>>> def write(text):
>>>     print text
>>> write('foo')
Arguments: ('foo',) {}
foo
```

* Default Argument Gotchas / Dangers of Mutable Default arguments   
> **Be careful with mutable default arguments**
```python
>>> def foo(x=[]):
...     x.append(1)
...     print x
... 
>>> foo()
[1]
>>> foo()
[1, 1]
>>> foo()
[1, 1, 1]
```
Instead, you should use a sentinel value denoting "not given" and replace with the mutable you'd like as default:
```python
>>> def foo(x=None):
...     if x is None:
...         x = []
...     x.append(1)
...     print x
>>> foo()
[1]
>>> foo()
[1]
```

* Descriptors
> **They're the magic behind a whole bunch of core Python features.**  
>
When you use dotted access to look up a member (eg, x.y), Python first looks for the member in the instance dictionary. If it's not found, it looks for it in the class dictionary. If it finds it in the class dictionary, and the object implements the descriptor protocol, instead of just returning it, Python executes it. A descriptor is any class that implements the `__get__`,`__set__`, or`__delete__`methods.  
>
Here's how you'd implement your own (read-only) version of property using descriptors:
```python
class Property(object):
    def __init__(self, fget):
        self.fget = fget
    def __get__(self, obj, type):
        if obj is None:
            return self
        return self.fget(obj)
```
and you'd use it just like the `built-in property()`:
```python
class MyClass(object):
    @Property
    def foo(self):
        return "Foo!"
```
Descriptors are used in Python to implement properties, bound methods, static methods, class methods and slots, amongst other things. Understanding them makes it easy to see why a lot of things that previously looked like Python 'quirks' are the way they are.  
>
Raymond Hettinger has an [excellent tutorial](http://users.rcn.com/python/download/Descriptor.htm) that does a much better job of describing them than I do.




* Dictionary default `.get` value
> **Dictionaries have a `get()` method**
Dictionaries have a 'get()' method. If you do `d['key']` and key isn't there, you get an exception. If you do `d.get('key')`, you get back None if 'key' isn't there. You can add a second argument to get that item back instead of None, eg: `d.get('key', 0)`.  
>
It's great for things like adding up numbers:
```python
sum[value] = sum.get(value, 0) + 1
```

* Docstring Tests
> Doctest: documentation and unit-testing at the same time.  
>
Example extracted from the Python documentation:  
```python
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    Factorials of floats are OK, but the float must be an exact integer:
    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
def _test():
    import doctest
    doctest.testmod()    
if __name__ == "__main__":
    _test()
 ```   
***Rep1***:Doctests are overrated and pollute the documentation. How often do you test a standalone function without any setUp() ? 

* Ellipsis Slicing Syntax   
> Python's advanced slicing operation has a barely known syntax element, the ellipsis:
```python
>>> class C(object):
...  def __getitem__(self, item):
...   return item
... 
>>> C()[1:2, ..., 3]
(slice(1, 2, None), Ellipsis, 3)
```
Unfortunately it's barely useful as the ellipsis is only supported if tuples are involved.

* Enumeration
> Wrap an iterable with enumerate and it will yield the item along with its index.  
For example:
```python
>>> a = ['a', 'b', 'c', 'd', 'e']
>>> for index, item in enumerate(a): print index, item
...
0 a
1 b
2 c
3 d
4 e
>>>
```
***References***:
>> * [Python tutorial—looping techniques]
(https://docs.python.org/2/tutorial/datastructures.html#looping-techniques)
>> * [Python docs—built-in functions—enumerate]
(https://docs.python.org/2/library/functions.html#enumerate)
>> * [PEP 279]
(https://www.python.org/dev/peps/pep-0279/)




* For/else
> he for...else syntax (see http://docs.python.org/ref/for.html )
```python
for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")
```
The "else" block will be normally executed at the end of the for loop, unless the break is called.  
>
The above code could be emulated as follows:
```python
found = False
for i in foo:
    if i == 0:
        found = True
        break
if not found: 
    print("i was never 0")
```
>
I think the for/else syntax is awkward. It "feels" as if the else clause should be executed if the body of the loop is never executed


* Function as `iter()` argument   
> `iter()` can take a callable argument  
For instance:
```python
def seek_next_line(f):
    for c in iter(lambda: f.read(1),'\n'):
        pass
```
The `iter(callable, until_value)` function repeatedly calls callable and yields its result until until_value is returned.
>
***Rep***You should also add the explanation: iter(callable, sentinel) -> iterator; the callable is called until it returns the sentinel

* Generator expressions
> Creating generators objects  
If you write
```python
x=(n for n in foo if bar(n))
```
you can get out the generator and assign it to x. Now it means you can do
```python
for n in x:
```
The advantage of this is that you don't need intermediate storage, which you would need if you did
```python
x = [n for n in foo if bar(n)]
```
In some cases this can lead to significant speed up.
<br>
You can append many if statements to the end of the generator, basically replicating nested for loops:
```python
>>> n = ((a,b) for a in range(0,2) for b in range(4,6))
>>> for i in n:
...   print i 
(0, 4)
(0, 5)
(1, 4)
(1, 5)
```
***Rep:***Of particular note is the memory overhead savings. Values are computed on-demand, so you never have the entire result of the list comprehension in memory. This is particularly desirable if you later iterate over only part of the list comprehension


* import this
> Main messages :)
```python
import this
# btw look at this module's source :)
```
***Rep:***I've updated my `/usr/lib/python2.6/this.py` replacing the old code with this print `s.translate("".join(chr(64<i<91 and 65+(i-52)%26 or 96<i<123 and 97+(i-84)%26 or i) for i in range(256)))` and it looks much better now!! :-D

* In Place Value Swapping   
> 
```python
>>> a = 10
>>> b = 5
>>> a, b
(10, 5)
>>> a, b = b, a
>>> a, b
(5, 10)
```
The right-hand side of the assignment is an expression that creates a new tuple. The left-hand side of the assignment immediately unpacks that (unreferenced) tuple to the names a and b.  
>
After the assignment, the new tuple is unreferenced and marked for garbage collection, and the values bound to a and b have been swapped.  
> 
As noted in the Python tutorial section on data structures,
>
Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.  
>
***Rep:***It doesn't use more memory. It uses less.. I just wrote it both ways, and de-compiled the bytecode.. the compiler optimizes, as you'd hope it would. dis results showed it's setting up the vars, and then ROT_TWOing. ROT_TWO means 'swap the two top-most stack vars'... Pretty snazzy, actually.

* List stepping
> The step argument in slice operators. For example:
```python
a = [1,2,3,4,5]
>>> a[::2]  # iterate over the whole list in 2-increments
[1,3,5]
```
The special case x[::-1] is a useful idiom for 'x reversed'.
```python
>>> a[::-1]
[5,4,3,2,1]
```  
***Rep1:***much clearer, in my opinion, is the reversed() function. >>> list(reversed(range(4))) [3, 2, 1, 0]  
>
***Rep2:***The problem with reversed() is that it returns an iterator, so if you want to preserve the type of the reversed sequence (tuple, string, list, unicode, user types...), you need an additional step to convert it back.

* \_\_missing\_\_ items
> From 2.5 onwards dicts have a special method `__missing__` that is invoked for missing items:
```python
>>> class MyDict(dict):
...  def __missing__(self, key):
...   self[key] = rv = []
...   return rv
... 
>>> m = MyDict()
>>> m["foo"].append(1)
>>> m["foo"].append(2)
>>> dict(m)
{'foo': [1, 2]}
```
There is also a dict subclass in collections called defaultdict that does pretty much the same but calls a function without arguments for not existing items:
```python
>>> from collections import defaultdict
>>> m = defaultdict(list)
>>> m["foo"].append(1)
>>> m["foo"].append(2)
>>> dict(m)
{'foo': [1, 2]}
```
I recommend converting such dicts to regular dicts before passing them to functions that don't expect such subclasses. A lot of code uses `d[a_key]` and catches KeyErrors to check if an item exists which 
would add a new item to the dict.

* Multi-line Regex
> Readable regular expressions  
>
In Python you can split a regular expression over multiple lines, name your matches and insert comments.
Example verbose syntax (from Dive into Python):
```python
>>> pattern = """
... ^                   # beginning of string
... M{0,4}              # thousands - 0 to 4 M's
... (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
...                     #            or 500-800 (D, followed by 0 to 3 C's)
... (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
...                     #        or 50-80 (L, followed by 0 to 3 X's)
... (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
...                     #        or 5-8 (V, followed by 0 to 3 I's)
... $                   # end of string
... """
>>> re.search(pattern, 'M', re.VERBOSE)
```
Example naming matches (from Regular Expression HOWTO)
```python
>>> p = re.compile(r'(?P<word>\b\w+\b)')
>>> m = p.search( '(((( Lots of punctuation )))' )
>>> m.group('word')
'Lots'
```
You can also verbosely write a regex without using re.VERBOSE thanks to string literal concatenation.
```python
>>> pattern = (
...     "^"                 # beginning of string
...     "M{0,4}"            # thousands - 0 to 4 M's
...     "(CM|CD|D?C{0,3})"  # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
...                         #            or 500-800 (D, followed by 0 to 3 C's)
...     "(XC|XL|L?X{0,3})"  # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
...                         #        or 50-80 (L, followed by 0 to 3 X's)
...     "(IX|IV|V?I{0,3})"  # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
...                         #        or 5-8 (V, followed by 0 to 3 I's)
...     "$"                 # end of string
... )
>>> print pattern
"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
```



* Named string formatting
> % -formatting takes a dictionary (also applies `%i/%s` etc. validation).
```python
>>> print "The %(foo)s is %(bar)i." % {'foo': 'answer', 'bar':42}
The answer is 42.
>>> foo, bar = 'question', 123
>>> print "The %(foo)s is %(bar)i." % locals()
The question is 123.
```
And since `locals()` is also a dictionary, you can simply pass that as a dict and have `% -substitions `from your local variables. I think this is frowned upon, but simplifies things..  
>
**New** Style Formatting
```python
>>> print("The {foo} is {bar}".format(foo='answer', bar=42))
```

* Nested list/generator comprehensions
   
>Nested list comprehensions and generator expressions:
```python
[(i,j) for i in range(3) for j in range(i) ]    
((i,j) for i in range(4) for j in range(i) )
```
These can replace huge chunks of nested-loop code.

* New types at runtime
> Creating new types in a fully dynamic manner
```python
>>> NewType = type("NewType", (object,), {"x": "hello"})
>>> n = NewType()
>>> n.x
"hello"
```
which is exactly the same as
```python
>>> class NewType(object):
>>>     x = "hello"
>>> n = NewType()
>>> n.x
"hello"
```
Probably not the most useful thing, but nice to know.  
>
**Note:** all classes are created at runtime. So you can use the 'class' statement within a conditional, or within a function (very useful for creating families of classes or classes that act as closures). The improvement that 'type' brings is the ability to neatly define a dynamically generated set of attributes (or bases).


* .pth files
>To add more python modules (espcially 3rd party ones), most people seem to use PYTHONPATH environment variables or they add symlinks or directories in their site-packages directories. Another way, is to use `*.pth` files. Here's the official python doc's explanation:
>
"The most convenient way `[to modify python's search path]` is to add a path configuration file to a directory that's already on Python's path, usually to the `.../site-packages/` directory. Path configuration files have an extension of .pth, and each line must contain a single path that will be appended to sys.path. (Because the new paths are appended to sys.path, modules in the added directories will not override standard modules. This means you can't use this mechanism for installing fixed versions of standard modules.)"


* ROT13 Encoding    
> ROT13 is a valid encoding for source code, when you use the right coding declaration at the top of the code file:
```python
#!/usr/bin/env python
# -*- coding: rot13 -*-
cevag "Uryyb fgnpxbiresybj!".rapbqr("rot13")
```
That has nothing to do with the encoding, it is just Python written in Welsh. :-P

* Regex Debugging
> Get the python regex parse tree to debug your regex.  
>
Regular expressions are a great feature of python, but debugging them can be a pain, and it's all too easy to get a regex wrong.
>
Fortunately, python can print the regex parse tree, by passing the undocumented, experimental, hidden flag re.DEBUG (actually, 128) to re.compile.
```python
>>> re.compile("^\[font(?:=(?P<size>[-+][0-9]{1,2}))?\](.*?)[/font]",
    re.DEBUG)
at at_beginning
literal 91
literal 102
literal 111
literal 110
literal 116
max_repeat 0 1
  subpattern None
    literal 61
    subpattern 1
      in
        literal 45
        literal 43
      max_repeat 1 2
        in
          range (48, 57)
literal 93
subpattern 2
  min_repeat 0 65535
    any None
in
  literal 47
  literal 102
  literal 111
  literal 110
  literal 116
 ```
Once you understand the syntax, you can spot your errors. There we can see that I forgot to escape the `[]` in `[/font]`.  
Of course you can combine it with whatever flags you want, like commented regexes:
```python
>>> re.compile("""
 ^              # start of a line
 \[font         # the font tag
 (?:=(?P<size>  # optional [font=+size]
 [-+][0-9]{1,2} # size specification
 ))?
 \]             # end of tag
 (.*?)          # text between the tags
 \[/font\]      # end of the tag
 """, re.DEBUG|re.VERBOSE|re.DOTALL)
```

* Sending to Generators
> Sending values into generator functions. For example having this function:
```python
def mygen():
    """Yield 5 until something else is passed back via send()"""
    a = 5
    while True:
        f = (yield a) #yield a and possibly get f in return
        if f is not None: 
            a = f  #store the new value
```
You can:
```python
>>> g = mygen()
>>> g.next()
5
>>> g.next()
5
>>> g.send(7)  #we send this back to the generator
7
>>> g.next() #now it will yield 7 until we send something else
```


* Tab Completion in Interactive Interpreter
>
```python
try:
    import readline
except ImportError:
    print "Unable to load readline module."
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
>>> class myclass:
...    def function(self):
...       print "my function"
... 
>>> class_instance = myclass()
>>> class_instance.<TAB>
class_instance.__class__   class_instance.__module__
class_instance.__doc__     class_instance.function
>>> class_instance.f<TAB>unction()
```
You will also have to set a `PYTHONSTARTUP` environment variable.  
***Rep:***IPython gives you this plus tons of other neat stuff 

* Ternary Expression    
> Conditional Assignment
```python
x = 3 if (y == 1) else 2
```
It does exactly what it sounds like: "assign 3 to x if y is 1, otherwise assign 2 to x". Note that the parens are not necessary, but I like them for readability. You can also chain it if you have something more complicated:
```python
x = 3 if (y == 1) else 2 if (y == -1) else 1
```
Though at a certain point, it goes a little too far.  
Note that you can use `if ... else` in any expression. For example:
```python
(func1 if y == 1 else func2)(arg1, arg2)
``` 
Here func1 will be called if y is 1 and func2, otherwise. In both cases the corresponding function will be called with arguments arg1 and arg2.  
Analogously, the following is also valid:
```python
x = (class1 if y == 1 else class2)(arg1, arg2)
```
where class1 and class2 are two classes.  
>
***Rep:***The assignment is not the special part. You could just as easily do something like: `return 3 if (y == 1) else 2`.

* try/except/else
> Exception else clause:
```python
try:
  put_4000000000_volts_through_it(parrot)
except Voom:
  print "'E's pining!"
else:
  print "This parrot is no more!"
finally:
  end_sketch()
```
The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the `try ... except` statement.  
>
See http://docs.python.org/tut/node10.html

* Unpacking+print() function


* with statement
> Context managers and the "with" Statement
>
Introduced in PEP 343, a context manager is an object that acts as a run-time context for a suite of statements.
>
Since the feature makes use of new keywords, it is introduced gradually: it is available in Python 2.5 via the __future__ directive. Python 2.6 and above (including Python 3) has it available by default.
>
I have used the "with" statement a lot because I think it's a very useful construct, here is a quick demo:
```python
from __future__ import with_statement
with open('foo.txt', 'w') as f:
    f.write('hello!')
```
What's happening here behind the scenes, is that the "with" statement calls the special `__enter__` and `__exit__` methods on the file object. Exception details are also passed to __exit__ if any exception was raised from the with statement body, allowing for exception handling to happen there.
>
What this does for you in this particular case is that it guarantees that the file is closed when execution falls out of scope of the with suite, regardless if that occurs normally or whether an exception was thrown. It is basically a way of abstracting away common exception-handling code.
>
Other common use cases for this include locking with threads and database transactions.
