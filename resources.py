# resources.py
# Helper to find assets in both development and bundled exe

import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running in development
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def asset_path(filename):
    """Shortcut for getting asset paths"""
    return resource_path(os.path.join("assets", filename))