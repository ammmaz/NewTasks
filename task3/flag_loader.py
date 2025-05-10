import json, threading, time, os

class FlagStore:
    def __init__(self, path='flags.json'):
        self.path = path
        self._lock = threading.Lock()
        self._last_mtime = 0
        self.flags = {}
        self._load_flags()
        threading.Thread(target=self._watch_file, daemon=True).start()

    def _load_flags(self):
        with open(self.path) as f:
            self.flags = json.load(f)

    def _watch_file(self):
        while True:
            try:
                mtime = os.path.getmtime(self.path)
                if mtime != self._last_mtime:
                    with self._lock:
                        self._load_flags()
                        self._last_mtime = mtime
            except Exception as e:
                print(f"Error watching file: {e}")
            time.sleep(1)

    def get_flags(self):
        with self._lock:
            return self.flags.copy()

store = FlagStore()
