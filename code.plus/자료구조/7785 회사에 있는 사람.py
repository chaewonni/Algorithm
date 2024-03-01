import sys

n = int(sys.stdin.readline())

name_set = set()

for i in range(n):
    name, action = sys.stdin.readline().split()

    if action == "enter":
        name_set.add(name)
    elif action == "leave":
        name_set.discard(name)

sorted_names = sorted(name_set, reverse=True)

# for i in range(len(sorted_names)):
#     print(sorted_names[i])

for name in sorted_names:
    print(name)