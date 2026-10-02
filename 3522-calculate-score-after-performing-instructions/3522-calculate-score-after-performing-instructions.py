class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        i=0
        score=0
        hsh=set()
        while (i>=0 and i<len(instructions) and i not in hsh):# 1st {0} i=0+2=2,
            hsh.add(i)
            if instructions[i]=="add":
                score+= values[i]
                i+=1
            elif instructions[i]=="jump":
                i+=values[i]
        return score






        


        