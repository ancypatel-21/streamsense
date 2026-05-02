def score_event(event):
    score = 0

    # engagement signals
    score += event["watch_time"] * 0.6
    score += event["clicked"] * 10
    score += event["liked"] * 15

    # content-type boost
    if event["content_type"] == "movie":
        score += 5
    elif event["content_type"] == "tv_show":
        score += 4
    elif event["content_type"] == "documentary":
        score += 3
    else:
        score += 2

    return round(score, 2)

def rank_events(events):
    ranked = []
    for event in events:
        event["score"] = score_event(event)
        ranked.append(event)

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked