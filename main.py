import math
from typing import List

def bigO():
    #BigO tells us which implementation/algorithm is better especially in scaling

    timeComplexity = "Time taken to run the algorithm, number of "
    SpaceComplexity = "Space needed to run the algorithm"

    fn = "N is linear, n^2 is quadratic O(c)/O(1) is constant"
    speed = "N! > a^N > n^a > nlogn > n > logn > c, worst case"
    simplify = "ignore lower terms and constants, keeping highest term"
    cost = "arithmetic,array[i] print,functions are all 1 operation"

    Constant  = "O(1)    = Number of instructions is independent of N"
    linear    = "O(N)    = For Loops based on N sized Array/iterations"
    logn      = "O(logN) = Inverse of a polynomial, Binary Search"
    polynomial= "O(N^2)  = Nested For Loop, N*N, generally N^a Polynomial"
    nlogn     = "O(NlogN)= Merge Sort"
    nFactorial= "O(N!)   = "

    spaceComplexity = "Memory needed to run the algorithm"

    #Below all are O(N) to Store
    hashTable  = "O(N) because number of slots in dictionary is proportional to N"
    Stacks     = "O(N) because number of elements is proportional to N"
    Queues     = "O(N) because number of elements is proportional to N"
    Arrays1D   = "O(N) for 1D, N^2 for 2D"
    Strings    = "O(N) because number of characters is proportional to N"
    LinkedList = "O(N) because number of nodes is proportional to N"

    table      = "Access  Insert  Delete Search"
    Array      = "O(1)    O(N)    O(N)    O(N) "
    Stack      = "O(N)    O(1)    O(1)    O(N) "
    Queue      = "O(N)    O(1)    O(1)    O(N) "
    LinkedList = "O(N)    O(1)    O(1)    O(N) "
    HashTable  = "O(1)    O(1)    O(1)    O(1) "
    BST        = "O(logN) O(logN) O(logN) O(logN) "

def BSearchDemo():
    print("BSearch Demo")
    arr = [1,2,3,4,5]
    for i in range(0,len(arr)+1):
        print("Item",i,"Index",BSearch(arr,i))
    print("")

def BSearch(BST : List[int],target: int) -> None:
    #Algorithm only works on sorted collections, such as BST, sorted Array etc
    #Init 2 pointers, Low and High Indexed at 0 and len(array),find midpoint of pointers.
    #Check if midpoint is < or > target, set Low to midpoint if greater, High to midpoint if lesser
    #Repeat till 1 element left, check equality

    #Array Algorithm
    Low = 0
    High = len(BST)-1
    Middle = (Low+High)//2

    while(True):
      #print("Low",Low,"Middle",Middle,"High",High)
      if target == BST[Middle]:
          return Middle
      if target == BST[Low]:
          return Low
      if target == BST[High]:
          return High

      elif target > BST[Middle]:
          Low = Middle
      elif target < BST[Middle]:
          High = Middle
      Middle = (High+Low)//2
      if (Low == Middle or High == Middle):
          return -1

def SlidingWindow():
    arr = [80, -50, 90, 100]
    k = 2

    arrSum = sum(arr[i] for i in range(len(arr)))
    print(arrSum)

def moveZeroes(nums: List[int]) -> None:
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index,len(nums)):
        nums[i] = 0
    return nums

# Time complexity is NlogN, space is O(N)
def numRescueBoats(people: List[int], limit:int) -> int:

    #people array contains people's weight, limit is max boat weight
    #boat carries max 2

    #max is len(people), min is (len(people)//2)+

    people.sort() #sorts array in O(N) time/space

    nrBoats = 0

    lightest = 0
    heaviest = len(people)-1
    while (lightest <= heaviest):

        if(lightest == heaviest):#person gets boat by themselves
            nrBoats +=1
            break
        if (people[lightest] + people[heaviest] <= limit): #put heaviest and lightest together
            nrBoats  +=1
            lightest +=1
            heaviest -=1
        else:                                              #heaviest person goes alone
            nrBoats += 1
            heaviest-= 1

    return nrBoats

def missingNumber(nums: List[int]) -> int:
    Largest = max(nums)
    Smallest = min(nums)-1#We do this to remove the double counting
    GaussSum = (Largest*(Largest+1)/2) - (Smallest*(Smallest+1)/2)

    ActualSum = sum(nums)
    Missing = int(GaussSum-ActualSum)
    return Missing

#returns number of primes under N
def countPrimes(n : int) -> int:
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

def single(nums : List[int]) -> int:
    








if __name__ == '__main__':
    bigO()
    #BSearchDemo()
    #SlidingWindow()

    #print(moveZeroes([0,1,0,3,12]))
    #print(moveZeroes([0,0,1]))
    #print(moveZeroes([1,0,0,1]))

    #print(numRescueBoats([3,2,2,1],3))

    #print(missingNumber([1,3,4,5]))
    print(countPrimes(5))

