from typing import List
import bisect

class Engineer:
    def __init__(self, speed, efficiency):
        self.speed = speed
        self.efficiency = efficiency
    def __repr__(self):
        return f"e: {self.efficiency}"

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []
        for i, j in zip(speed, efficiency):
            enginner = Engineer(i, j)
            engineers.append(enginner)
        engineers.sort(key=lambda r:-1*r.efficiency)
        speed_q = []
        e_q = {}
        num_e = max_perf = existing_speed = 0
        for e in engineers:
            i = bisect.bisect_left(speed_q, e.speed)
            if num_e < k:
                if e.speed not in e_q:
                    e_q[e.speed] = [e.efficiency]
                else:
                    e_q[e.speed].append(e.efficiency)
                speed_q.insert(i, e.speed)
                existing_speed += e.speed
                num_e +=1
            else:
                speed_q.insert(i, e.speed)
                if e.speed not in e_q:
                    e_q[e.speed] = [e.efficiency]
                else:
                    e_q[e.speed].append(e.efficiency)
                rem_sp = speed_q.pop(0)
                if len(e_q[rem_sp]) == 1:
                    e_q.pop(rem_sp)
                else:
                    e_q[rem_sp] = e_q[rem_sp][:-1]
                existing_speed = existing_speed - rem_sp + e.speed
            poss_perf = (existing_speed * e.efficiency)
            max_perf = max(max_perf, poss_perf)
        return max_perf % (pow(10, 9) + 7)

if __name__ == "__main__":
    n = 6
    speed = [2,10,3,1,5,8]
    efficiency = [5,4,3,9,7,2]
    k = 2
    s = Solution()
    print(s.maxPerformance(n, speed, efficiency, k))