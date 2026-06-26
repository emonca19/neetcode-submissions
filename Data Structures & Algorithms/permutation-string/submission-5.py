class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        lenS1, lenS2 = len(s1), len(s2)
        mpS1, mpS2 = [0] * 26, [0] * 26

        if lenS1 > lenS2:
            return False
        
        for r in range(lenS1):
            mpS1[ord(s1[r]) - ord('a')] += 1
            mpS2[ord(s2[r]) - ord('a')] += 1

        if mpS1 == mpS2:
            return True
        
        for l in range(lenS1, lenS2):
            mpS2[ord(s2[l]) - ord('a')] += 1
            mpS2[ord(s2[l- lenS1]) - ord('a')] -= 1
            if mpS2 == mpS1:
                return True
        return False



        


            







            
        