#!/usr/bin/env python3

import cv2
import threading
import numpy as np
import base64

# put
# empty.aquire()
# qlock.aquire()
# qlock.put()
# qlock.release()
# full.release()

# get
# full.aquire()
# qlock.aquire()
# qlock.put()
# qlock.release()
# empty.release()

class ExtractFrames(threading.Thread):
    def __init__(self, file_name, max_frames=9999):
        """
        Create thread
        """
        threading.Thread.__init__(self)
        self.file_name = file_name
        self.max_frames = max_frames
        self.count = 0
    
    def run(self):
        """
        Run thread
        """
        vidcap = cv2.VideoCapture(self.file_name)
        success, image = vidcap.read()
        while success and self.count < self.max_frames:
            success, jpgImage = cv2.imencode('.jpg', image)
            jpgAsText = base64.b64encode(jpgImage)
            # semaphore usage
            empty.acquire()
            qlock.acquire()
            queue.append(image)
            print(f'Extrating frame {self.count}')
            qlock.release()
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

    def run(self):
        """
        Run thread
        """
        while True:
            if len(queue) != 0:
                # semaphore usage
                full.acquire()
                qlock.acquire()
                frame = queue.pop(0)
                print(f'Displaying frame {self.count}')
                qlock.release()
                empty.release()
                cv2.imshow('Video', frame)
                if cv2.waitKey(42) and 0xFF == ord("q"):
                    break
                self.count += 1

        print('Finished displaying all frames')
        # cleanup the windows
        cv2.destroyAllWindows()


if __name__ == "__main__":
    clip = 'clip.mp4'
    full = threading.Semaphore(20)
    empty = threading.Semaphore(4)
    qlock = threading.Lock()
    queue = []
    extract = ExtractFrames(clip, 72)
    display = DisplayFrames()

    extract.start()
    display.start()
