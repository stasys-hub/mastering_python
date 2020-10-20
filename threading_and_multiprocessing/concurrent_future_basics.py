# This is a toy script which explains how to use the concurrent future module 
# for multiprocessing and threading
# we are going to use the process pool executor for this
#import CF

import concurrent.futures
import time


# function used for demonstration
def sleeeping_noobs(sec):
    print('How long did the Noob sleep...' )
    time.sleep(sec)
    print(f'... he slept {sec} seconds')
    #return value to explain how we get it while multiprocessing
    return 'Done'


######## MULTIPROCESSING ##########
# call the process pool executor
with concurrent.futures.ProcessPoolExecutor() as executor:
    # execute the function using submit
    # returns a future object
    f1 = executor.submit(sleeeping_noobs, 2)
    f2 = executor.submit(sleeeping_noobs, 2)
    print(f1.result(), f2.result())

######## MULTITHREADING ###########
# call the thread pool executor
with concurrent.futures.ThreadPoolExecutor() as executor2:
    # execute the function using submit
    # returns a future object
    f3 = executor2.submit(sleeeping_noobs, 2)
    f4 = executor2.submit(sleeeping_noobs, 2)
    print(f3.result(), f4.result())





# Let's do the same in a loop with list comprehension -> this works similar for both methods
with concurrent.futures.ProcessPoolExecutor() as executor:
    # we get future objects back -> not results!!!
    results = [executor.submit(sleeeping_noobs,2) for _ in range(5)]
    # to get results we need to exctract them from future objects!!!
    for f in concurrent.futures.as_completed(results):
        print(f.result())
