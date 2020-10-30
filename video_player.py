#!/usr/bin/env python3

import cv2
from threading import Thread, Semaphore, Lock
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

semaphore = Semaphore(2)
qlock = Lock()
queue = []

def extract_frames(file_name, output_buffer, max_frames=9999):
    """
    docstring
    """
    pass

def convert_frames():
    """
    docstring
    """
    
def display_frames(parameter_list):
    """
    docstring
    """
    pass

if __name__ == "__main__":
    
