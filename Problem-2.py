def generate_series(a: int):
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    return result
