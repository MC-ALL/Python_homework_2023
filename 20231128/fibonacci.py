import math

def make_Fibonacci(N):
    n0 = 1
    n1 = 1
    fiboacci_seq = [1, 1]
    for i in range(N - 2):
        n0, n1 = n1, n0 + n1
        fiboacci_seq.append(n1)
    return fiboacci_seq

def converging_ratio(F):
    error = []
    for i in range(len(F) - 1):
        error.append(abs(F[i + 1] / F[i] - (1 + 5 ** 0.5) / 2))
    return error

def compute_rates(F):
    error = converging_ratio(F)
    rate = []
    for i in range(1, len(error) - 1):
        rate.append(math.log(error[i + 1] / error[i]) / math.log(error[i] / error[i - 1]))
    return rate


if __name__ == '__main__':
    F = make_Fibonacci(20)
    print(F)
    print()
    print(converging_ratio(F))
    print()
    print(compute_rates(F))
    