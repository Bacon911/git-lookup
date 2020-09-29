def mixa_krutoy(count):
    import random
    arr = []
    for _ in range(count):
        arr.append(random.randrange(0, 10))
    return arr

print(mixa_krutoy(50))
