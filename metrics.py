class Metrics:
    def __init__(self):
        self.total_events = 0
        self.total_score = 0
        self.total_anomalies = 0

    def record_event(self, score):
        self.total_events += 1
        self.total_score += score

    def record_anomalies(self, count):
        self.total_anomalies += count

    def summary(self):
        avg_score = self.total_score / self.total_events if self.total_events else 0
        print("\n=== Metrics Summary ===")
        print(f"Total events processed: {self.total_events}")
        print(f"Average score: {avg_score:.2f}")
        print(f"Total anomalies detected: {self.total_anomalies}")