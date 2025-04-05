import time
import math
import threading
import multiprocessing
import asyncio
import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    print(f"Calculating Fibonacci for n = {n}", flush=True)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial(n):
    print(f"Calculating Factorial for n = {n}", flush=True)
    return math.factorial(n)

def prime_worker(start, step, deadline, return_dict, idx):
    current = start
    largest = 0
    count = 0
    while time.time() < deadline:
        if is_prime(current):
            largest = current
            count += 1
        current += step
    return_dict[idx] = (largest, count)

def full_task_multiprocess():
    cpu_count = multiprocessing.cpu_count()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    deadline = time.time() + 10  # 🔁 10-second test

    processes = []
    for i in range(cpu_count):
        start = 3 + i * 2
        step = 2 * cpu_count
        p = multiprocessing.Process(target=prime_worker, args=(start, step, deadline, return_dict, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    largest_prime = 2
    total_primes = 1

    for result in return_dict.values():
        largest_prime = max(largest_prime, result[0])
        total_primes += result[1]

    print("\nTotal primes found across all processes:", total_primes, flush=True)
    print("Largest prime found:", largest_prime, flush=True)
    print("Fibonacci({}) = {}".format(largest_prime, fibonacci(largest_prime)), flush=True)
    print("Factorial({}) = {}".format(largest_prime, factorial(largest_prime)), flush=True)

def full_task_single():
    start_time = time.time()
    current = 2
    largest_prime = 0
    prime_count = 0

    print("Running for 10 seconds (single-threaded)...", flush=True)

    while time.time() - start_time < 10:
        if is_prime(current):
            largest_prime = current
            prime_count += 1
        if current == 2:
            current += 1
        else:
            current += 2

    print("\nTotal primes found:", prime_count, flush=True)
    print("Largest prime found:", largest_prime, flush=True)
    print("Fibonacci({}) = {}".format(largest_prime, fibonacci(largest_prime)), flush=True)
    print("Factorial({}) = {}".format(largest_prime, factorial(largest_prime)), flush=True)

async def async_full_task():
    await asyncio.to_thread(full_task_single)

def run_main(mode="thread"):
    print(f"\n[INFO] Running in {mode.upper()} mode for 10 seconds...\n", flush=True)
    
    if mode == "thread":
        t = threading.Thread(target=full_task_single)
        t.start()
        t.join()
    elif mode == "process":
        full_task_multiprocess()
    elif mode == "async":
        try:
            asyncio.run(async_full_task())
        except RuntimeError:
            import nest_asyncio
            nest_asyncio.apply()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_full_task())
    else:
        print("Invalid mode. Choose 'thread', 'process', or 'async'.", flush=True)

if __name__ == "__main__":
    mode = "async"  # Change to: "thread", "process", or "async"
    run_main(mode)
