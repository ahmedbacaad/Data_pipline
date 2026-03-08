import pandas as pd 
import numpy as np 
from datetime import datetime, timedelta
import random


#repropducibility
np.random.seed(42)

#simulation parameters

NUM_USERS = 200
NUM_SESSIONS = 500
EVENTS_PER_SESSION = (3,15)

pages = ["/home", "/search", "/product", "/cart", "/checkout", "/profile"]
event_types = ["view", "click", "purchase"]
devices = ["mobile", "desktop", "tablet"]
countries = ["US", "CA", "UK", "DE", "IN"]

rows = []
start_time = datetime.now() - timedelta(days=7)

for session_id in range(NUM_SESSIONS):
    user_id = random.randint(1, NUM_USERS)
    num_events = random.randint(*EVENTS_PER_SESSION)
    session_start = start_time + timedelta(minutes=random.randint(0, 10000))

    for i in range(num_events):
        rows.append({
            "user_id": user_id,
            "session_id": session_id,
            "timestamp": session_start + timedelta(seconds=i * random.randint(5, 30)),
            "page": random.choice(pages),
            "event_type": random.choice(event_types),
            "device": random.choice(devices),
            "country": random.choice(countries),
        })

df = pd.DataFrame(rows).sort_values("timestamp")
df.to_csv("data/raw/user_clicks.csv", index=False)

print(f"Generated {len(df)} rows of user behavior data")
