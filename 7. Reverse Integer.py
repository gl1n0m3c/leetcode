def reverse(x: int) -> int:
    if x < 0:
        x1 = int(-1 * int(str(x)[1:][::-1]))
    else:
        x1 = (int(str(x)[::-1]))
    if -2**31 < x1 < 2**31 - 1:
        return x1
    return 0


print(reverse(123))
print(reverse(-123))
print(reverse(1534236469))
