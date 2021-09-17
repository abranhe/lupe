"""The Lupe module."""

import sys

from lupe.core import lupe

__all__ = ['lupe']
__version__ = '0.2.0'

sys.modules[__name__] = lupe
