""" Strategy Pattern: Dynamic Dispatch """


def alpha(val):
    return f"alpha {val}"


def beta(val):
    return f"beta {val}"


def delta(val):
    return f"delta {val}"


def default(val):
    return val


dispatch = {
    "alpha": alpha,
    "beta": beta,
    "delta": delta,
}

action, value = "alpha", 100
print(dispatch[action](value))

action = input("Action: ")
value = input("Value: ")
print(dispatch.get(action, default)(value))
