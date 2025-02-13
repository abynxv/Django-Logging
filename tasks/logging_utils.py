import logging
import functools
import time

logger = logging.getLogger('tasks')

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f'Function {func.__name__} took {end_time - start_time:.2f} seconds to execute',
            extra={
                'function_name': func.__name__,
                'execution_time': end_time - start_time
            }
        )
        return result
    return wrapper