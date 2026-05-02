# StreamSense

Video recommendation engine with ranking, feedback monitoring, and anomaly detection.

---

## Overview

StreamSense is a simulation of a modern content recommendation system designed to rank video content based on user engagement signals. The system processes user interaction data, computes relevance scores, and monitors feed quality using anomaly detection techniques.

It models key concepts used in real-world platforms such as TikTok, Netflix, and YouTube, including ranking pipelines, engagement-based scoring, and system monitoring.

---

## Key Features

* Generation of user interaction events (watch time, clicks, likes)
* Ranking engine based on engagement-driven scoring
* Content prioritization using weighted signals
* Feed quality monitoring through anomaly detection
* Metrics tracking for system observability
* Structured logging for debugging and analysis

---

## System Architecture

```id="qv8i3o"
User Events → Feature Signals → Ranking Engine → Ranked Feed
                                      ↓
                              Anomaly Detection
                                      ↓
                                 Metrics & Logs
```

---

## How It Works

### 1. Data Generation

`data.py` simulates user interaction events including:

* watch time
* click behavior
* likes

---

### 2. Ranking Engine

`ranking.py` computes a relevance score using:

* watch time (primary signal)
* clicks and likes (engagement signals)
* content-type weighting

Content is then sorted based on this score to generate a ranked feed.

---

### 3. Anomaly Detection

`anomaly.py` monitors feed quality by detecting:

* low click-through rate (CTR)
* unusually high watch-time spikes

These signals help identify potential issues in recommendation quality.

---

### 4. Logging and Metrics

* `logger.py` provides structured, timestamped logs
* `metrics.py` tracks:

  * total events processed
  * average ranking score
  * anomalies detected

---

## Run the Project

```id="t6c4px"
python3 main.py
```

---

## Sample Output

```id="y6c7z2"
[12:45:10] Top Ranked Content Events:
{'user_id': 'user_2', 'content_id': 41, 'watch_time': 118.32, 'clicked': 1, 'liked': 1, 'score': 96.2}

[12:45:11] Anomaly Report:
- Low CTR detected

=== Metrics Summary ===
Total events processed: 25
Average score: 68.45
Total anomalies detected: 1
```

---

## Tech Stack

* Python
* Data Processing
* Basic Statistical Analysis
* Recommendation System Concepts

---

## Key Learnings

* Designing a ranking pipeline based on user engagement signals
* Implementing scoring logic for recommendation systems
* Monitoring system quality using anomaly detection
* Building modular, extensible backend systems

---

## Future Improvements

* Add matrix factorization or embeddings for personalization
* Introduce real-time streaming with queues
* Store events in a database
* Build a dashboard for recommendation metrics
* Improve anomaly detection using statistical models

---

## Author

Ancy Patel
