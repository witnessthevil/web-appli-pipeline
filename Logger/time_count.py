from functools import wraps
import time 
from Logger.Log import Logger

log = Logger().get_logger(__name__)

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        log.info(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds') # this one can change to logger 
        return result
    return timeit_wrapper