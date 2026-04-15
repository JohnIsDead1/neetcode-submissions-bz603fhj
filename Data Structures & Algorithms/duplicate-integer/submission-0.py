class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a_dict = {}
        for num in nums:
            if num not in a_dict:
                a_dict[num] = 1
            else:
                a_dict[num] += 1
        for value in a_dict.values():
            if value > 1:
                return True
        return False