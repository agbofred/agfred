---
title: "Reading and Writing"
author: Jed Rembold & Fred Agbo
date: October 27, 2023
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
- Problem Sets 5 is due _next_ week Tuesday at 12 noon
- Grading of project 1 to be published soon.
- Project 3 will be posted early next week. You will be notified when uploaded
- CS151 Graphics Contest is due on ***31st October***
- We will return to Ford Hall 102 from Monday next week
- Polling continues today! Use this link [https://www.polleverywhere.com/agbofred203](https://www.polleverywhere.com/agbofred203)


<!--
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
```{.python style='max-height:900px; font-size:.8em; line-height:1.3em;'}
class Demo:
	def __init__(self):
		self.x = []

	def add(self, v):
		self.x.append(v)

	def get_x(self):
		return self.x

A, B = Demo(), Demo()
A.add(3)
B.add(3)
C = B.get_x()
C.append(A)
print(A.get_x() == B.get_x())
```

::::
::::::
-->

## Review! {data-notes="Solution: [2,3,4,5]"}
Suppose I construct the below 2D array using list comprehension:

`A = [[i+j for i in range(3)] for j in range(4)]`{.inlinecode .python}

What would be the output of:

`print([A[i][2] for i in range(len(A))])`{.inlinecode .python}

<br>

:::{.poll}
#. `[0,1,2]`
#. `[2,3,4]`
#. `[2,3,4,5]`
#. `[2,2,2,2]`
:::

## Tabulating with list

- Arrays can also be useful when you have a set of values and you need to count how many values fall into a different ranges
  - Process is called _tabulation_
- The idea is that for each data file we encounter, we figure out a corresponding index in our tabular array and then increment the value of that element
- Your book shows this for seeing how many times each letter of the alphabet appears in a text sequence


## Tabulating with list example

- Below program is an example of determining how many students got different letters grades on a final


```{.python style='min-height:850px; width=100%;'}
import random
mark = [random.randint(50,100) for i in range(27) ]
count = [0 for i in range(5)]
for i in range(len(mark)):
    if mark[i] >= 90:
        count[0] +=1
    elif mark[i] >= 80:
        count[1] +=1
    elif mark[i] >= 70:
        count[2] +=1
    elif mark[i] >= 60:
        count[3] +=1
    else:
        count[4] +=1
print(mark)
print(count)

```
- List generated contains random values, it changes every time it executes

## Breaking out the Pixel Colors
- You do not need to convert the pixel values yourself! PGL has built-in ways to extract the various colors

:::{style="font-size:.8em;"}

Function | Description
--- | -----
`GImage.get_red(pixel)` | Returns the integer (0-255) corresponding to the red portion of the pixel
`GImage.get_green(pixel)` | Returns the integer (0-255) corresponding to the green portion of the pixel
`GImage.get_blue(pixel)` | Returns the integer (0-255) corresponding to the blue portion of the pixel
`GImage.get_alpha(pixel)` | Returns the integer (0-255) corresponding to the alpha portion of the pixel
`GImage.create_rgb_pixel(r,g,b)` | Returns a 32-bit integer corresponding to the desired color

:::


## Image Thresholding
::::::cols
::::col
- As an example of reading and manipulating pixel values, lets look at how we could threshold the image to the right
- Thresholding is when you take a grayscale image and convert it to a black and white image, where a pixel is set to be white if it is above a certain threshold in brightness
- Grayscale, so each RGB component is the same
Let’s threshold at a value of 30
::::

::::col
![Blurry Moon by Jed](../../Class_Demos/Moon.png){width=80%}
::::
::::::


## Image Thresholding Example 


```{.python style='min-height:980px; width=100%;'}

from pgl import GWindow, GOval, GImage

gw =GWindow(600,400)
image = GImage("Moon.png", 0,0)
image.scale(gw.get_width()/image.get_width())
gw.add(image)

def imagetreshold(e):
    TRESHOLD = 130
    pixel = image.get_pixel_array()
    #print(pixel)
    for r in range(len(pixel)):
        for c in range(len(pixel[0])):
            value = pixel[r][c]
            red =GImage.get_red(value)
            if red< TRESHOLD:
                pixel[r][c]= GImage.create_rgb_pixel(0,0,0)
            else:
                pixel[r][c] = GImage.create_rgb_pixel(255,255,255)
    # You must create a new Gimage
    new_image = GImage(pixel)
    gw.add(new_image)
gw.add_event_listener("click", imagetreshold)

```

<!--
## Reading
- Programs often need to work with collections of data that are too large to reasonably exist typed all out in the code
	- Easier to read in the values of a list from some external data file
- A _file_ is the generic name for any named collection of data maintained on some permanent storage media attached to a computer
- Files can contain information encoded in many different ways
	- Most common is the _text file_
	- Contains character data like you'd find in a string


## Strings vs Text Files
- While strings and text files both store characters, there are some important differences:
	- **The longevity of the data stored**
		- The value of a string variable lasts only as long as the string exists, is not overridden, or is not thrown out when a function completes
		- Information in a text file exists until the file is deleted
	- **How data is read in**
		- You have access to all the characters in a string variable pretty much immediately
		- Data from text files is generally read in sequentially, starting from the beginning and proceeding until the end of the file is reached
-->
## Reading Text Files
- The general approach for reading a text file is to first _open_ the file and associate that file with a variable, commonly called its _file handle_
- We will also use the _with_ keyword to ensure that Python cleans up after itself (closes the file) when we are done with it (Many of us could use a `with` irl)
  ```python
  with open(filename) as file_handle:
  	# Code to read the file using the file_handle
  ```
- Python gives you several ways to actually read in the data
	- `read` reads the entire file in as a string
	- `readline` or `readlines` reads a single line or lines from the file
	- `read` alongside `splitlines` gets you a list of line strings
	- Can use the file handle as an iterator to loop over

## Entire file ⟶ String
- The `read` method reads the entire file into a string, with includes newline characters (`\n`) to mark the end of lines
- Simple, but can be cumbersome to work with the newline characters, and, for large files, it can take a large amount of memory

- As an example, the file:<br><br>

  :::{.block name="Seuss.txt" style='width:40%; margin-left: auto; margin-right: auto;'}
	One fish<br>
	two fish<br>
	red fish<br>
	blue fish
  :::

  would get read as

`"One fish\ntwo fish\nred fish\nblue fish"`{style="display: block; margin: auto; text-align: center;"}

## Line by Line
- Of the ways to read the file in a string at a time, using the file handler as an iterator and looping is probably best and certainly most flexible
- Leads to code that looks like:
  ```python
  with open(filename) as f:
	  for line in f:
		  # Do something with the line
  ```
- Note that **most** strategies preserve the newline character, which you very likely do not want, so be ready to strip them out before doing more processing


## Powers Combined
- So long as your files are not gigantic, using `read` and then the `splitlines` method can be a good option
- This **does** remove the newline characters, since it splits the string at them
  ```python
  with open(filename) as f:
	  lines = f.read().splitlines()
  # Then you can do whatever you want with the list of lines
  ```
  
## Aren't you Exceptional
- When opening a file for reading, it is possible the file does not exist!
	- Python handles this (and many other potential errors that can arise) using a mechanism called _exception handling_
	- Common in other languages as well
- An _exception_ is a object that belongs to an overarching hierarchy of exception classes
	- Different classes/types for different purposes
	- File operations, for example, use the exception class `IOError`
- If `open` encounters an error, it reports the error by _raising an exception_ with `IOError` as its type.
	- Raising an exception generally immediately terminates your program, but sometimes that is undesirable


## Ignore Yoda, there is a `try`
- Python uses the `try` statement to indicate an interest in trying to handle a possible exception
- In simplest form, the syntax is:
  ```python
  try:
  	  # Code that may cause an exception
  except type_of_exception:
  	  # Code to handle that type of exception
  ```
- `type_of_exception` here is the class name of the exception being handled
	- `IOError` for the file reading errors we are discussing
- Any exceptions arising from within the `try` block or within functions *called* within the try block would be "caught" and the lower block of code run instead of terminating the program

## Example: Requesting Existing File
- As an example, the below function will repeatedly ask the user to supply a file name that actually exists. 
- It will not just immediately break should they give it an invalid filename!
  ```python
  def get_existing_file(prompt="Input a filename: "):
	  while True:
		  filename = input(prompt)
  		  try:
  			  with open(filename):
  				  return filename
  		  except IOError:
  			  print("That filename is invalid!")
  ```
- If the `open` call succeeds, we immediately just return the filename, but if it fails due to a `IOError`, we display a message and then keep asking



## Choosing Wisely
- The Python package used to implement `pgl.py` also supports a mechanism to choose files interactively, made available through the `filechooser.py` library module.
- `filechooser.py` exports two functions:
	- `choose_input_file` for selecting a file
	- `choose_output_file` for selecting a folder and filename to save a file to
- Both open up a file dialog that lets you select/choose a file
	- Clicking Open or Save returns the full pathname of the file
	- Clicking Cancel returns an empty string

- Using it thus looks something like:
```python
filename = choose_input_file()
with open(filename) as f:
	# Code to read file
```


## Writing Text Files
- You can write text files using almost the same syntax as reading:
  ```python
  with open(filename, mode) as file_handle:
  	  # Code to write the file using file_handle
  ```
- Note the `mode` parameter to `open` here! Mode is a string which is either
	- `"w"` to **write** a new file (or overwrite an existing file)
	- `"a"` to **append** new contents to the end of an existing file
- The file handler supports the methods:
	- `.write(some_string)` to write a string to the file
	- `.writelines(iterable_of_strings)` to write each iterable element to the file


## Writing ASCII SINE
- Suppose I wanted to try my hand at some ASCII art and fill a text file with a vertical oscillating sine wave
- A sine wave generally looks like:
	$$ A + A \sin\left(\frac{2\pi}{T}x\right)$$
  where $A$ is the amplitude of the wave and $T$ the period of the wave, or how quickly it repeats
  - The extra $A +$ out front is to push the wave over to the right, since we can't really place negative characters
- How can we put this together?


## ASCII SINE Code
```{.python style='font-size:.6em; max-height:900px;'}

from math import sin, pi

def sine_file(filename, A, T, symbol, padding=" "):
    """ 
    Creates a new sine wave in the provided file with the provided amplitude (A),
    and period (T) with the indicated symbol at the end.

    Inputs:
        filename (string): the name of the file to write the art to
        A (int): the amplitude of the wave in terms of number of characters
        T (int): the period of the wave in terms of number of lines
        symbol (string): the symbol to place to mark the wave
        padding (string): what character to pad the left side of the wave with

    Outputs:
        None
    """

    def compute_symb_placement(A, T, x):
		"""Computes where the symbol should be placed."""
        value = A * sin(2 * pi / T * x) + A
        return int(value) # to integer character placement

    def construct_line(placement, symbol, padding):
		"""Constructs the line with the necessary padding and symbol at the end."""
        return padding * placement + symbol

    with open(filename, 'w') as fh:
        for x in range(10 * T): # write 10 periods worth of lines
            v = compute_symb_placement(A, T, x)
            line = construct_line(v, symbol, padding)
            fh.write(line + '\n') # need the newline character at the end!

if __name__ == '__main__':
    sine_file('sine_test.txt', A=30, T=50, symbol='X')
```
