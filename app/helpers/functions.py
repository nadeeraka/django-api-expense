def valdate(x):
    if x is not None:
        if type(x) == int:
            if x > 0:
                return True;
        elif type(x) == list:
            if len(x) > 0:
                return True
    return False


def select_mx(arr):
    x = 0
    for e in arr:
        if e > x:
            x = e
    return x


def select_min(arr):
    if not valdate(arr):
        return False
    x = arr[0]
    for e in arr:
        if x > e:
            x = e
    return x