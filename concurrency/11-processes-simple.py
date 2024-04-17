import multiprocessing


def worker(i):
    """worker function"""
    print(f'Worker: {i}')


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()