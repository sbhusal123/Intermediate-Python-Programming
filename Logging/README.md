# Logging:

## Log Levels in Order:

-   Debug
-   Info
-   Warning
-   Error
-   Critical

> By default only the levels below info is displayed.

## Setting a Log level

```python
logging.basicConfig(level=logging.<LEVEL_IN_UCASE> format="<format_of_log_message>", datefmt='<date_time_format>')

```

**i. level**

-   Level from which to show the log messages for.
-   logging.DEBUG
-   logging.INFO
-   logging.WARNING
-   logging.ERROR
-   logging.CRITICAL

**ii. format**

-   Format of output message.
-   Example: `"%(asctime)s--%(name)s--%(levelname)s--%(message)s"`
-   **asctime** Time
-   **name** Name of logger.
-   **levelname** Log level
-   **message** log message
-   These attributes are called LogRecordAttributes.
-   Other formatter attributes can be accessed from [here](https://docs.python.org/3/library/logging.html#logrecord-attributes)

**iii. datefmt**

-   Date time format
-   [Explore Here..](https://www.w3schools.com/python/python_datetime.asp)

![Logging Flow](https://docs.python.org/3/_images/logging_flow.png)
