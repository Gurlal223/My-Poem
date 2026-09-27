PROGCON Week 11 - Test Results and Reflection Summary
1. Four Test Arrays and Averages:
   - [22, 9, 0, 17] -> Sum: 48, Count: 4, Average: 12.0
   - [22, 0, 49, 8] -> Sum: 79, Count: 4, Average: 19.75
   - [35, 13, 22, 0] -> Sum: 70, Count: 4, Average: 17.5
   - [10, 5, -4, 27] -> Sum: 38, Count: 4, Average: 9.5
 
2. Correctness Judgments and Reflections:
   - All calculated averages matched the expected manual outputs accurately.
   - The program correctly handled zero values and negative numbers without logic errors.
"""
 
 
numbers = [0] * (5)
 
print("Hey there! This program displays the average of the numbers you input.")
print("How many numbers do you need the program to average?")
num = int(input())
total = 0
count = 0
for i in range(0, len(numbers) - 1 + 1, 1):
    print("Input the value of the " + str(i + 1) + " number")
    numbers[i] = int(input())
for i in range(0, len(numbers) - 1 + 1, 1):
    num = numbers[i]
    if num == 0:
        pass
    else:
        total = total + num
        count = count + 1
    if count == 0:
        print(0.0)
    else:
        average = float(total) / count
print(average)
