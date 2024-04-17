import multiprocessing
import random
import time


def worker(number, tasks, results):
    print(f"Worker {number} started")

    # Loop fetching tasks from the queue
    while True:
        task = tasks.get()

        if task is None:
            # Time to die
            print(f"Worker {number} shutting down")
            tasks.task_done()
            return

        # Perform the task
        answer = task()
        tasks.task_done()
        results.put((number, answer))


def job():
    """Importable job for the workers"""
    # Sleep for up to a second
    time.sleep(random.randint(0, 10) / 10)
    # return the result of some onerous calculation
    return random.randint(0, 100)


if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start the workers
    num_workers = multiprocessing.cpu_count() * 2

    workers = [
        multiprocessing.Process(target=worker, args=(i, tasks, results))
        for i in range(num_workers)
    ]
    for w in workers:
        w.start()

    # Enqueue jobs
    num_jobs = 100
    for i in range(num_jobs):
        tasks.put(job)

    # Add a poison pill for each worker
    for i in range(num_workers):
        tasks.put(None)

    # Wait for all the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        worker, result = results.get()
        print(f'Worker: {worker} Result: {result}')
        num_jobs -= 1
