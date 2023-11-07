---
title: Testing Ranges
author: Jed Rembold & Fred Agbo
date: September 13, 2023
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: slide
hash: true
history: false

---


## Announcements
- Problem Set 2 is posted and due on Tuesday next week ***at 12 noon***
	- Feedback for PS1 will be ready by tomorrow! Don't just look at the scores (which could be quite good). **Look at the comments**
- If you have just joined the course and not in section yet, see me after to class to fill out the form
- We will be concluding chapter 2 of the text today. Hope eveyone is reading the text along
- Polling continues today! Remember to use this link [https://www.polleverywhere.com/agbofred203](https://www.polleverywhere.com/agbofred203) when it becomes **active**


<!--
## Review Question
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
B += C + C[0]
D = B[0] + B[1] + B[2]
print(len(D))
```

::::
:::::

## Boolean Expressions
- Python defines two types of operators that work with Boolean data: _relational operators_ and _logical operators_
- Relational operators compare values of other types and produce a `True`/`False` result:

	---- ----------------- - - - ---- --------------------
	`==` Equals                  `!=` Not equals
	 `<` Less than               `<=` Less than or equal too
	 `>` Greater than            `>=` Greater than or equal to
	---- ----------------- - - - ---- --------------------
- Be careful! `==` _compares_ two booleans. A single `=` _assigns_ a variable. The odds are high you'll use one when you meant the other at least once this semester!


## The Vulcan Way
- Logical operators act on Boolean pairings

	Operator | Description
	---|---
	`A and B` | True if both terms True, False otherwise
	`A or B` | True if _any_ term is True, False otherwise
	`not A` | True if A False, False if A True (opposite)

::: incremental
- Order of operations follows parentheses and then proceeds left to right
- Careful that `or` is still `True` if both options are `True` 
- Similarly, careful with combining `not` with `and` and `or`
	- "Not A or B" in common English is not the same as `not A or B`
:::
-->

## Review Question
What value is printed when the code to the right runs?

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

<!--
## Shorting the Circuit
- Python evaluates _and_ and _or_ operators using a strategy called _short-circuit mode_
- Only evaluates the right operand if it actually needs to
	- Example: if `n=0`, then the `x % n == 0` is never actually checked in the statement

		```python
		n != 0 and x % n == 0
		```

		since `n != 0` already is `False` and `False and ` _anything_ is always `False`
- Can use short-circuit to prevent errors: the above `x % n == 0` statement would have erred out if `n=0`



## Sentinels
- Many programs in programming can be approached similarly by using a particular _idiom_ or _pattern_
- A common one with repetition is to use a variable to keep track of the loop state until something particular happens (the sentinel is triggered)
<br><br>

```python
finished = False
while not finished:
	line = input("Enter a number: ")
	if line == "":
		finished = True
	else:
		print(line)
```

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
-->

## Sentinels
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

## Extra `if` functionality
::::::cols
::::col
- Karel could only use `if` and `else`
- Python also supports as `elif` statement
- Let's you chain together multiple mutually exclusive condition checks
- You can include as many `elif` chained statements as you want
::::

::::col
```{.python style='max-height:900px; font-size:0.75em'}
if condition_1:
	# Run this code if 
	# condition 1 is true
elif condition_2:
	# This code runs if 
	# condition 1 is false
	# but condition 2 is true
elif condition_3:
	# Runs if both condition 1
	# and 2 fail but condition
	# 3 is true
else:
	# This code runs if 
	# all above conditions 
	# fail
```

::::
::::::

## For Loop Anatomy
- We have already seen `for` loops in Karel, but let's expand on their use:
- The more general syntax of a `for` loop looks like:

	```python
	for variable_name in sequence:
		# code to loop over
	```
	- `variable_name` is a variable name that will be assigned every value in the sequence over the course of the loop
	- `sequence` is any expression that produces a variable that supports iteration
		- We've already seen `range()` fill this role
		- **Any** sequence works though! So strings and lists can also be looped over!

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
- We can loop through a string or list to examine each individual character or element
- Example of looping through a word to count occurrences of a given letter:

	```python
	def count_letters(letter, string):
		count = 0
		for character in string:
			if character == letter:
				count += 1
		return count
	```

## Test Yourself
- It is easy to make mistakes when writing code
	- Syntax mistakes
	- Typos or operations mistakes
	- Overall conceptual mistakes
- Given that making mistakes is entirely natural, it is also imperative that looking for mistakes become entirely natural
- You known what the desired goal is for basically every problem in this class. **Test your code!**


## Way of Testing
:::incremental
- Run your code early and often
	- If your code is breaking at something early, it is not going to fix itself if you continue
- Test outputs directly
	- Problems will generally give several example outputs of desired functions
	- For your own functions, you should know what you want them to be outputting
	- Run a function as isolated as you can make it after writing it, and _ensure_ that it is performing as expected
- Write code to test code
	- Wherever possible, I provide some automated tests that can be run
	- You can (and should) write your own tests as well. They need not be complicated!!
:::

## Assertions
- You can use Python's `assert` statement to write test functions, which take the form:
  ```python
  assert condition
  ```
  where `condition` is any operation that returns a `True` or `False`
- Assert statements "expect" a condition to yield a `True`, and if they do, nothing happens
	- No news is good news in this case
- If an assert condition evaluates to `False`, an error is raised
- Naming your test functions starting with the word `test_` will make them automatically discoverable by other tools


## Testing Example
- Suppose we wanted to write some checks of the `count_letters` function from earlier

```python
def test_count_letters():
	""" Runs several tests on the function count_letters """
	assert count_letters("z", "banana") == 0
	assert count_letters("a", "strawberry") == 1
	assert count_letters("A", "apple") == 0
	assert count_letters("e", "eerie") == 3
```
<!--
## Showcasing Autochecks
- When you submit code to GitHub, my pre-written tests are run
	- If **any** check fails, you'll see the red X (and possibly get an email)
	- Let's look at how to get information about what went wrong
- VSCode actually can run all the tests locally as well
	- Let's also walk through how that works (and looks)


## Introduction to Wordle
::::::cols
::::col
- Our first project will be Wordle
- Milestone guide will be posted this weekend
- Not due until the end of the month
- You still have another PS due in between
- Could complete in a week, but we are getting it to you early in case you want to start sooner
::::

::::col
![The game of Wordle](../images/wordle.png)
::::
::::::

## Your Responsibilities
- We will provide you with a custom data type that will handle all the graphics and user interaction
	- Don't worry, you'll have a chance to implement your own GUIs later in the semester!
- Your responsibilities:
	- Displaying and reading letters from boxes
	- Evaluating whether a word is valid
	- Determining what color each letter of a word should be
	- Determining when victory or defeat occurs


## Your Toolbox
- Special functions provided by the graphics data type
	- These will be well documented, and include things like
		- Getting or setting a letter in a particular box
		- Getting or changing the color of a given box
		- Changing which row is used when characters are entered
- Variables and functions
- Control statements
	- Good use of loops and if statements will be very useful
- Basic string functions


## An Approach to Success
- Each project is accompanied by a highly detailed guide: **read it!**
	- Explains background ideas so that you can understand the big picture of what you are needing to do
	- Also included a breakdown of individual _milestones_
		- A _milestone_ is a discrete checkpoint that you should ensure is working (and that you understand!) before moving on
- Projects are all about managing complexity. If you start trying to implement milestones out of order, you are asking for disaster
- Don't let yourself get overwhelmed by scale. Focus on one particular milestone at a time, which should involve focusing only on a small part of your overall code


-->
