# Input: p (starting position), s (unused), n (number of iterations)
p, s, n = list(map(int, input().split()))
p -= 1
seq = list(map(int, input().split()))
# Initialize places dictionary
places = {}
# Convert 1D index to 2D grid position
def pToPos(a):
    y = a // 5
    x = a % 5
    return (x, y)
# Draw the grid
def draw():
    for y in range(5):
        for x in range(5):
            print(places.get((x, y), 0), end="")
        print()
    print()
# Main simulation
for i in range(n):
    pos = pToPos(p)
    places[pos] = places.get(pos, 0) + 1
    # Handle overflowing cells
    while True:
        handled = True
        for item in list(places.keys()):
            while places[item] >= 4:
                places[item] -= 4
                x, y = item
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    neighbor = (x + dx, y + dy)
                    places[neighbor] = places.get(neighbor, 0) + 1
                handled = False
        if handled:
            break
    # Update position using sequence
    p = (p + seq[i % len(seq)]) % 25
# Draw the final grid
draw()