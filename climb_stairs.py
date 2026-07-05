# In how many different ways can you reach the nth stair using only 1-step and 2-step moves


def climb_stairs(n):
    if n == 0 or n == 1:
        return 1

    return climb_stairs(n - 1) + climb_stairs(n - 2)


print(climb_stairs(4))
