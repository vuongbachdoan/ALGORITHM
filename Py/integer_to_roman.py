class Solution(object):
    romanChars = [{1: 'I'}, {5: 'V'}, {10: 'X'}, {50: 'L'}, {100: 'C'}, {500: 'D'}, {1000: 'M'}]
    
    def dividedArrayByUnit(num):
        arr = []
        unit = 1
        while num != 0:
            foundNumber = num % 10
            arr.insert(0, foundNumber * unit)
            num = num // 10
            unit *= 10
        return arr

    def findRoman(self, num):
        # for item in self.romanChars:
        #     print(item)
        print(self.romanChars[0])
 
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.findRoman(self, 30)
        arrayOfUnitsDivided = self.dividedArrayByUnit(num)


        
Solution.intToRoman(Solution, 58)

        