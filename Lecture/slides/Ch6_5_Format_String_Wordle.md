---
title: "Testing English Wordle"
author: Jed Rembold & Fred Agbo
date: September 25, 2023
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
- Problem set 3 is due **tomorrow at 12:noon**
- I am working on returning PS 2. Apologies for the few remaining 
- First project will be posted tomorrow, will be due on October 3rd
- Polling continues today! Remember to use this link [https://www.polleverywhere.com/agbofred203](https://www.polleverywhere.com/agbofred203) when it becomes **active**
<!--
## Review Question {data-notes="Answer is B, as it would not print the 0"}
Which of the below blocks of code would print something different from the others?

::::: cols

:::: col
:::{.block name=A}
```{.python style='margin-left:1em'}
for n in range(10):
	if n % 2 == 0:
		print(n)
```
:::
:::{.block name=B}
```{.python style='margin-left:1em'}
for i in range(0,10,2):
	if i > 0:
		print(i)
```
:::
::::

:::: col
:::{.block name=C}
```{.python style='margin-left:1em'}
for j in '02468':
	L = int(j)
	print(L)

```
:::
:::{.block name=D}
```{.python style='margin-left:1em'}
for k in range(0,10):
	if not (k % 2 > 0):
		print(k)
```
:::
::::
:::::

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

## Showcasing Autochecks
- When you submit code to GitHub, my pre-written tests are run
	- If **any** check fails, you'll see the red X (and possibly get an email)
	- Let's look at how to get information about what went wrong
- VSCode actually can run all the tests locally as well
	- Let's also walk through how that works (and looks)


## Algorithms
- Recall that when approaching a computation problem, you **must** have an algorithm designed before you start coding
- An **algorithm** is a problem-solving strategy, and should be:
	- _Clear and unambiguous_, in the sense that it is understandable and leaves no gaps
	- _Effective_, in the sense that each step is actually possible
	- _Finite_, in the sense that it ends at some point
- You need to come up with an algorithm before you start coding!

## Creating your own Algorithms
- Some useful hints to keep in mind when constructing your own algorithms:
	- Think about how you would solve the problem **without** a computer. You can't write code if you don't understand what you want the computer to do.
	- Try to use tools and programming patterns you have already seen. It is often far easier to write programs by assembling pieces from code you have already seen than writing each program entirely from scratch.
		- Common patterns we have already seen include: looping over sequences, using variables to track/control a loop, and building up sequences from empty sequences using concatenation
	- Recognize that the program you write is highly unlikely to work the first time
		- Errors can occasionally be in your algorithms
		- More often, early on, errors are in your translating of the algorithm into Python
-->


## Formatting Strings
- F-strings allow us to easily substitute in values, but what if we want those values to have a particular format?
	- Rounded to the nearest two decimal places, for example
- One option would be to handle all this before the substitution manually
- Python gives a more streamlined method, using a _format spec_
- A format spec will be given inside the `{}` placeholder
	- Comes after the variable/value itself
	- There is a colon between the variable/value and the format spec
  ```python
  A = 10.234
  print(f"The value of A is {A:0.2f}")
  ```

## Shaping your format
- A Format spec is a special string that determine the desired format
- Lots we can do, but we rarely need to do it all at once
- The basic building blocks (square brackets just to group):
<center>
<br>
<span style="font-family: monospace">
<span class="fragment highlight-current-red" data-fragment-index=6>[[fill]align]</span><!--
--><span class="fragment highlight-current-red" data-fragment-index=5>[sign]</span><!--
--><span class="fragment highlight-current-red" data-fragment-index=4>[width]</span><!--
--><span class="fragment highlight-current-red" data-fragment-index=3>[,]</span><!--
--><span class="fragment highlight-current-red" data-fragment-index=2>[.precision]</span><!--
--><span class="fragment highlight-current-red" data-fragment-index=1>[type]</span>
</span>
</center>

<hr>

<div class="only-fragment fragment current" data-fragment-index=1>
- Type
	- How you want the object represented as a string
	- "d" - base-10 integer
	- "f" - float or decimal
	- "e" - scientific notation
	- More on next slide
</div>
<div class="only-fragment fragment current" data-fragment-index=2>
- Precision
	- How many digits to display after a decimal point
	- Details can vary a little by conversion type
</div>
<div class="only-fragment fragment current" data-fragment-index=3>
- Grouping?
	- A comma here indicates that numbers should be grouped in sets of 3 and separated with a comma
</div>
<div class="only-fragment fragment current" data-fragment-index=4>
- Width
	- The *minimum* number of characters you want the formatted value to have
	- If not otherwise specified, pads the value with space characters
</div>
<div class="only-fragment fragment current" data-fragment-index=5>
- Sign?
	- If the sign of the number should be specified
	- A `+` sign ensures all numbers will have either a `+` or `-` sign in front
	- A space just adds a space before positive numbers (negatives would have a `-` sign in front)
</div>
<div class="only-fragment fragment current" data-fragment-index=6>
- Fill and Align
	- How you want the text aligned if it is shorter than the minium width
		- Can be `<`, `>`, or `^` for left, right, or center justified
	- Any fill characters you want to fill the empty space come before
		- Default is space
</div>

## Review Question! {data-notes="The 32//8 option"}
Which of the provided formatted string options below would evaluate to appear as:

<center>
`**101,234.98 & 4000`
</center>

when printed?

:::{.poll}
#. `f"{101234.984:*<12,.2f} & {3200//8:1<4d}"`
#. `f"{101234.984:*>12,.2f} & {32000//8:1>3d}"`
#. `f"{101234.984:*<12,f} & {320//8:1>4d}"`
#. `f"{101234.984:*<12,.2f} & {32//8:1<4d}"`
:::

## Learning English
- When working with sequences of characters, it is often useful or desirable to determine if they form actual valid English words
- This class provides for you a new library, through the file `english.py`
- The `english` library provides two objects you can import into your programs:
	- The constant `ENGLISH_WORDS`, which is a list of all the valid words in the English dictionary
	- The function `is_english_word()`, which accepts a single string as an argument and returns `True` if the string represents a valid English word.
- This library will be particularly useful for Wordle!


## Example: How many 2 letter words?
- Before we start writing code, let's pause. Give a physical English dictionary, how could you go about figuring out the number of two letter words?

::::::cols
::::{.col .fragment}
:::{.block name="Check valid words for right length"}
```{.python style='width: 100%' .fragment}
from english import ENGLISH_WORDS

count = 0
for word in ENGLISH_WORDS:
	if len(word) == 2:
		count += 1
print(count)
```
:::
::::

::::{.col style='flex-grow:1.15' .fragment}
:::{.block name="Check all two letter combinations"}
```{.python style='width:100%' .fragment}
from english import is_english_word

count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter1 in alphabet:
	for letter2 in alphabet:
		word = letter1 + letter2
		if is_english_word(word):
			count += 1
print(count)
```
:::
::::
::::::

## Introduction to Wordle
::::::cols
::::col
- Our first project will be Wordle
- Milestone guide will be posted tomorrow
- Not due until October 3rd
::::

::::col
![The game of Wordle](../images/wordle.png)
::::
::::::

## Your Responsibilities
- We will provide you with a custom data type that will handle all the graphics and user interaction
	- Don't worry, you'll have a chance to implement your own GUIs later in the semester!
- Your responsibilities will include:
	- Displaying and reading letters from boxes
	- Evaluating whether a word is valid
	- Determining what color each letter of a word should be
	- Determining when victory or defeat occurs


## Your Toolbox
- Special functions provided by the provided graphics data type: `WordleGWindow`
	- These will be well documented, and include, but are not limited to, things like
		- Getting or setting a letter in a particular box
		- Getting or changing the color of a given box
		- Changing which row is used when characters are entered
- Variables and functions
- Control statements
	- Good use of loops and if statements will be very useful
- Basic string functions

## Receiver Syntax
:::{style='font-size:.9em'}
- So far, all operations between or on objects have used symbols to indicate the operation
	- The `+` sign, for instance
- Going forward, we will begin to see more examples of operations on objects that use _receiver syntax_
- In receiver syntax, we specify the object to act on, followed by a dot and then a predefined function (called a _method_ here) name

  ```python
  obj.method_name()
  ```
  - This is like you are running this special function on the object, so you **need** the `()` at the end
  - Some methods also allow arguments, to influence exactly how the operation will proceed
:::

## An Approach to Success
- Each project is accompanied by a highly detailed guide: **read it!**
	- Explains background ideas so that you can understand the big picture of what you are needing to do
	- Also included a breakdown of individual _milestones_
		- A _milestone_ is a discrete checkpoint that you should ensure is working (and that you understand!) before moving on
- Projects are all about managing complexity. If you start trying to implement milestones out of order, you are asking for disaster
- Don't let yourself get overwhelmed by scale. Focus on one particular milestone at a time, which should involve focusing only on a small part of your overall code

<!--
## The Worth of a Picture
:::{style='font-size:.9em'}
- There comes a time when reading and entering text on a terminal doesn't cut it
	- Maybe you need more complicated input
	- Maybe you need a more complicated interface that pure text can manage
	- Maybe you have output that can not be shown as text
- Standard Python really only deals with the terminal interface
- Lots of outside libraries give Python more visual input/output
	- Turtle
	- Matplotlib
	- Tkinter <span class='fragment'>← PGL</span>
	- PyGame
	- Arcade
:::

## The Portable Graphics Library
- Built atop Tkinter
- The library (`pgl.py`) is available to you throught the project templete 
	- Put it in the same folder as your code, and then you can import it
- Operates on the idea of a collage or cork-board

![Test](../images/CorkBoard.svg)

- Note that newer objects can obscure older objects. This layering arrangement is called the _stacking order_.


## The Pieces
- At its simplest then, we have two main parts:
	- The window (or felt-board/cork-board)
		- Created with the `GWindow` function
		- Takes two arguments: a width and a height in pixels
	- The contents
		- A wide assortment of shapes that can be added to the scene
		- Control over where they are placed, how large they are, what color they are, etc


## Blue Rectangle!
```{.python data-line-numbers="1|3,4|6|7|8|9|10|11"}
from pgl import GWindow, GRect

GW_WIDTH = 500
GW_HEIGHT = 200

gw = GWindow(GW_WIDTH, GW_HEIGHT)
rect = GRect(150, 50 ,200, 100)
rect.set_color("Blue")
rect.set_filled(True)
gw.add(rect)
```

## The Coordinate System
![PGL Coordinates](../images/pgl_coordinates.svg)

- Positions and distances on the screen are measured in terms of pixels
- The location of the origin and orientation of the y-axis are **different from math**!
	- Origin is in the upper left instead of lower left
	- Y-values increase as you move downwards

## Other Simple Objects
Functions to create simple geometric objects:
<br>

- Rectangles!
	- `GRect( x, y, width, height )`
	- Creates a rectangle whose upper left corner is at (x,y) of the specified size
- Circles/Ovals!
	- `GOval( x, y, width, height )`
	- Creates an oval that fits inside the rectangle with the same dimensions
- Lines!
	- `GLine( x1, y1, x2, y2 )`
	- Creates a line extending from (x1,y1) to (x2,y2)


## The `GObject` Hierarchy
- The types of graphical objects form a hierarchy:

![](../images/GObject_Hierarchy.svg)

- The `GObject` type represents the collection of all graphical objects
- The `GFillableObject` type represents those that have a fillable interior


## Interacting with the `GWindow`
- We've already shown creation:

  ```python
  gw = GWindow(width, height)
  ```
- You have several more operations that you can apply to the `GWindow` object:

-------------------------------------- -------------------------------------
       `gw.add(object)`{.no-highlight} Adds an object to the window
 `gw.add(object, x, y)`{.no-highlight} Adds an object to the window after moving it to (x,y)
    `gw.remove(object)`{.no-highlight} Removes an object from the window
       `gw.get_width()`{.no-highlight} Returns the width of the graphics window in pixels
      `gw.get_height()`{.no-highlight} Returns the height of the graphics window in pixels
-------------------------------------- -------------------------------------


## Interacting with `GObject`s
- The following operations apply to all GObjects,  where `object`{.no-highlight} is the name of any specific instance.

---------------------------------------- ----------------------------
         `object.get_x()`{.no-highlight} Returns the x coordinate of this object
         `object.get_y()`{.no-highlight} Returns the y coordinate of this object
     `object.get_width()`{.no-highlight} Returns the width of this object
    `object.get_height()`{.no-highlight} Returns the height of this object
`object.set_color(color)`{.no-highlight} Sets the color of the object to the specified color
---------------------------------------- ----------------------------

- All coordinates and distances are measured in pixels


## Interacting with `GFillableObject`s
- Fillable GObjects have a smaller subset of commands that also apply to them.
- Initially the only fillable objects available to you are rectangles and ovals

--------------------------------------------- ----------------------------
     `object.set_filled(bool)`{.no-highlight} Sets the fill state of the object
`object.set_fill_color(color)`{.no-highlight} Sets the color to be used to fill the interior, otherwise same as the outer line
     `object.get_fill_color()`{.no-highlight} Gets the current color used to display the object interior
          `object.is_filled()`{.no-highlight} Returns True or False depending on whether the object is currently filled
--------------------------------------------- ----------------------------

-->
