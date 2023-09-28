def subarraysWithKDistinct(nums, k):
        count = cnt = 0
        arr = {}
        j = i = 0
        for x in nums:
            if not(x in arr):
                arr[x] = 0
        while j < len(nums):
            if arr[nums[j]] == 0:
                cnt += 1
            arr[nums[j]] += 1

            while cnt > k:
                if arr[nums[i]] == 1:
                    cnt -= 1
                arr[nums[i]] -= 1
                i += 1

            f = i
            arr_1 = dict(arr)
            while cnt == k:
                count += 1
                if arr_1[nums[f]] == 1:
                    break
                arr_1[nums[f]] -= 1
                f += 1

            j += 1

        return count