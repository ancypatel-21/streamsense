def detect_anomalies(events):
    anomalies = []

    if not events:
        return anomalies

    ctr_values = []
    watch_times = []

    for event in events:
        ctr_values.append(event["clicked"])
        watch_times.append(event["watch_time"])

    avg_ctr = sum(ctr_values) / len(ctr_values)
    avg_watch_time = sum(watch_times) / len(watch_times)

    if avg_ctr < 0.25:
        anomalies.append("Low CTR detected")

    if avg_watch_time > 90:
        anomalies.append("Watch-time spike detected")

    return anomalies