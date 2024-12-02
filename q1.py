l, s, m, r, query = 1, 1, 0, 0, input()
current = (l + r, m + s)
for item in query:
    if item == "L":
        l, m = current[0], current[1]
    else:
        r, s = current[0], current[1]
    current = (l + r, m + s)
print(current[0], "/", current[1])