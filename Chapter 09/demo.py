import cProfile
import time

def do_some_work():
    # Just waste some time
    time.sleep(3)

def costly_process():
    # just a long loop of nothing
    for i in range (10 ** 7):
        pass

def even_more_costly_process():
    # an even longer loop of nothing
    for i in range (10 ** 8):
        pass
    # ... and do some more nothing
    costly_process()

def do_some_stuff():
    costly_process()
    even_more_costly_process()
    time.sleep(4)

def main():
    do_some_work()
    costly_process()
    even_more_costly_process()
    do_some_stuff()

if __name__ == '__main__':
    print("Running...")
    cProfile.run('main()', sort='cumtime')
