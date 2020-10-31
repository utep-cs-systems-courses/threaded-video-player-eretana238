#!/usr/bin/env python3

import cv2
import threading
import numpy as np
import base64
import sys

class ExtractFrames(threading.Thread):
    def __init__(self, file_name, max_frames=9999):
        """
        Create thread
        """
        threading.Thread.__init__(self)
        self.file_name = file_name
        self.max_frames = min(video_frames, max_frames)
        self.count = 0
    
    def run(self):
        """
        Run thread
        """
        vidcap = cv2.VideoCapture(self.file_name)
        # check length
        video_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        success, image = vidcap.read()
        while success and self.count < self.max_frames:
            success, jpgImage = cv2.imencode('.jpg', image)
            jpgAsText = base64.b64encode(jpgImage)
            # semaphore usage
            empty.acquire()
            with qlock:
                queue.append(image)
                print(f'Extrating frame {self.count}')
            full.release()
            success,image = vidcap.read()
            self.count += 1

class DisplayFrames(threading.Thread):
    def __init__(self):
        """
        Create thread
        """
        threading.Thread.__init__(self)
        self.count = 0
        self.video_frames = video_frames

    def run(self):
        """
        Run thread
        """
        while True:
            if len(queue) != 0:
                # semaphore usage
                full.acquire()
                with qlock:
                    frame = queue.pop(0)
                    print(f'Displaying frame {self.count}')
                empty.release()
                grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('Video', grayscaleFrame)
                if cv2.waitKey(42) and 0xFF == ord("q"):
                    break
                self.count += 1
            if self.count == self.video_frames:
                break
        print('Finished displaying all frames')
        # cleanup the windows
        cv2.destroyAllWindows()


if __name__ == "__main__":
    clip = 'clip.mp4'
    full = threading.Semaphore(20)
    empty = threading.Semaphore(4)
    qlock = threading.Lock()

    video_frames = 100

    queue = []

    extract = ExtractFrames(clip)
    display = DisplayFrames()

    extract.start()
    display.start()
