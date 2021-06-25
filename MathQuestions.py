from typing import List
class MathQuestions():
    def __init__(self):
        print("Math")

    def missingNumber(self,nums: List[int]) -> int:
        Largest = max(nums)
        Smallest = min(nums)-1#We do this to remove the double counting
        GaussSum = (Largest*(Largest+1)/2) - (Smallest*(Smallest+1)/2)

        ActualSum = sum(nums)
        Missing = int(GaussSum-ActualSum)
        return Missing

    #returns number of primes under N
    def countPrimes(self,n : int) -> int:
        if n < 2:
            return 0
        arr = [True]*n
        arr[0] = arr[1] = False

        #Sieve of Erastothenes
        for i in range(2,int(math.ceil(math.sqrt(n)))):
            print(i*i,math.ceil(math.sqrt(n)))
            if(arr[i]):
                for multiples in range (i*i,n,1):

                    arr[multiples] = False

        return sum(arr)

    #All elements contain a single duplicate except for one, we return the missing duplicate.
    def singleNumber(self,nums : List[int]) -> int:
        #set() contains all unique elements of the list
        #We know there is
        return 2*sum(set(nums)) - sum(nums)

    #Checks if the robot ends up at (0,0) at the end, returning a boolean
    def judgeCircle(self, moves: str) -> bool:
        Coords = [0,0]

        for move in moves:
            if move == 'U':
                Coords[1] +=1
            elif move == 'D':
                Coords[1] -=1
            elif move == 'L':
                Coords[0] -=1
            elif move == 'R':
                Coords[0] +=1

        #Shorthand return Coords[0] == 0 and Coords[0] == 0
        if Coords[0] == 0 and Coords[1] == 0:
            return True
        else:
            return False

    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        result = ""
        i, j = len(a)-1,len(b)-1

        #11
        #11
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >=0:
                total+=int(a[i])
                i-=1
            if j >=0:
                total+=int(b[j])
                j-=1
            result += ""+str(total%2)
            carry = total //2

        return result[::-1]

