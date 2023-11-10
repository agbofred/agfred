---
title: "All the Squiggles"
author: Jed Rembold & Fred
date: November 8, 2023
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1200
transition: slide
hash: true
history: false

---


## Announcements
- PS 5 feedback not ready yet!
- Exam 2 on Friday!
	- Learning Objectives posted
	- Practice Exam 1 & 2 posted with their solutions
- We will post the Enigma project by Friday
	- Not due until Nov 21

<!--
## Review Question {data-notes="Solution: hnktge"}
::::::cols
::::col
Let's consider a greatly simplified Enigma machine, which only has one rotor that is not turning. So the signal goes through the rotor then the reflector and back through the rotor. Given the rotor and reflector mappings shown to the right, what would the word `python` encrypt to?

:::{.poll}
#. `aicmnz`
#. `hnktge`
#. `rfqbls`
#. `zghpmy`
:::

::::

::::col
\begin{tikzpicture}%%width=55%
[label/.style={font=\Large\bf, MGreen},
scale=1.8,
transform shape,
]
\node[label, MRed] at (1,0.5) {Rotor 1};
\foreach[count=\t] \a/\b in {A/D,B/M,C/T,D/W,E/S,F/I,G/L,H/R,I/U,J/Y,K/Q,L/N,M/K,N/F,O/E,P/J,Q/C,R/A,S/Z,T/B,U/P,V/G,W/X,X/O,Y/H,Z/V} {
	\node[label](a) at (0,-\t*0.5) {\a};
	\node[label](b) at (2,-\t*0.5) {\b};
	\draw[-stealth, MBlue, line width=3pt] (a) -- (b);
}


\node[label, MRed] at (6,0.5) {Reflector};
\foreach[count=\t] \a/\b in {A/U,B/Q,C/N,D/T,E/L,F/S,G/Z,H/F,I/M,J/R,K/E,L/H,M/D,N/P,O/X,P/K,Q/I,R/B,S/V,T/Y,U/G,V/J,W/C,X/W,Y/O,Z/A} {
	\node[label](a) at (5,-\t*0.5) {\a};
	\node[label](b) at (7,-\t*0.5) {\b};
	\draw[-stealth, MBlue, line width=3pt] (a) -- (b);
}

\end{tikzpicture}


::::
::::::

## Maps and Dictionaries
- A common form of information associates pairs of data values
	- Commonly called a _map_ in computer science
	- Python calls such a structure a _dictionary_
- A dictionary associates two different values:
	- A simple value called the _key_, which is often a string but doesn't need to be
	- A larger and more complex object called the _value_
- This idea of associating pairs of values is exhibited all over in the real world
	- Actual dictionaries! The words are the keys, the definitions the values.
	- Web addresses! Keys are the urls, the values are the webpage contents.

## Creating Dictionaries
- Python dictionaries use squiggly brackets `{}` to bracket their contents
- Can create an empty dictionary by providing no key-value pairs:
  ```python
  empty_dict = {}
  ```
- If creating a dictionary with key-value pairs
	- Keys are separated from values with a colon `:`
	- Pairs are separated by a comma `,`
  ```python
  generic_dict = {'Bob': 21, 0: False, 13: 'Thirteen'}
  ```


## Review Question
::::::{.cols style='align-items:center'}
::::col
What would be the output of the last print statement in the code to the right?

:::{.poll}
#. True
#. False
#. Error: Index out of range
#. Error: Python will not know how to compare the new Demo objects
:::

::::

::::col
```{.mypython style='max-height:900px; font-size:.8em; line-height:1.3em;'}
class Demo:
	def __init__(self):
		self.x = []

	def add(self, v):
		self.x.append(v)

	def get_x(self):
		return self.x

A, B = Demo(), Demo()
C = B.get_x()
A.add(3)
B.add(3)
C.append(A)
print(A.get_x() == B.get_x())
```

::::
::::::

