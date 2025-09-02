

def print_fibonacci(length):
    """
    Prints a list containing the Fibonacci sequence up to the given length.
    - If length == 0 → prints []
    - If length == 1 → prints [0]
    - If length == 2 → prints [0, 1]
    - Otherwise → builds the sequence iteratively
    """
    sequence = []

    if length > 0:
        sequence.append(0)
    if length > 1:
        sequence.append(1)

    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])

    print(sequence)
