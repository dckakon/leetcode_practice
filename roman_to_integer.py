class Solution:
    def romanToInt(self, s: str) -> int:
        
        rtoi={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        intvalue=0
        
        for i in range(len(s)-1):
            if( rtoi[s[i]]<rtoi[s[i+1]]):
                intvalue= intvalue-rtoi[s[i]]
            else:
                intvalue = intvalue + rtoi[s[i]]
        
        return intvalue+rtoi[s[-1]]