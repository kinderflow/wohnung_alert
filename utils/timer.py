import time
import random

#Time Delay on requests on www.kleinanzeigen.de for bot protection

def random_pause(min_sec=1.5, max_sec=3.5):

    duration = random.uniform(min_sec, max_sec)
    print(f"Pause für {duration:.2f} Sekunden....")
    time.sleep(duration)

print(random_pause)