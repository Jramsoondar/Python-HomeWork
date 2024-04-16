def main():
    iterations = int(input("Number of iterations: "))
    print(pi_value(iterations))

def pi_value(iterations):
    approximation = 0
    for pi in range(iterations):
        approximation = approximation + (-1) ** pi / (2 * pi + 1)
    return approximation * 4
main()