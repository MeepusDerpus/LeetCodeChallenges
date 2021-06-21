# LeetCodeChallenges
 My Attempts at various LeetCode Challenges
 
 bigO() Is a simple crash course in algorithm analysis & Complexity, Will update later to make user friendly and print out info
 
 BSearch(BST,Target) Is a binary search algorithm on an array, searching for the index of target, returning -1 if it does not exist.
 This was done for practicing O(LogN) time complexity and O(N) Space complexity due to the entire Array
 
 Sliding Window is an Optimization algorithm that I will detail later.
 
 moveZeroes(nums) Is a sorting algorithm, moving zeroes to the end of the array, 
 preserving the order of the non zero elements and moving them to the begining
 
 There is an added restriction of only moving elements inside the array rather than inserting into another array.
 This saves space, keeping complexity at O(N) and time complexity being O(N) as well as we do two iterations over the array.
 
 NumRescueBoats(people,limit) returns the minimum number of boats needed to rescue people.
 People is an array containing their weights, limit is the weight limit of each life boat. 
 Note that upto 2 people can fit into a life boat regardless of weight, this greatly simplifies things 
 
 Time complexity is O(N)/O(nLogN) as we use people.sort() and Iterate in a binary search manner over the people array.
 Space complexity is O(N) as well as we do not create any new arrays and sorting is O(N) as well.
 
