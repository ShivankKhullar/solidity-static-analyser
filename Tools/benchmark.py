# benchmark.py
import time

# Create a dictionary to hold total execution times for each function
function_times = {}

def function_benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = (end - start) * 1000  # Time in milliseconds
        # print(f"Execution time for {func.__name__}: {elapsed_time} milliseconds")
        # Accumulate function's execution time
        function_times[func.__name__] = function_times.get(func.__name__, 0) + elapsed_time

        return result
    return wrapper

def print_benchmark_results():
    for function_name, total_time in function_times.items():
        print(f"Total execution time for {function_name}: {total_time} milliseconds")