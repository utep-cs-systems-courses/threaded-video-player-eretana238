#!/usr/bin/env python3

import cv2
import threading
import numpy as np
import base64
from queue import Queue

class ExtractFrames(threading.Thread):
    def __init__(self, file_name, max_frames=9999):
        """Create thread."""
        threading.Thread.__init__(self)
        self.file_name = file_name
        self.vidcap = cv2.VideoCapture(self.file_name)
        self.max_frames = min(max_frames, int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
        self.count = 0

    def run(self):
        """Run thread."""
        success, image = self.vidcap.read()
        while success and self.count != self.max_frames:
            print(f'Extracting frame {self.count}')
            success, jpgImage = cv2.imencode('.jpg', image)
            jpgAsText = base64.b64encode(jpgImage)
            color_queue.enqueue(image)
            success,image = self.vidcap.read()
            self.count += 1
        print('Finished extracting all frames')

class ConvertFrames(threading.Thread):
    def __init__(self, max_frames):
        """Create thread."""
        threading.Thread.__init__(self)
        self.max_frames = max_frames
        self.count = 0

    def run(self):
        """Run thread."""
        while self.count != self.max_frames:
            if color_queue.size() != 0:
                print(f'Converting frame {self.count}')
                frame = color_queue.dequeue()
                grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray_queue.enqueue(grayscaleFrame)
                self.count += 1
        print('Finished converting frames')


class DisplayFrames(threading.Thread):
    def __init__(self, max_frames):
        """Create thread."""
        threading.Thread.__init__(self)
        self.count = 0
        self.max_frames = max_frames

    def run(self):
        """Run thread."""
        while self.count != self.max_frames:
            print(f'Displaying frame {self.count}')
            if gray_queue.size() != 0:
                grayscaleFrame = gray_queue.dequeue()
                cv2.imshow('Video', grayscaleFrame)
                if cv2.waitKey(42) and 0xFF == ord("q"):
                    break
                self.count += 1

        print('Finished displaying all frames')
        # cleanup the windows
        cv2.destroyAllWindows()


if __name__ == "__main__":
    clip = 'clip.mp4'

    color_queue = Queue()
    gray_queue = Queue()

    extract = ExtractFrames(clip, 72)
    convert = ConvertFrames(extract.max_frames)
    display = DisplayFrames(extract.max_frames)

    extract.start()
    convert.start()
    display.start()
