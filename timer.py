import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.process_time()
        ret = func(*args, **kwargs)
        elapsed = time.process_time() - start
        print(f"Функция {func.__name__} время выполнения: {elapsed}")
        return ret
    return wrapper