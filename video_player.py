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
# full.release()

# get
# full.aquire()
# qlock.aquire()
# qlock.put()
# qlock.release()
# empty.release()

sem = threading.Semaphore(2)
qlock = threading.Lock()
queue = []

class ExtractFrames(threading.Thread):
    def __init__(self, file_name, output_buffer, max_frames=9999):
        """
        Create thread
        """
        threading.Thread.__init__(self)
        self.file_name = file_name
        self.output_buffer = output_buffer
        self.max_frames = max_frames
    
    def run(self):
        """
        Run thread
        """
        count = 0
        
        vidcap = cv2.VideoCapture(self.file_name)
        
        success, image = vidcap.read()
        
        while success and count < self.max_frames:
            success, jpgImage = cv2.imencode('.jpg', image)
        
            jpgAsText = base64.b64encode(jpgImage)
            
            sem.acquire()
        
            self.output_buffer.put(image)
        
            sem.release()
        
            success,image = vidcap.read()

if __name__ == "__main__":

