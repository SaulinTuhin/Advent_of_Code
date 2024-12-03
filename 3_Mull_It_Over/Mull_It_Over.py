import os
import re

class Solution:
    def multiplicationSum(self, memory: list[str]) -> int:
        multiplication_sum = 0
        matches = re.findall(r"mul\(([\d]{1,3}),([\d]{1,3})\)", memory)
        for first, second in matches:
            multiplication_sum += int(first) * int(second)
        return multiplication_sum
    
    def multiplicationSum_withLogical(self, memory: list[str]) -> int:
        multiplication_sum = 0
        matches = re.findall(r"mul\(([\d]{1,3}),([\d]{1,3})\)|(do\(\))|(don't\(\))", memory)
        enable = True
        for first, second, do, dont in matches:
            if do or dont:
                enable = bool(do)
            elif not enable:
                continue
            else:
                multiplication_sum += int(first) * int(second)
        return multiplication_sum


if __name__=="__main__":
    sol = Solution()
    
    memory = []
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(base_dir + '/input.txt', 'r') as f:
        for line in f.readlines():
            memory.append(line)
    memory = "".join(memory)
            
    print('Memory corrected calculations - ' + str(sol.multiplicationSum(memory)))
    print('Memory corrected calculations with logic - ' + str(sol.multiplicationSum_withLogical(memory)))