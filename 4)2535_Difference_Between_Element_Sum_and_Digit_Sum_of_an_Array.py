class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total_sum = 0
        for item in nums:
            total_sum += item
        

        difference_array = []
        for item in nums:
            length = len(str(item))
            divider = 10 ** (length - 1)
            if length == 1:
                difference_array.append(item)
            else:
                while divider >= 1:
                    digit = item // divider
                    difference_array.append(digit)
                    item %= divider
                    divider //= 10

       

        digit_sum = sum(difference_array)
        

        absolute_difference = abs(total_sum - digit_sum)
       

        return absolute_difference

