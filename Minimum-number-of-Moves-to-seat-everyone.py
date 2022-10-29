# Problem Description: Make the students sit in the seats closest to their positions.

# Input: seats = [3,1,5], students = [2,7,4]
# Output: 4
# Explanation: The students are moved as follows:
# - The first student is moved from from position 2 to position 1 using 1 move.
# - The second student is moved from from position 7 to position 5 using 2 moves.
# - The third student is moved from from position 4 to position 3 using 1 move.
# In total, 1 + 2 + 1 = 4 moves were used.

def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    return sum([abs(i-j) for i,j in zip(seats, students)])

print(minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6]))

