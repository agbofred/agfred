---
title: "Inputting Other Data Types"
author: Jed Rembold
date: February 1, 2023
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
hash: true
history: false

---


## Announcements
- Problem Set 2 due Friday!
	- I'm halfway through PS1 feedback, should be coming back tomorrow
- A reminder that you can contact your section leaders to ask questions as well!
	- Don't wait until 11pm on Friday night!
- I'll be updating the syllabus schedule, as we added a chapter to the book, but it shouldn't make a huge difference outside of chapter numbering
	- I'll also actually fix the old website schedule, since I realized I failed to update that originally
<!--- Will be spending part of next Monday introducing the first project: Wordle-->
- Polling: [rembold-class.ddns.net](http://rembold-class.ddns.net)

## Review Question
::::::cols
::::col
Examining the code to the right, what is the output value if I evaluate the expression `func2(10)`?


:::{.poll}
#. 24
#. 19
#. 10
#. 5
:::

::::

::::{.col style='font-size:.9em; flex-grow:1.5'}
```python
def func1(x):
	if x > 10:
		return 3 + x
	else:
		return 0

def func2(y):
	A = func1(y+1)
	if y % 2 == 0 or A ** 3 > 30:
		A -= 5
	return A + y
```
::::
::::::

## Shorting the Circuit
- Python evaluates _and_ and _or_ operators using a strategy called _short-circuit mode_
- Only evaluates the right operand if it actually needs to
	- Example: if `n=0`, then the `x % n == 0` is never actually checked in the statement

		```python
		n != 0 and x % n == 0
		```

		since `n != 0` already is `False` and `False and ` _anything_ is always `False`
- Can use short-circuit to prevent errors: the above `x % n == 0` statement would have erred out if `n=0`



## Other Data Types
- Numbers are great, but what about other types of data?
- We will spend considerable time on the details of these data types later
- For now, let us introduce:
	- strings!
	- lists!


## Lists
- A _list_ in Python represents a sequence of **any** type of data
- Denote by bordering with square brackets (`[`, `]`) with commas separating each element of the sequence
	- Each element could be any data type (even mixing from element to element!)
	- `['This', 'is', 'a', 'list']`
	- `['Great', 4, 'storing', 5 * 10]`
- There are many operations that we will see are possible on lists, but will start with only the basics


## Sequences
- Both _strings_ and _lists_ are examples of a more general type called a _sequence_
	- Strings are sequences of characters
	- Lists are sequences of anything
- Sequences are _ordered_, so we can number off their elements, which we call their _index_
	- Counting in Python always starts with **0**, so the first element of the sequence has index 0
- Python defines operations that work on all sequences
	- Selecting an individual element out of a sequence
	- Concatenating two sequences together
	- Determing the number of elements in a sequence

## Selection
- You can select or "pluck out" just a single element from a sequence using square brackets `[` `]`
	- There are **no** commas between these square brackets, so they can't be confused with a list
	- The square brackets come after the sequence (or variable name representing a sequence)
	- Inside the square brackets, you place the index number of the element you want to select

:::::cols
::::{.col .fragment}
```python
>>> A = [2, 4, 6, 8]
>>> print(A[1])
4
```
::::
::::{.col .fragment}
```python
>>> B = "Spaghetti"
>>> print(B[6])
't'
```
::::
:::::

## Concatenation
- _Concatenation_ is the act of taking two separate objects and bringing them together to create a single object
- For sequences, concatenation takes the contents of one sequence and add them to the end of another sequence
- The `+` operator concatenates sequences
	- This is why it is important to keep track of your variable types! `+` will **add** two integers, but will **concatenate** two strings
  
  :::::cols
  ::::{.col .fragment}
  ```python
  >>> A = 'fish'
  >>> B = 'sticks'
  >>> print(A + B)
  'fishsticks'
  ```
  ::::
  ::::{.col .fragment}
  ```python
  >>> A = [1, 'fish']
  >>> B = [2, 'fish']
  >>> print(A + B)
  [1, 'fish', 2, 'fish']
  ```
  ::::
  :::::

## Lengths
- The number of elements in a sequence is commonly called its _length_, and can be given by the `len( )` function
- Simply place the sequence you desire to know the length of between the parentheses:

  ```python
  >>> len("spaghetti")
  9
  ```
- You can have sequences of 0 length as well!
  
  ```python
  >>> A = ""
  >>> B = [ ]
  >>> print( len(A) + len(B) )
  0
  ```

## Understanding Check
:::::cols
::::col
What would be the printed output of the code to the right?

:::poll
#. 12
#. 13
#. 14
#. 15
:::
::::
::::col
```python
A = "hots"
B = ["fire", A + A]
C = A[3] + A[1]
B += [C + C[0]]
D = B[0] + B[1] + B[2]
print(len(D))
```

::::
:::::


## Input: `input`
- To retrieve data from a user, we can use Python's built-in `input()` function
- The form will generally look like:

  ```python
  variable = input(prompt_text)
  ```
    - `variable` is the variable name you want to assign the user's typed input to
	- `prompt_text` is the string that will be displayed on the screen to communicate to the user what they should be doing
- The `input()` function **always returns a string**
	- If you want to get an integer from the user, you will need to convert it yourself after retrieving it
	
	  ```python
	  num = int(input('Pick a number between 1 and 10: '))
	  ```


## Running a Program
- Python programs specify what part of the code is supposed to be executed when a program is run using a few special lines at the end of the program

	```python
	if __name__ == '__main__':
		function_to_run()
	```
	- `function_to_run` is the name of whatever function you want to execute when the program is run directly
- Patterns of this sort are commonly called _boilerplate_
	- Less important to fully understand all the pieces of it now
	- Is important to understand what it is doing and how to implement it correctly

## An adding program
:::{style='align:center;'}
``` {.python style="max-height: 800px; width:100%"}
# File: AddTwoIntegers.py

"""
This program adds two integers entered by the user.
"""

def add_two_integers():
	print("This program adds two integers.")
	n1 = int(input("Enter n1? "))
	n2 = int(input("Enter n2? "))
	total = n1 + n2
	print(f"The sum is: {total}")

# Startup boilerplate
if __name__ == '__main__':
	add_two_integers()
```
:::

## Common Patterns
- Many programs in programming can be approached similarly by using a particular _idiom_ or _pattern_
<!--- A common one with repetition is to use a variable to keep track of the loop state until something particular happens (the sentinel is triggered)-->


::::::cols
::::col

:::{.block name="Loop Until..." style='font-size:.75em'}
- Using a variable to track/control a loop state

  ```{.python style='width:100%'}
  finished = False
  while not finished:
  	  line = input("Enter a number: ")
  	  if line == "":
  	  	  finished = True
  	  else:
  	  	  print(line)
  ```
:::

::::

::::col
:::{.block name="Building Sequences" style='font-size:.75em'}
- Building up a sequence from nothing using concatenation

  ```{.python style='width:100%'}
  new = ""
  word = "fantastical"
  i = 0
  while i < len(word):
  	  new += word[i]
  	  i += 2
  ```
:::

::::
::::::



## Visiting the library(ies)
- A huge strength of Python is that it offers a very large number of code collections called _libraries_
	- Can save you the effort from writing that code yourself!
- Requires you to _import_ that library, which can take several different forms
	- Most common is to use `import` to grab everything in a library

		```python
		import math
		```
		- You must then access any function in that library using its _fully qualified name_, which includes the library name (`var = math.sqrt(4)`)
	- Can also use `from ... import` to grab specific functions from the library

		```python
		from math import sqrt
		```
		- You do not need to use the library name then when you call it (`var = sqrt(4)`)


## Useful `math` definitions

:::{style='font-size:.9em'}

Code | Description
--- | ---
`math.pi` | The mathematical constant $\pi$
`math.e` | The mathematical constant $e$
`math.sqrt(x)` | The square root of x
`math.log(x)` | The natural logarithm of x
`math.log10(x)` | The base 10 logarithm of x
`math.sin(x)` | The sine of x in radians
`math.cos(x)` | The cosine of x in radians
`math.asin(x)` | The arcsin of x
`math.degrees(x)` | Converts from radians to degrees
`math.radians(x)` | Converts from degrees to radians

:::


<!--
## Understanding Check
What is the final printed value in the code below?

:::: cols
::: col
:::::{.poll}
#. `True`
#. `False`
#. `"4Quiz"`
#. This would give an error
:::::
:::

::: {.col style="flex-grow:2;"}
```python
A = 10
B = 4
C = "Quiz"
A *= len(C)
if A > 40 and C != "C":
	print(str(B)+C)
else:
	print(A < B or not (C == "C"))

```
:::
::::
-->


<!--
## Understanding Check
::::: cols

:::: col
```python
x = 7
y = 0
while x >= 0:
	y += x
	x -= 2
print(y)
```
::::

:::: col
What will the printed output of the code to the left?

:::{.poll}
#. 15
#. 16
#. 28
#. Infinite Loop
:::
::::

:::::


## The `range()` iterable
- Need an easy way to produce or describe a range of numeric values
- The built-in `range()` function handles this and produces the needed iterable object
- Takes 1, 2, or 3 arguments:
	- Start (default 0): where to start the sequence at
	- Stop (mandatory): the sequence ends just _below_ this value (does not include it!)
	- Step (default 1): what value the sequence counts by
<br><br>

:::{.block name='Warning!'}
Be careful, the `range` function will stop one step _before_ the final stop value.
:::


## For ranging examples
- Providing just a stop argument:

	```python
	for n in range(5):
		print(n)
	```
- Providing a start and stop:

	```python
	for n in range(1,11):
		print(n)
	```
- Providing a start, stop, and step:

	```python
	for n in range(10,0,-1):
		print(n)
	```


## Iterating over sequences
- We can also use a `for` loop to iterate directly over a sequence of values
- Python supports many different types of sequences, but thus far we only know about one: strings!
	- Recall strings are just a sequence of individual characters
- We can loop through a string to examine each individual character
- Example looping through to count occurrences of a given letter:

	```python
	def count_letters(letter, string):
		count = 0
		for character in string:
			if character == letter:
				count += 1
		return count
	```

-->
