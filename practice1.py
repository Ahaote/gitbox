
"""
【线段重合】
https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37
步骤1：按起点排序（类似会议排期）
将所有线段按起点从小到大排序（若起点相同则按终点排）
这样处理线段时，可以保证当前线段的起点≥之前所有线段的起点，避免重复比较

步骤2：小根堆实时维护
清理旧会议：每次处理新会议时，踢出所有已经结束的会议（堆中结束时间≤新会议开始时间）
登记新会议：将新会议的结束时间记录到本子上
统计最大会议室需求：本子上当前记录的数量就是需要的最大会议室数量（即线段重合数）

处理 [1,6] → 堆空 → 记录6 → 当前1个重叠 
处理 [2,4] → 堆顶6>2 → 记录4 → 当前2个重叠
处理 [3,10] → 堆顶4>3 → 记录10 → 当前3个重叠（最大值更新为3）
处理 [9,20] → 堆顶4≤9 → 踢出4 → 堆顶6≤9 → 踢出6 → 记录20 → 当前1个重叠 


三、为什么这个算法有效？
决定性观察: 任何重合区域的左边界必定是某个线段的起点2。因此只需检查每条线段起点处的重叠情况。
堆的单调性：小根堆始终维护可能重叠的线段中最小的结束时间，踢出旧线段的操作保证了堆中所有线段都与当前线段有实际重叠1。
时间复杂度优化：暴力法需两两比较（O(n²)），此方法通过排序+堆将复杂度降为O(n log n)。
"""

import sys
import heapq

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split()))  for _ in range(n)]

#第一步，先讲所有线段按头大小排序
matrix = sorted(matrix, key=lambda x : x[0])

#第二步，建立小堆找出重合线段个数
heap = []
ans = 0
num = 0

for item in matrix:
    while len(heap) > 0 and item[0] >= heap[0]:
        heapq.heappop(heap)
        num -= 1
    if len(heap) == 0 or item[0] < heap[0]:
        heapq.heappush(heap, item[1])
        num += 1
    ans = ans if ans > num else num


print(ans)