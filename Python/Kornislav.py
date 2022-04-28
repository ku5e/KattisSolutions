#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose: Kornislav

nums = list(map(int, input().split()))
nums = sorted(nums)
ans = nums[0] * nums[len(nums) - 2]
print(ans)