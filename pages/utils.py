import datetime
import logging
from time import sleep

from pages.values import User


def user_value():
    """Add  user value"""
    return User


def wait_until_ok(timeout=7, period=0.5):
    """Retires function until ok (or 5 seconds)"""
    log = logging.getLogger("[Wait until OK]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catch: {err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """Add log for method base on the docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)

        log.info(func.__doc__)

        return result

    return wrapper
