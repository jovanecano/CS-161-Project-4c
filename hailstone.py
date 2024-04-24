# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/23/2024
# Description: This function called hailstone takes a positive integer parameter as the initial number of a hailstone
# sequence and returns how many steps it takes to reach 1.

def hailstone(num):
    """This function will do the following:
    If the integer the user entered is even, then it will divide it by two to get the next integer in the sequence
    If it is odd, then it will multiply it by three and add one to get the next integer in the sequence.
    Then it will use the value generated to find the next value, according to the same rules.
    For example, if our initial number is 3, the subsequent numbers will be: 10, 5, 16, 8, 4, 2, 1."""
    steps = 0 # initializing the variable steps to count steps
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        steps += 1
    return steps

#answer = hailstone(3)
#print(answer)