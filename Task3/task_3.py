from threading import Thread, Lock


a = 0


def thread_locker(func):
    lock = Lock()

    def wrapper(*args):
        func(*args, lock)

    return wrapper


@thread_locker
def function(arg, lock):
    global a
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()


def main():
    threads = []

    for i in range(5):
        thread = Thread(target=function, args=(1000000, ))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)  # 5000000


if __name__ == '__main__':
    main()
