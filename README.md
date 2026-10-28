# Application Log Monitoring System

## Aim
Build a small Python application that generates structured log events, track its source code with Git/GitHub, and analyze the generated log file in Splunk Cloud.

## Tools
- Python 3
- Git
- GitHub
- Splunk Cloud
- VS Code (optional)

## Project structure
```text
Application-Log-Monitoring-System/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── logs/
    └── application.log   # generated when the app runs
```

## Run locally
```bash
python app.py
```
The application creates `logs/application.log` and writes 20 sample events. The log file is intentionally not ignored, so you can upload it to Splunk and optionally commit sample logs if desired. Avoid committing real secrets or sensitive production logs.

## Upload the log to Splunk Cloud
1. Sign in to your Splunk Cloud deployment.
2. Open **Settings / Add Data** (the labels can vary by deployment).
3. Choose **Upload** and select `logs/application.log`.
4. Review the source type and index settings, then submit.
5. Open Search and Reporting and set the time range to include the generated events.

## Example SPL searches
Replace `main` with the index you selected if it differs.

All events:
```spl
index=main
```

Count events by severity:
```spl
index=main
| stats count by log_level
```

Because this demo's log format places the severity as a plain token (for example, `INFO` or `ERROR`), if Splunk does not automatically extract `log_level`, use:
```spl
index=main
| rex "\s(?<log_level>INFO|WARNING|ERROR)\s"
| stats count by log_level
```

Show error events:
```spl
index=main "ERROR"
```

Trend events over time:
```spl
index=main
| timechart span=1m count
```

Note: Splunk field extraction and index names depend on your ingestion settings. If `index=main` returns no events, check the selected index and time range.

## Git and GitHub
Create an empty repository on GitHub, then run these commands in this project directory. Replace the placeholder with your own repository URL:
```bash
git init
git add .
git commit -m "Initial commit: log monitoring project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Application-Log-Monitoring-System.git
git push -u origin main
```

## Expected result
- A Python script generates INFO, WARNING, and ERROR log events.
- Git records project changes.
- GitHub hosts the source code.
- Splunk Cloud can search the uploaded log file and summarize events in a dashboard.

## Conclusion
This project demonstrates basic application logging, source-code version control, log ingestion, searching, and monitoring with Splunk Cloud.
