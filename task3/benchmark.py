import timeit
from evaluator import evaluate_flags

def run_benchmark():
    duration = timeit.timeit(
        lambda: evaluate_flags("42", "EU"),
        number=10000
    )
    print(f"Avg eval time: {duration / 10000 * 1_000_000:.2f} µs")

if __name__ == "__main__":
    run_benchmark()
