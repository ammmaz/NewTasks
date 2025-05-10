Redis Failure Handling:
If Redis is unreachable, limiter blocks requests (False from is_allowed).

This prevents abuse in degraded mode.

Clock Skew:
Mitigated by always using server-side timestamps (from time.time()).

Client clock irrelevant, consistent behavior across multiple app instances.