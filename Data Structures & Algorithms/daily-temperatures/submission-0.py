class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*len(temperatures)

        for i,v in enumerate(temperatures):
            while stk and v > stk[-1][0]:
                _,stkIdx = stk.pop()
                res[stkIdx] = i - stkIdx
            stk.append((v,i))
        return res
        