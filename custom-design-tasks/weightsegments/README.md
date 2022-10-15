Given and array of integers and number k. Find all subsequences of the array where the difference between min and max elements of the subsequence is not larger than k. Return the amount of these subsequences

Example:

arr=[1,2,8], k = 6
(0,0): 1 - 1 < 6
(0,1): 2 - 1 < 6
(0,2): 8 - 1 > 6
(1,1): 2 - 2 < 6
(1,2): 8 - 2 = 6
(2,2): 8 - 8 < 6
Answer: 5