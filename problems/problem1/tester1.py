from answer1 import Solution

reverse = Solution().reverse

testcases = [(123, 321), (-123, -321), (120, 21)]

print("Running Unit Tests for Problem 1:\n")

correct_count = 0

for case in testcases:
    result = reverse(case[0])
    print("Input: " + str(case[0]))
    print("Output: " + str(result))
    print("Expected Output: " + str(case[1]) + "\n")
    if result == case[1]:
        correct_count += 1

print("Score: " + str(correct_count) + "/" + str(len(testcases)))
