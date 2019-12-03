import random
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        ncities = 20
    else:
        ncities = int(sys.argv[1])

    with open("cities.txt", "w") as of:
        for i in range(ncities):
            x = random.random()
            y = random.random()
            of.write(f'{x} {y}\n')
