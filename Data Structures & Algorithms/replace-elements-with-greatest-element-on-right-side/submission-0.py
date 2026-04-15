class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a_list = []
        for i in range(len(arr)):
            biggest = -1
            for j in range(i+1,len(arr)):
                if arr[j] > biggest:
                    biggest = arr[j]
            arr[i] = biggest
            a_list.append(arr[i])
            if i == len(arr):
                arr[i] == -1
                a_list.append(arr[i])
        return a_list