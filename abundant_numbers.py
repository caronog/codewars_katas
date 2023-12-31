"""
In number theory, an abundant number or an excessive number is one for which the sum of it's proper divisors is greater
than the number itself. The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a
total of 16. The amount by which the sum exceeds the number is the abundance. The number 12 has an abundance of 4, for
example. Other initial abundant numbers are : 12, 18, 20, 24, 30, 36, 40, 42, 48, 54 etc .
Infinitely many odd and even abundant numbers exist.
As you should have guessed by now, in this kata your function will take a positive integer h as range input and return
a nested array/list that will contain the following information:

    Highest available odd or even abundant number in that range
    Its abundance

Examples
abundant(15)  = [[12], [4]]
abundant(19)  = [[18], [3]]
abundant(100) = [[100], [17]]
abundant(999) = [[996], [360]]

Tips

The problem involves some pretty big random numbers. So try to optimize your code for performance as far as you can.
And yes, the input argument will always be positive integers. So no need to check there.
"""

# SOLUTION #

def abundant(h):
    while sum([n for n in range(1, h) if h % n == 0]) < h:
        h -= 1
  
    return [[h], [sum([n for n in range(1, h) if h % n == 0]) - h]]

"""
For some reason, when I try to assign sum([n for n in range(1, h) if h % n == 0]) to a variable,
the code doesn't work the same way.
"""
