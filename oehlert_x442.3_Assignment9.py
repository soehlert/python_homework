#!/usr/bin/env python3

import os
import urllib.request
import re

############
# Q1
############


def zero_length(directory):
    """ Using os.walk, write a script that will print the filenames of zero
    length files. It should also print the count of zero length files. """

    os.chdir(directory)

    zero_length_files = 0
    for dirname, subdirname, fn in os.walk(directory):
        for f in fn:
            if os.path.getsize(f) == 0:
                zero_length_files += 1
                print(os.path.abspath(f))
    print("number of zero length files: {}".format(zero_length_files))


zero_length("/tmp/zero")


############
# Q2
############


def html_images(url):
    """ List and count all of the images in a given HTML web page/file.
    You can assume that:
    Each image file is enclosed with the tag <img and ends with >
    The HTML page/file is syntactically correct """

    images = 0

    with urllib.request.urlopen(url) as response:
        html = response.read()
        image_list = re.findall(r"<img.*?>", str(html))

        for i in image_list:
            print(i)
            if i:
                print(i)
                images += 1

        print(images)


html_images("https://www.cnn.com/")
