class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = 2
        answer = []
        for i in range(0,x):
            for j in nums:
                answer.append(j)
        return answer 