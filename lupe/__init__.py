"""The Lupe module."""

import sys

from lupe.core import lupe

sys.modules[__name__] = lupe
