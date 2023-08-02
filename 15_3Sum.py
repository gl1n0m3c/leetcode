def threeSum(nums):
    s0, s1, s2 = [], [], []
    ans = set()
    for x in nums:
        if x == 0:
            s0.append(x)
        elif x < 0:
            s1.append(x)
        else:
            s2.append(x)
    S1, S2 = set(s1), set(s2)
    if len(s0) > 2:
        ans.add((0, 0, 0))
    if len(s0) > 0:
        for x in S2:
            if -1*x in S1:
                ans.add((-1*x, 0, x))
    for i in range(len(s1) - 1):
        for j in range(i + 1, len(s1)):
            target = -1*(s1[i] + s1[j])
            if target in S2:
                ans.add(tuple(sorted([s1[i], s1[j], target])))
    for i in range(len(s2) - 1):
        for j in range(i + 1, len(s2)):
            target = -1*(s2[i] + s2[j])
            if target in S1:
                ans.add(tuple(sorted([s2[i], s2[j], target])))
    return ans
            
print(threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))