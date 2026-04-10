class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        op = {}
        for each in s:
            if each in op:
                op[each] += 1
            else:
                op[each]  = 1
        print(op)
        for each in t:
            if not each in op:
                op[each] = 1
            else:
                op[each] -= 1
        return all(value == 0 for value in op.values())

        