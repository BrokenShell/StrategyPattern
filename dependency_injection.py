""" Strategy Pattern: Dependency Injection """
from typing import Callable
from Fortuna import shuffle


def alpha(val):
    return f"alpha {val}"


def beta(val):
    return f"beta {val}"


def delta(val):
    return f"delta {val}"


def engage(func: Callable, *args, **kwargs):
    print(func(*args, **kwargs))


action_queue = [
    alpha,
    beta,
    delta,
]

shuffle(action_queue)

for count, action in enumerate(action_queue, 1):
    engage(action, count)
