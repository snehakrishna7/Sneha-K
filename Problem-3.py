def generate_pattern_series(a: int):
    result = []
    count = 0
    num = 1
    while count < a:
        result.append(num)
        count += 2  # only odd positions count
        num += 2
    return result
