from typing import List
class HashTables():

    #Return Indices of 2 numbers that add up to target
    @staticmethod
    def twoSum(self,nums : List[int],target : int) -> List[int]:
        m = {}#dictionary of nums and their index in arr
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in m:
                return [m[goal],i]  #returns i and dictionary value of key [goal]
            m[nums[i]] = i          #Adds to dictionary

    #Returns a bool if an array has a duplicate value
    @staticmethod
    def containsDuplicates(self, nums : List[int]) -> bool:
        m = {}

        for num in nums:
            if num in m:
                return True
            m[num] = 1
        return False

    #returns the number occuring more than 50% of the time else 0
    @staticmethod
    def majorityElement(self,nums : List[int]) -> int:
        numsMap = {} #list of numbers as keys and their frequency as values

 #       for num in nums:
 #           if num in numsMap:
 #               numsMap[num] += 1
 #           else:
#                numsMap[num] = 1

        for num in nums:
            numsMap[num] = numsMap.get(num,0) + 1 #gets value for key num else sets it to 0

        for key in numsMap:
       #     print(key,numsMap[key])
            if numsMap[key] > (len((nums))//2):
                return key
        return 0

    #Complexity O(N*M*LogM)
    #N number of words, M is longest word
    #M*logM is due to hashing sort
    @staticmethod
    def groupAnagrams(self, words : List[str]) -> List[str]:
        hashMap = {}
        answers = []

        for string in words:
            hashVal = "".join(sorted(string))   #tan, nat hash to ant
            if hashVal in hashMap:              #checks if it's in hashmap
                hashMap[hashVal].append(string) #appends it as a list
            else:
                tempList = []
                tempList.append(string)
                hashMap[hashVal] = tempList     #creates new list for value

                #OR
                #hashMap[hashVal] =[]
                #hashMap[hashVal] = tempList

        for values in hashMap.values():         #Returns hash values as list
            answers.append(values)
        return answers

    @staticmethod
    def fourSumV2(self,A : List[int],B : List[int],C : List[int],D : List[int]) -> int:
        #count how many tuples ijkl such that the sum of ABCD[ijkl] is 0
        Map = {}
        Answer = 0
        lA,lB,lC,lD = len(A),len(B),len(C),len(D)

        for i in range(lA):
            x = A[i]
            for j in range(lB):
                y = B[j]
                if (x+y not in Map):
                    Map[x+y] = 0
                Map[x+y] += 1

        for i in range(lC):
            x = C[i]
            for j in range(lD):
                y = D[j]
                target = -(x+y)
                if(target in Map):
                    Answer += m[target]

        return Answer

    def __init__(self):
        #print(HashTables.twoSum(self,[1,2,3,4],3))
        #print(HashTables.majorityElement(self,[1,2,4,4,3,4,4,4,6]))
        #print(HashTables.groupAnagrams(self,["bat","tan","eat","tea","ate","nat"]))