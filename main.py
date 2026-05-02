from data import event_stream
from ranking import rank_events
from anomaly import detect_anomalies
from metrics import Metrics
from logger import log

metrics = Metrics()

events = list(event_stream(num_users=5, events_per_user=5))
ranked_events = rank_events(events)
anomalies = detect_anomalies(ranked_events)

log("Top Ranked Content Events:")
for event in ranked_events[:10]:
    print(event)
    metrics.record_event(event["score"])

log("Anomaly Report:")
if anomalies:
    for a in anomalies:
        print("-", a)
    metrics.record_anomalies(len(anomalies))
else:
    print("No anomalies detected")

metrics.summary()