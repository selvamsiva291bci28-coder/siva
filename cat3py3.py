def print_pattern(N1, N2):
    for i in range(N2 - N1 + 1):
        print(' '.join(str(x) for x in range(N1, N2 - i + 1)))

# Input
N1, N2 = map(int, input().split())
print_pattern(N1, N2)
