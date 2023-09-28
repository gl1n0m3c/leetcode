def minOperations(nums: list[int], x: int) -> int:
    if sum(nums) < x:
        return - 1

    left = 0
    right = len(nums) - 1
    s = k = 0
    ans = 10**10

    flag = False
    while s + nums[left] <= x:
        flag = True
        s += nums[left]
        left += 1
        k += 1
    if flag:
        left -= 1


    while s + nums[right] <= x:
        s += nums[right]
        right -= 1
        k += 1

    if s == x:
        ans = min(ans, k)

    # print(s, k)

    if k != 0:
        while left != -1:
            s -= nums[left]
            left -= 1
            k -= 1

            while s + nums[right] <= x:
                flag = True
                s += nums[right]
                right -= 1
                k += 1

            if s == x:
                ans = min(ans, k)
        
    if ans == 10**10:
        return -1
    return ans
