# 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        op = []
        d = {}
        for index, string in enumerate(strs):
            currSorted = "".join(sorted(string))
            if currSorted in d:
                d[currSorted].append(index)
            else:
                d[currSorted] = [index]
        for idxs in d.values():
            print(idxs)
            op.append([strs[i] for i in idxs])
        return op

