# RotatingFileHandler

-   Rotates / Creates new log file once the specified size of file is reached.
-   **Usage:** `RotatingFileHandler(<file_path>, maxBytes=<int>, backupCount=<int>)`

**Example**

```python
handler = RotatingFileHandler('logs/app.log', maxBytes=2000, backupCount=2)
```

-   Log location: logs/app.log
-   Max bytes of each file: 2000bytes
-   Backup Count: 10 i.e. `app.log app.log.1`
-   Once these files are fully occupied, logs are cleared and recreated.
