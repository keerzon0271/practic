J = input()
S = input()

jewels = set(J)
count = 0

for stone in S:
    if stone in jewels:
        count += 1

print(count)
