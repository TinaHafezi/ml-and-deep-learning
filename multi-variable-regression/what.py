# Original sequences
x = [[1, 2, 3],[4,5,6],[6,7,8]]
w = [10, 20, 30]

for x, w in zip(x, w):
    print(f"x: {x}, w: {w}")
    y=x*w
    print(y)
