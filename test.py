import random
# Compute number of lines to push down smaller matrix (for pretty aligment purposes)

for i in range(10):
    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)

    d_max = max(d1, d2)
    d_min = min(d1, d2)
    # Compute number of lines to push down smaller matrix (for pretty aligment purposes)
    # Do not ask how I came up with this formula. It just works. More detailed notes in
    # Goodnotes document
    push_down_factor = 0
    for _ in range(d_min, d_max, 2):
        push_down_factor += 1

    push_down = (d_max - d_min) // 2
    if not push_down_factor == push_down:
        print(d1, d2)
        print(push_down_factor)
        print(push_down, "\n")
