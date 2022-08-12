#
# ps1pr2.py - Problem Set 1, Problem 2
#
# Indexing and slicing puzzles
#
# This is an individual-only problem that you must complete on your own.
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:] 

# Solve puzzles 1-4 here:

answer1 = e[:2]

answer2 = pi[-2::-2]

answer3 = pi[:5:4] + [e[1]]

answer4 = e[-1::-2] + pi[0:5:2]

#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]

# Solve puzzles 5-10 here:

answer6 = u[:7] + t[1]
answer7 = u[5] + b[1:4] + t[1:3]
answer8 = b[0:2]+ u[2] + b[2:4] + t[1:3] + b[1] + u[:7:6]
answer9 = (u[9] + u[4:7:2])*3
answer10 = u[-2:-9:-3] + b[2:4]




# test code below, do not modify!
if __name__ == '__main__':

    for x in ['answer0', 'answer1', 'answer2', 'answer3', 'answer4',
              'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
              'answer10']:
        if x in dir():
            print(x + ' = ', eval(x))


