---
title: "Reading and Writing"
author: Jed Rembold
date: November 7, 2022
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
- Problem Set 6 posted!
	- The last problem set!
	- I was late getting it posted, so I've given you an extra day as well
- Grade report progress: I'm close!!
- Polling: [rembold-class.ddns.net](http://rembold-class.ddns.net)

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


## Reading
- Programs often need to work with collections of data that are too large to reasonably exist typed all out in the code
	- Easier to read in the values of a list from some external data file
- A _file_ is the generic name for any named collection of data maintained on some permanent storage media attached to a computer
- Files can contain information of many different types and encodings
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

## Reading Text Files
- The general approach for reading a text file is to first _open_ the file and associate that file with a variable, commonly called its _file handle_
- We will also use the _with_ keyword to ensure that Python cleans up after itself (closes the file) when we are done with it (Many of us could use a `with` irl)
  ```python
  with open(filename) as file_handle:
  	# Code to read the file using the file_handle
  ```
- Python gives you several different ways to actually read in the data
	- `read` reads the entire file in as a string
	- `readline` or `readlines` reads a single line or lines from the file
	- `read` alongside `splitlines` gets you a list of line strings
	- Can use the file handle as an iterator to loop over

## Entire file ⟶  String
- The `read` method reads the entire file into a string, with includes newline characters (`\n`) to mark the end of lines
- Simple, but can be cumbersome to work with the newline characters, and, for large files, it can take a large amount of memory

As an example, the file:<br><br>

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

## Example: Name Mangling
- Let's look at an example with some more meat to it
- I have a text file with all your first names. I'd like to:
	- Read in the names
	- Select two at random
	- Combine the first half of one name with the second half of the other
	- Print out both potential hybrid names
- We'll practice breaking a problem into steps along the way here


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

<!--
- Using it thus looks something like:
```python
filename = choose_input_file()
with open(filename) as f:
	# Code to read file
```
-->


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
	$$ A \sin\left(\frac{2\pi}{T}x\right)$$
  where $A$ is the amplitude of the wave and $T$ the period of the wave, or how quickly it repeats
- How can we put this together?
