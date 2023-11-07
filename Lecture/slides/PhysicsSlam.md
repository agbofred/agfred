---
title: "Searching the Cosmos with Neural Networks"
author: Jed Rembold
date: November 18, 2021
slideNumber: false
theme: solarized
highlightjs-theme: solarized
width: 1920
height: 1080
transition: fade
hash: true
autoPlayMedia: true
---


## Motivation
::::::cols
::::col
- The amount of data that telescopes produce is growing...astronomically
	- LSST to collect 20 TB _per night_ starting in 2022
	- Square Kilometre Array will generate 2 PB daily starting in 2028
- One of the largest sky surveys currently, SDSS, has collected 40 TB over **the past 20 years**
- New systems and methods are necessary to process and keep up
::::

::::col
![The 3.2 GPixel LSST Camera](../images/Slam/LSST.webp)

::::
::::::



## Gravitational Lenses
![](../images/Slam/Lensing.mp4){height=800 loop=True}

## Gravitational Lenses
![](../images/Slam/Lensing2.mp4){height=800 loop=True}

## Convolutions
<div class="fig-container" data-file="../images/d3/Convolution_Blur.html" data-scroll="no", data-style="width:100%; display:inline;"></div>

## Feature Extraction
- Different kernels can highlight different features in an image

<div class="fig-container" data-file="../images/d3/Convolution_Sobel.html" data-scroll="no", data-style="width:100%; display:inline;"></div>

## Convolutional Neural Networks
- The networks "learns" the best kernel weights
- Generally use many kernels and combinations of kernels

<br><br>

![](../images/Slam/CNN.svg)

## Challenges
- Choosing the convolution model
	- How many kernels to use each step of the way?
	- What size should they be?
	- How do decide when to pool or stride?
	- **Lots of practice to get a feel for what seems to work well and what does not.**
- Acquiring and reading in training data
	- Need labeled data for a supervised algorithm like this
	- Often times large datasets, so can only read in a bit at a time
	- **Practice working, cleaning, and streaming in large datasets**
- Dealing with poor fitting or overfitting
	- **Practice looking at different analytics to determine how your model is performing**


## Interested in More?
- Talk to me!
	- My office is Collins 311
	- Email: jjrembold@willamette.edu
