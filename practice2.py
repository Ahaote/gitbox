'''
【将数组和减半的最少操作次数】
https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/description/

核心思路是每次操作都选择当前数组中的最大元素进行减半
每次减半最大的数能最大限度地减少总和，从而用最少次数达成目标。如果优先处理小数，可能需要更多次操作。
使用最大堆（优先队列）：
将数组所有元素存入堆中，每次弹出堆顶（最大值），减半后再放回堆。这样可以动态维护当前最大值。

假设数组是 [5, 19, 8, 1]，总和是 33。目标是让总和减少到 ≤16.5（即至少减少一半）：

第一步操作：选最大的数 19 减半变成 9.5 → 总和减少 9.5
第二步操作：再选当前最大的数 9.5 减半变成 4.75 → 总和再减少 4.75
第三步操作：接着选当前最大的数 8 减半变成 4 → 总和再减少 4
此时总和减少了 9.5+4.75+4=18.25 >16.5，仅需 3次操作。

'''
#如何用负数模拟最大堆
# import heapq
# num = [2,3,7,9,4,6]
# nums = [-x for x in num]
# heapq.heapify(nums)
# while len(nums) > 0:
#     print(-nums[0])
#     heapq.heappop(nums)

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums)/2
        heap = [-x for x in nums]
        heapq.heapify(heap)

        reduced = 0
        count = 0

        while reduced < half:
            top = heapq.heappop(heap)
            heapq.heappush(heap,top/2)
            count += 1
            reduced += -top/2
        
        return count