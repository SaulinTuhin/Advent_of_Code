import os
from collections import Counter

class Solution:
    def findPathDiff(self, list1: list[int], list2: list[int]) -> int:
        path_diff = 0
        list1.sort()
        list2.sort()
        for i in range(len((list1))):
            path_diff += abs(list1[i] - list2[i])
        return path_diff
    
    def findSimilarityScore(self, list1: list[int], list2: list[int]) -> int:
        similarity_score = 0
        list2_freq = Counter(list2)
        for num in list1:
            similarity_score += num * list2_freq[num]
        return similarity_score


if __name__=="__main__":
    sol = Solution()

    # Take input from file
    # Call the solution function using the data
    list1, list2 = [], []
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    with open(cur_dir + '/input.txt', 'r') as f:
        for line in f.readlines():
            line = line.split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))

    print('Path Diff - ' + str(sol.findPathDiff(list1, list2)))
    print('Similarity score - ' + str(sol.findSimilarityScore(list1, list2)))