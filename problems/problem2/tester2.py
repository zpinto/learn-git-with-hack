from answer2 import Solution

twoSum = Solution().twoSum

testcases = [(([2, 7, 11, 15], 9), [0, 1])]

print("Running Unit Tests for Problem 2:\n")

correct_count = 0

for case in testcases:
    result = twoSum(case[0][0], case[0][1])
    print("Input: " + str(case[0]))
    print("Output: " + str(result))
    print("Expected Output: " + str(case[1]) + "\n")
    if result == case[1]:
        correct_count += 1

print("Score: " + str(correct_count) + "/" + str(len(testcases)))
