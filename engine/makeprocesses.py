import multiprocessing
import concurrent.futures

def make_processes(func,args=None):
    a = multiprocessing.Process(target=func,args=args)
    a.start()
    a.join()
    a.terminate()

def execute(func,args=None):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1=executor.submit(func,args)
        return f1.result()
