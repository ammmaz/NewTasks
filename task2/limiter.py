import time
import redis

WINDOW_SIZE = 60 * 1000  # 60 sec window in ms
RATE_LIMIT = 100  # allowed requests per minute

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def is_allowed(api_key: str):
    now = int(time.time() * 1000)
    key = f"rate:{api_key}"
    pipeline = r.pipeline()

    try:
        pipeline.zremrangebyscore(key, 0, now - WINDOW_SIZE)
        pipeline.zadd(key, {now: now})
        pipeline.zcard(key)
        pipeline.expire(key, 70)  # TTL to expire old keys
        _, _, count, _ = pipeline.execute()

        return count <= RATE_LIMIT
    except redis.exceptions.RedisError:
        return False  # Safe fallback: block request
