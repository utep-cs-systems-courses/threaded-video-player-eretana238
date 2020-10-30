#!/usr/bin/env python3

import cv2
import threading
import numpy as np
import base64

# put
# empty.aquire()
# qlock.put()
# qlock.aquire()
# qlock.release()
# full.release

# get
# full.aquire()
# qlock.aquire()
# qlock.put()
# qlock.release()
# empty.release()

class Extract(Thread):
    def __init__(self):
        pass

class Convert(Thread):
    def __init__(self):
        pass

class Display(Thread):
    def __init__(self):
        pass
