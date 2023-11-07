---
title: "Algorithms and Graphics!"
author: Jed Rembold
date: September 2, 2020
slideNumber: true
theme: "class_python"
highlightjs-theme: horizon-dark
width: 1920
height: 1200
transition: fade
hash: true
history: false

---


## Announcements
- Homework due Friday evening at midnight
	- Pdf on the main webpage.
	- Link in pdf to add repository, then download to edit on your own system!
	- Remember to edit the README to switch PENDING to DONE when you are done!
	- Problems 2 and 3 have some auto-testing to help you check your work
- CS Tea tommorrow at 11:30
	- Dept introduction tomorrow with info about programs, clubs, internships, and more
- Polling:
	- [rembold-class.ddns.net](http://rembold-class.ddns.net)

## Review Question
Which of the below blocks of code would print something different than the others?

::::: cols

:::: col
:::{.block name=A}
```python
for n in range(10):
	if n % 2 == 0:
		print(n)
```
:::
:::{.block name=B}
```python
for i in range(0,10,2):
	if i > 0:
		print(i)
```
:::
::::

:::: col
:::{.block name=C}
```python
for j in range(0,20,4):
	L = j // 2
	print(L)

```
:::
:::{.block name=D}
```python
for k in range(0,10):
	if not (k % 2) > 0:
		print(k)
```
:::
::::
:::::


## Nesting Loops
- Most anything can go in the repeating block of a loop, _including other loops_
- The inner most loop must finish **all** of its iterations before the outer loop finishes a **single** iteration
- Useful when you need to iterate over multiple different values
	- Example: generating multiplication tables

	```python
	for a in range(1,5):
		for b in range(1,5):
			print(a*b)
	```


## Algorithms
- A fundamental concept in computer science
- An _algorithm_ is a solution strategy that satisfies the following criteria:
	- It is _clear and unambiguous_, in the sense that it is easily understood
	- It is _effective_, in the sense that it is possible to carry out the steps
	- It is _finite_, in the sense that the strategy always reaches an end point
- The word algorithm comes from the name of the 9th-century Persian mathematician Muhammad ibn Mūsā al-Khwārizmī
- Al-Kwārizmī's most significant work was a treatise on mathematical methods entitled _Kitab al jabr w'al-muqabala_, which gave rise to the English word _algebra_
- Many instances of algorithmic procedures that are extremely old, dating back to early civilizations in the Middle East, India, and China


## Efficiency
- There can be many different algorithms for solving the same problem
- Many will vary widely in their efficiency, or how quickly and easily they will get you a solution
- May also vary in their complexity, or it how difficult they are to implement
- Commonly you will want to look for trade-offs between the two

<br><br>

:::{.block name=Example}
Let's look at the classical case of trying to find the greatest common divisor between two integers. That is, we want to find the largest number that evenly divides two numbers.
:::


## Brute Force
- One strategy is to just count backwards from the smaller value until you find a value that evenly divides both numbers
- The code could look something like:
```python
def gcd(x, y):
	g = min(x,y):
	while x % g != 0 or y % g != 0:
		g -= 1
	return g
```
- The algorithm will eventually terminate, since `g` would eventually hit 1 and 1 evenly divides everything
- Might take a while!
	- Take a million steps to figure out that the gcd between 1000000 and 1000005 is 5!


## Euclid's Algorithm
- Euclid had the great insight that the gcd of x and y must also be the gcd of y and the remainder of x divided by y
- Gives rise to an alternative algorithm:
```python
def gcd(x, y):
	r = x % y
	while r != 0:
		x = y
		y = r
		r = x % y
	return y
```
- This only takes **TWO** steps to find the gcd between 1000000 and 1000005!!


## Illustrating Euclid's Algorithm


## The Worth of a Picture
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


## The Portable Graphics Library
- Built atop Tkinter
- The library (`pgl.py`) is available on the website
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
```{.python data-line-numbers="1|3,4|7|8|9|10|11"}
from pgl import GWindow, GRect

GW_WIDTH = 500
GW_HEIGHT = 200

def blue_rectangle():
	gw = GWindow(GW_WIDTH, GW_HEIGHT)
	rect = GRect(150, 50 ,200, 100)
	rect.set_color("Blue")
	rect.set_filled(True)
	gw.add(rect)
```
<!--![Variable Tracker](../images/blue_rectangle.svg)-->

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
