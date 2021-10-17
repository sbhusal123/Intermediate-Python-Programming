# Creating a module wise logger

**helper.py**

```python
import logging

logger = logging.getLogger(__name__) # where __name__ = name of module
logger.debug("This is debug message.")
```

-   Here we created a custom logger with name same as that of name of module.
-   By default only the log >=Warning is shown.

**main.py**

```python
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s--%(name)s--%(levelname)s--%(message)s",
                    datefmt='%m/%d/%Y %H:%M:%S')

import helper # note that the import should be after declaration of logger

""" Output due to propagation to helper module.
10/17/2021 11:09:07--helper--INFO--This is info message
"""
```

-   Here we imported helper, also a logger.
-   Logger from helper gets added to the hierarchy. Thus the log is propagated to the base logger.

## Disabling log propagation

-   `<logger>.propagate = False`

**helper.py**

```python
import logging

logger = logging.getLogger(__name__)

logger.propagate = False  # disable propagation

logger.debug("This is debug message.")
```

-   This stops keepng log records from hepler module.
