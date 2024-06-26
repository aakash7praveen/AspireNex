import tkinter as tk
from tkinter import ttk
from imutils import face_utils
import playsound
import imutils
import dlib
import cv2
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt
import sys
import urllib
import urllib.request
import time

class DrowsinessDetectionInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Drowsiness Detection System")
        
        # Elements on the interface
        self.status_label = ttk.Label(root, text="System Status: Ready", font=("Helvetica", 14))
        self.calibration_button = ttk.Button(root, text="Calibrate", command=self.calibrate)
        self.start_button = ttk.Button(root, text="Start Detection", command=self.start_detection)
        self.notification_label = ttk.Label(root, text="Notification Preferences:")
        self.notification_options = ttk.Combobox(root, values=["Visual", "Auditory", "Haptic"])
        self.notification_options.set("Visual")
        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        
        # Layout
        self.status_label.pack(pady=10)
        self.calibration_button.pack(pady=10)
        self.start_button.pack(pady=10)
        self.notification_label.pack(pady=5)
        self.notification_options.pack(pady=5)
        self.exit_button.pack(pady=10)

    def calibrate(self):
        # Add calibration logic here
        self.status_label.config(text="System Status: Calibrated")

    def start_detection(self):
        # Add logic to start the detection system here
        selected_notification = self.notification_options.get()
        self.status_label.config(text=f"System Status: Detection Started\nNotification: {selected_notification}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrowsinessDetectionInterface(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk

def start_detection():
    driver_name = driver_name_entry.get()
    def sound_alarm(path):
	    playsound.playsound(path)

    def eye_aspect_ratio(eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear
	
    
    print(f"Starting detection for driver: {driver_name}")



# Create and configure the main frame
frame = tk.Frame(root, padx=50, pady=50)
frame.pack()

# Create and add elements to the frame
label = tk.Label(frame, text="Drowsiness Detection", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=2, pady=10)

driver_name_label = tk.Label(frame, text="Driver's Name:")
driver_name_label.grid(row=1, column=0, pady=5, sticky=tk.E)

driver_name_entry = tk.Entry(frame)
driver_name_entry.grid(row=1, column=1, pady=5)

start_button = tk.Button(frame, text="Start Detection", command=start_detection)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrowsinessDetectionInterface(root)
    root.mainloop()