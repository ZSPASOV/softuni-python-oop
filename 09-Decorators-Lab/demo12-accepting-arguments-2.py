import time


def measure_time(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f'Total time: {total}')
        return res
    return wrapper

@measure_time
def do_something():
    return



do_something() # Total time: 0.0 - otnelo e 0 sekundi za izpalnenie

@measure_time
def do_other_thing():
    time.sleep(1)
    return

do_other_thing() # Total time: 1.0000569820404053 - otnelo e malko nad 1 sekunda za izpalnenie