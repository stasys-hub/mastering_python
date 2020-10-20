### This is a basic python Scripts which shows how to use multiprocessing in python

#import time for benchmarks and multiprocessing module
import time 
import threading

# Let's create a function which we will paralyze using MP

def sleeeping_noobs(sec):
    print('How long did the Noob sleep...' )
    time.sleep(sec)
    print(f'... he slept {sec} seconds')

#execute function in order

#sleeeping_noobs(2)
#sleeeping_noobs(2)

# let's paralellize this using multiprocessing:

#create a list of processes
threads = []

#cerate a 5 processes of 'sleeping noob'
for _ in range(5):
    # create a process using the MP module
    t = threading.Thread(target = sleeeping_noobs, args = [2])
    # start the process
    t.start()
    # append the process to the process list
    threads.append(t)

for thread in threads:
    # join method will coordinate all processes
    thread.join()


