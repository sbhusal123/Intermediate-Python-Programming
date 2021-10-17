# Handlers

-   Responsible for dispatching the log message.
-   Through http requests, emails, files, ...

## Basic Template

-   **Define a logger:** `logger=logging.getLogger(<logger_name>)`
-   **Define a handler:** `foo_handler=FooHandler()`
-   **Set log level for handler:** `foo_handler.setLevel(logging.<LEVEL>)`
-   **Define formatter for a handler:** `foo_formatter=logging.formatter(<format>)`
-   **Set formatter for handler:** `foo_handler.Formatter(foo_formatter)`
-   **Add Handler for logger:** `logger.addHandler(foo_handler)`

```python
import logging

# define a loger
logger = logging.getLogger(__name__)

# define handler
stream_handler = logging.StreamHandler()

# set loglevel for handler
stream_handler.setLevel(logging.WARNING) # logs messages above and equal WARN level

# define formatters for those handlers
stream_formatter = logging.Formatter("%(asctime)s--%(name)s--%(levelname)s--%(message)s")

# setting formatters
stream_handler.setFormatter(stream_formatter)

# add handler to the logger
logger.addHandler(stream_handler)

logger.warn("This is a warning")
```

[Inbuilt Handlers](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers)
