import sys
from itertools import accumulate, cycle

def solve(input):    
    c = [int(n.strip()) for n in input]

    part1 = sum(c)

    r = set()
    part2 = next(n for n in accumulate(cycle(c)) if n in r or r.add(n))

    return part1, part2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <input>".format(sys.argv[0]),
              file=sys.stderr)
        exit(1)

    i = None
    with open(sys.argv[1], 'r') as f:
        i = f.readlines()
    
    part1, part2 = solve(i)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")