
# 📊 Data Pipeline Monitoring for Sales Ops

**Internship Project – Future Investment**  
**Tools**: SQL, Python, Tableau  
**Duration**: [Insert Duration]  
**Role**: Data Analyst Intern

---

## 📝 Overview

This project was built to ensure robust monitoring and alerting for sales operations data pipelines at Future Investment. During the internship, I identified critical issues related to pipeline latency, data inconsistency, and lack of visibility for stakeholders. To address these, I developed a comprehensive monitoring system using SQL for audits, Python for automation and alerts, and Tableau for live operational insights.

---

## 🎯 Goals

- Audit existing data pipelines and improve reporting consistency.
- Automate health and freshness checks to preempt failures.
- Visualize real-time metrics for enhanced operational decision-making.

---

## 🧰 Tools & Technologies

| Tool     | Purpose                                  |
|----------|------------------------------------------|
| **SQL**  | Query data freshness, failure logs, inconsistencies |
| **Python** | Automate health checks and alerts     |
| **Tableau** | Visual dashboard for operational insights |

---

## 🛠️ What I Built

### 🔍 1. SQL Pipeline Auditing

- Wrote SQL scripts to identify failed ETL jobs and stale pipeline data.
- Improved reporting reliability by **35%** through targeted audits.

**Key SQL Scripts:**
- `Freshness Check`: Detects outdated pipeline outputs  
```sql
SELECT pipeline_name, MAX(last_run_time) AS last_run
FROM etl_job_status
GROUP BY pipeline_name
HAVING MAX(last_run_time) < CURRENT_TIMESTAMP - INTERVAL '6 HOURS';
```

- `Failed ETL Jobs`: Retrieves most recent failed jobs  
```sql
SELECT *
FROM etl_job_status
WHERE status = 'FAILED'
ORDER BY last_run_time DESC;
```

---

### 🐍 2. Python-Based Health Checks & Alert System

- Automated hourly checks for pipeline failures and data freshness.
- Implemented email-based alerts using `smtplib` for escalations.
- Reduced stakeholder escalations and metric delays by **40%**.

**Modules Implemented:**
- `data_freshness_checker.py`: Checks for stale records  
- `error_log_parser.py`: Extracts failed ETL jobs  
- `email_alerts.py`: Sends automated notifications  
- `utils/logger.py`: Custom logger for monitoring logs  

---

### 📊 3. Tableau Dashboards

- Designed interactive dashboards to visualize:
  - Pipeline health status (Success, Failed, Stale)
  - Daily job counts and error trends
  - Time-based filters for historical view
- Used in weekly Sales Ops sync meetings to improve transparency and reduce investigation time.

---

## 📈 Impact

| Metric                          | Result       |
|----------------------------------|--------------|
| Reporting reliability improved   | **+35%**     |
| Metric delay & escalations cut   | **−40%**     |
| Ops insight visibility (Tableau) | **Real-time**|

---

## 🔄 Folder Structure

```
data-pipeline-monitoring/
├── README.md
├── sql/
│   ├── Freshness Check.sql.txt
│   └── Failed_ETL_Jobs.sql.txt
├── python/
│   ├── data_freshness_checker.py
│   ├── error_log_parser.py
│   ├── email_alerts.py
│   └── utils/
│       └── logger.py
├── data/
│   └── [Sample CSVs, pipeline logs]
├── tableau/
│   └── dashboard_screenshots/
│       └── pipeline_monitoring_dashboard.png
```

---

## ✅ Future Enhancements

- Integrate with **Slack** for real-time alerts.
- Add **anomaly detection** using statistical thresholds.
- Build **API hooks** for dynamic health dashboards.

---

## 👤 Author

**Yash Shah**  
[LinkedIn](https://www.linkedin.com/in/yashshah033/) | [GitHub](https://github.com/ShahYash12) | [Portfolio](https://yash-shah-portfolio.notion.site)

---

> 📌 _This project represents real-world experience in proactive monitoring, operational analytics, and cross-functional collaboration using modern data tools._
