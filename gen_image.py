#!/usr/bin/env python3

import glob
import os

g = glob.glob("images/*")
images = list(g)

image_name = ''

while (not image_name in images):
    server_name = input("What's the name of the server? ")
    image_name = 'images/%s.jpg' % server_name

print(image_name)

# copy file to etc
#os.system("sudo cp %s /etc/%s.jpg" % (image_name, server_name))
with open("01-motd", 'wb') as f:
    code = """#!/bin/bash
tiv /etc/%s.jpg -w 50 -h 33
    """ % server_name
    f.write(bytes(code, 'utf-8'))
