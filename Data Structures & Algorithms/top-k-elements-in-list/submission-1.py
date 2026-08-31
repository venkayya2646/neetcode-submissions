class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        s=sorted(s.items(), key=lambda x: x[1], reverse=True)
        l=[]
        for i in range(k):
            l.append(s[i][0])
        return l