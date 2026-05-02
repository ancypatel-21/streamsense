import random
import time

CONTENT_TYPES = ["movie", "tv_show", "documentary", "short_clip"]

def generate_user_event(user_id):
    return {
        "user_id": user_id,
        "content_id": random.randint(1, 100),
        "content_type": random.choice(CONTENT_TYPES),
        "timestamp": time.time(),
        "watch_time": round(random.uniform(0, 120), 2),
        "clicked": random.choice([0, 1]),
        "liked": random.choice([0, 1])
    }

def event_stream(num_users=5, events_per_user=5):
    for u in range(num_users):
        for _ in range(events_per_user):
            yield generate_user_event(f"user_{u}")