class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        findV=[]
        for element in s:
            for v in vowels:
                if(element == v):
                    findV.append(element)
        print(findV)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i]=findV.pop(-1)

        return ''.join(s)
        