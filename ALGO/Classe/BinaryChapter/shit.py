def size(minimum: int, maximum: int):
    n = int(input("Enter N"))
    if minimum < n < maximum:
        return n
    return size(minimum, maximum)
