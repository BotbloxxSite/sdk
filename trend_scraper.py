import json

def get_trends():
    trends = [
        "simulator",
        "tycoon",
        "obby",
        "idle progression"
    ]
    with open("research/signals.json", "w") as f:
        json.dump(trends, f)
    return trends