## Return of the Firework
```{.mypython style="max-height:900px; font-size:0.8em;"}
from pgl import GWindow, GOval, GRect
import random

GW_WIDTH = 500
GW_HEIGHT = 500

def random_color():
    color = "#"
    for _ in range(6):
        color += random.choice("0123456789ABCDEF")
    return color

class Firework:
    """ Creates a new firework with initial flight and then 
	explosion. 
	"""
    def __init__(self, size):
        self.obj = GOval(GW_WIDTH/2, GW_HEIGHT, size, size)
        self.obj.set_filled(True)
        self.obj.set_color("white")
        self.speed = 5
        self.heading = random.randint(60,120)
        self.fuse = random.randint(50,100)
        self.maxsize = random.randint(60,100)
        self.color = random_color()
        self.mode = 0

    def get_object(self):
        """ Returns the firework graphical object. """
        return self.obj

    def should_terminate(self):
        """ Checks if the firework should be removed. """
        return self.mode > 1

    def move(self):
        """ Moves the firework in its initial flight. """
        self.obj.move_polar(self.speed, self.heading)
        self.fuse -= 1
        if self.fuse < 0:
            self.mode += 1
            self.obj.set_color(self.color)

    def explode(self):
        """ Grows the firework explosion upon detonation. """
        R = 2
        x = self.obj.get_x()
        y = self.obj.get_y()
        S = self.obj.get_width()
        self.obj.set_bounds(x-R/2, y-R/2, S+R, S+R)
        if self.obj.get_width() >= self.maxsize:
            self.mode += 1

    def update(self):
        """ Controls what the firework should be doing during 
		each stage. 
		"""
        if self.mode == 0:
            self.move()
        elif self.mode == 1:
            self.explode()
       

def fireworks_show():
    """ Makes a fireworks show! """
    def step():
        """ Calls up update method on all fireworks in the box 
		and removes if necessary.
        """
        for f in firework_box[:]:
            f.update()
            if f.should_terminate():
                gw.remove(f.get_object())
                firework_box.remove(f)


    def give_me_more_fireworks():
        """ Adds more fireworks to the box. """
        new = Firework(2)
        firework_box.append(new)
        gw.add(new.get_object())

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    sky = GRect(GW_WIDTH, GW_HEIGHT)
    sky.set_filled(True)
    gw.add(sky)
    firework_box = []

    gw.set_interval(step, 20)
    gw.set_interval(give_me_more_fireworks, 100)

if __name__ == '__main__':
    fireworks_show()
```
-->
## Maps and Dictionaries
- A common form of information associates pairs of data values
	- Commonly called a _map_ in computer science
	- Python calls such a structure a _dictionary_
- A dictionary associates two different values:
	- A simple value called the _key_, which is often a string but doesn't need to be
	- A larger and more complex object called the _value_
- This idea of associating pairs of values is exhibited all over in the real world
	- Actual dictionaries! The words are the keys, the definitions the values.
	- Web addresses! Keys are the urls, the values are the webpage contents.

## Creating Dictionaries
- Python dictionaries use squiggly brackets `{}` to enclose their contents
- Can create an empty dictionary by providing no key-value pairs:
  ```python
  empty_dict = {}
  ```
- If creating a dictionary with key-value pairs
	- Keys are separated from values with a colon `:`
	- Pairs are separated by a comma `,`
  ```mypython
  generic_dict = {'Bob': 21, 0: False, 13: 'Thirteen'}
  ```

## Keys and Values
- The value of a key-value pair can be **any** Python object, mutable or immutable
	- This include other dictionaries!
- The key is more restricted:
	- Must be immutable
		- So dictionaries or lists can **not** work as a key
		- Tuples can though!
	- Must be unique per dictionary

::::::cols
::::col
:::{.block name=Viable}
```mypython
A = {True: 'Seth', False: 'Jesse'}
B = {'Jill': 13, 'Jack': 12}
C = {(1,2): {'x': 1}}
```
:::
::::

::::col
:::{.block name=Illegal style='border-color:var(--red)'}
```mypython
X = {{'x': 1, 'y': 2}: 'Shark'}
Y = {[1,3,5]: 'Odd'}
Z = {'A': 13, 'B': 24, 'A': 15}
```
:::
::::
::::::



## Selection
- The fundamental operation on dictionaries is selection, which is still indicated with square brackets: `[]`
- Dictionaries though are **unordered**, so it is not a numeric index that goes inside the `[ ]`
- You instead use the key directly to select corresponding values:
  ```python-repl
  >>> A = {'Jack': 12, 'Jill': 13}['Jack']
  >>> print(A)
  13
  >>> B = {True: 13, 0: 'Why?'}[0]
  >>> print(B)
  Why?
  ```

## Losing your keys
- If you attempt to index out a key that doesn't exist:
  ```{.python .badcode}
  A = {'Jack': 12, 'Jill': 13}
  print(A['Jil'])
  ```
  you will get an error!
- If in doubt, check for the presence of a key with the `in` operator:
  ```python
  if 'Jil' in A:
	  print(A['Jil'])
  ```

## Rewriting the Dictionary
- Dictionaries are _mutable_!
	- We can add new key-value pairs
	- We can change the value of corresponding keys
```python-repl
>>> d = {}
>>> d['A'] = 10
>>> d['B'] = 12
>>> print(d)
{'A':10, 'B':12}
>>> d['A'] = d['B']
>>> print(d)
{'A':12, 'B':12}
```



## Grade Sheet Example
- Suppose we had a file of student ids and accompanying scores that we wanted to read into a dictionary and then access.
  ```{.mypython style='max-height:700px; font-size:.8em; line-heigh:2em;'}
  def read_to_dict(filename):
      dictionary = {}
      with open(filename) as f:
          for line in f:
              ID, score = line.strip().split(',')
              dictionary[ID] = score
      return dictionary
  
  def get_student_score():
      scores = read_to_dict('SampleGrades.txt')
      done = False
      while not done:
          student_id = input('Enter a student id number: ')
          if student_id == "":
              done = True
          else:
              if student_id in scores:
                  print(f"Student got a {scores[student_id]}.")
              else:
                  print(f"Student id {student_id} was not found in classlist")
  ```

## Understanding Check {data-notes="Solution: [125,167,204]"}
What is the printed value of the below code?
```mypython
A = [
	{'name': 'Jill',  'weight':125, 'height':62},
	{'name': 'Sam',   'height':68},
	{'name': 'Bobby', 'height':72},
]
A.append({'weight':204, 'height':70, 'name':'Jim'})
B= A[1]
B['weight'] = 167
print([d['weight'] for d in A if 'weight' in d])
```


<div class='cols'>
<div class='col poll'>
<ol>
	<li> `[100,204]`</li>
	<li>`[156,173,204]`</li>
	</ol>
</div>
<div class='col poll'>
<ol style='counter-reset: li 2'>
	<li> `[100,167,173,204]` </li>
	<li>`[125,167,204]` </li>
</ol>
</div>
</div>


## Iterating through a Dictionary
- Frequently we might want to iterate through a dictionary, checking either its values or its keys
- Python supports iteration with the `for` statement, which has the form of:
  ```mypython
  for key in dictionary:
  	  value = dictionary[key]
  	  |||code to work with that key and value|||
  ```
- You can also use the `.items` method to grab both key and values together:
	- Returns a tuple with both the key and corresponding pair
  ```mypython
  for key, value in dictionary.items():
  	  |||code to work with that key and value|||
  ```

## Finding Students by grade
```{.mypython style='max-height:900px'}
def get_students_with_score():
    scores = read_to_dict('SampleGrades.txt')
    done = False
    while not done:
        des_grade = input('Enter a letter grade: ')
        if des_grade == "":
            done = True
        else:
            for st_id, grade in scores.items():
                if grade == des_grade.strip().upper():
                    print(f"{st_id} got a {grade}")
```


## Common Dictionary Methods

Method call | Description
---|-----
`len(dict)`{.python} | Returns the number of key-value pairs in the dictionary
`dict.get(key, value)`{.python} | Returns the value associated with the `key` in the dictionary. If the key is not found, returns the specified value, which is `None` by default
`dict.pop(key)`{.python} | Removes the key-value pair corresponding to `key` and returns the associated value. Will raise an error if the key is not found.
`dict.clear()`{.python} | Removes all key-value pairs from the dictionary, leaving it empty.
`dict.items()`{.python} | Returns an iterable object that cycles through the successive tuples consisting of a key-value pair.


## Dictionary Records
- While most commonly used to indicate mappings, dictionaries have seen increased use of late as structures to store records
- Looks surprisingly close to our original template of:
  ```python
  boss = {
	  'name': 'Scrooge',
	  'title': 'founder',
	  'salary': 1000
	  }
  ```
- Allows easy access of attributes without worrying about ordering
  ```python
  print(boss['name'])
  ```


<!--  for later
## Mathematical Sets
- A _set_ is an unordered collection of **distinct** values.
	- **digits** =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
	- **evens** =  0, 2, 4, 6, 8 
	- **odds** =  1, 3, 5, 7, 9 
	- **primes** =  2, 3, 5, 7 
	- **squares** =  0, 1, 4, 9 
	- **primary** =  red, green, blue 
	- **$\mathbf{R}$** =  x where x is a real number 
	- **$\mathbf{Z}$** =  x where x is an integer 
	- **$\mathbf{N}$** =  x where x is an integer >=0 
- The set with no elements is call the _empty set_ (∅)

## Pythonic Sets
- Enclosed within squiggly brackets
- No key-value pairs, just single values separated by commas
```python
digits = { 0, 1, 2, 3, 4, 6, 7, 8, 9 }
squares = { 0, 1, 4, 9 }
primary = { "red", "green", "blue" }
```
- Set elements must be immutable
- Sets themselves are generally mutable
- Can **not** create an empty set just using `{ }`!
	- Python assumes this to be an empty dictionary!
	- Must instead use `set()`.

## Set Operations
- The fundamental set operation is _membership_ (∈)
	- 3 ∈ **primes**
	- 3 ∉ **evens**
	- red ∈ **primary**
	- -1 ∉ **N**
