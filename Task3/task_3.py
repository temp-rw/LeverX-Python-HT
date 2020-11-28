from concurrent.futures import ThreadPoolExecutor


def function(arg):
    a = 0
    for _ in range(arg):
        a += 1
    return a


def main():
    threads = []
    executor = ThreadPoolExecutor(max_workers=5)

    for i in range(5):
        thread = executor.submit(function, 1000000)

        threads.append(thread)

    a = sum([t.result() for t in threads])
    print("----------------------", a)  # 5000000
