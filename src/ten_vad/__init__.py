"""
Voice Activity Detection (VAD) package from the TEN Framework.

This package provides Python bindings to the ten_vad C library.
For the C interface, see the header file in include/ten_vad.h.
"""

# Import the main class directly into the package namespace
from .wrapper import TenVad

# Define package metadata
__version__ = "1.0.1" 