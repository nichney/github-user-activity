from urllib.request import urlopen, Request
import shelve
from contextlib import contextmanager
import time


@contextmanager
def fetch_url(url: str):
    try:
        cache_lifetime = 15 * 60 # 15 minutes
        with shelve.open("storage.shelve") as d:
            current_time = time.time()
            if url in d:
                cached_time, cached_data = d[url]
                if current_time - cached_time < cache_lifetime:
                    yield cached_data
                    return
            data = urlopen(url).read()
            d[url] = (current_time, data)
            yield data
    except Exception as e:
        print(f"Error: {e}")