- The _union_ of the sets $A$ and $B$ ($A \cup B$) consists of all elements in either $A$ or $B$ or both.
- The _intersection_ of the sets $A$ and $B$ ($A \cap B$) consists of all elements in both $A$ and $B$.
- The _set difference_ of $A$ and $B$ ($A - B$) consists of all elements in $A$ but not in $B$.
- The _symmetric set difference_ of $A$ and $B$ ($A\triangle B$) consists of all elements in $A$ or $B$ but not in both.

## Python Implementations
- Python's built-in implementation of sets supports all these same operations
- Can either use appropriately named methods on sets or operators between sets
- Membership
	`3 in primes`{.inlinecode}

:::{.cols}
::::{.col}
- Union:
	`A.union(B)`{.inlinecode}
	`A | B`{.inlinecode .python}
- Intersection
	`A.intersection(B)`{.inlinecode}
	`A & B`{.inlinecode .python}
::::

::::{.col}
- Difference
	`A.difference(B)`{.inlinecode}
	`A - B`{.inlinecode .python}
- Symmetric difference
	`A.symmetric_difference(B)`{.inlinecode}
	`A ^ B`{.inlinecode .python}
::::
:::


## Venn Diagrams
- A _Venn Diagram_ is a graphical representation of a set which indicates common elements as overlapping areas
- The following Venn diagrams illustrate the effect of the 4 primary set operations

::::::cols
::::col
![](../images/Set_Union.svg)
<br>
![](../images/Set_Diff.svg)

::::

::::col
![](../images/Set_Intersect.svg)
<br>
![](../images/Set_SymDiff.svg)

::::
::::::
-->

<!--
## Losing the Keys
- Dictionaries are unordered, all the lookup information comes from the key
- When you ask for an value corresponding to a certain key, the computer needs to search the dictionary for a matching key
- There are several possible approaches to doing this, which we'll talk a bit more about later in the semester
	- Most strategies take longer the larger the dictionary is (which probably makes sense)
	- One strategy though, called _hashing_, implements a function on the space of possible keys, which ends up telling the implementation exactly where to look for the matching item. The result being that this strategy does _not_ take more time for a larger dictionary!

- Possible implementations:
	- _Linear search_: This implementation keeps track of the name-value pairs in an array, and just loops through the array to find or place new keys in $\mathcal{O}(N)$ time
	- _Binary search_: This implementation keeps track of the name-value pairs in an array but keeps them sorted by some method. Then uses binary search to find or place new keys in $\mathcal{O}{\log N}$ time


## Hashing
- Can seem surprising or magical that we could have a method that takes a constant amount of time to look up a value independent of the length of the map or dictionary!
- Envision finding a word in a dictionary
	- Most have markings along the edge where each section of letters starts, so you know where to start looking
- The most common map and dictionary implementations use a strategy called _hashing_, which is conceptually similar to using the section markings on a dictionary.
	- Critical idea is that can you massively improve performance if you use the key itself to help you figure out where to look

## Hash Codes, not Browns
- Hash codes must follow a set of guidelines (or a code of conduct):
	#. The hash code must be relatively easy to compute
	#. The hash code for a particular object must always be the same for a given Python session
	#. If two objects are identical, they must have the same hash code
	#. The hash codes must be distributed as randomly/evenly as possible over the space of possible keys
- Python has a built-in function called `hash` that takes an object and returns an integer, which is called the _hash code_ for that object
- Maps using the hashing algorithm use the hash code for a key as a starting point to help find the associated value.


## Bucket Hashing
- One common strategy is to choose a certain number of _buckets_ to make up an array, where each object's hash will place it into a particular bucket
	- Would mean that, having checked a key's hash, you'd know which bucket to look in!
- In practice, the number of buckets is smaller than the number of hash codes, so you need a way to decide on what hash code corresponds to which bucket.
	- Typically done with a remainder operation along the lines of
	```python
	bucket = abs(hash(key)) % num_buckets
	```
- Some buckets will still end up with multiple key-value pairs. These are called _collisions_ and lower the efficiency of the algorithm.
- Since hash codes are spread around equally, each bucket in theory would end up with similar numbers of key-value pairs


## Bucket Hashing Example 
```{.python style='max-height:900px; font-size:0.8em;'}
class Dictionary:
    NBUCKETS = 10

    def __init__(self):
        self.buckets = [ [] for _ in range(Dictionary.NBUCKETS)]

    def get(self, key):
        H = hash(key)
        bucket_id = abs(H) % Dictionary.NBUCKETS
        for pair in self.buckets[bucket_id]:
            if pair[0] == key:
                return pair[1]
        return None

    def put(self, key, value):
        H = hash(key)
        bucket_id = abs(H) % Dictionary.NBUCKETS
        bucket = self.buckets[bucket_id]
        for i in range(len(bucket)):
			bkey, bvalue = bucket[i]
            if bkey == key:
                bucket[i] = (key, value)
                return
        bucket.append((key,value))

    def __repr__(self):
        return repr(self.buckets)
```
-->
