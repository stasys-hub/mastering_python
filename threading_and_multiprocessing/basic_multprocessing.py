### This is a basic python Scripts which shows how to use multiprocessing in python

#import time for benchmarks and multiprocessing module
import time 
import multiprocessing

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
processes = []

#cerate a 5 processes of 'sleeping noob'
for _ in range(5):
    # create a process using the MP module
    p = multiprocessing.Process(target = sleeeping_noobs, args = [2])
    # start the process
    p.start()
    # append the process to the process list
    processes.append(p)

for process in processes:
    # join method will coordinate all processes
    process.join()


