"""
Lupe: The CLI helper you need

lupe(help_message, options?)

Example:

```python
import lupe

cli = lupe('usage: foo [options]')

# display help
cli.get_help()
```

Read the documentation at https://github.com/abranhe/lupe
"""

import sys

from lupe.core import Lupe

__version__ = '0.1.12'

sys.modules[__name__] = Lupe
