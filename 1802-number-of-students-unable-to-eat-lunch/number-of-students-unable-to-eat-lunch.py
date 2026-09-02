from collections import Counter

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # Count preferences of all students
        count = Counter(students)
        
        for sandwich in sandwiches:
            # If no student left wants this top sandwich, the process terminates
            if count[sandwich] == 0:
                break
            # Otherwise, a student matching this preference will eventually take it
            count[sandwich] -= 1
            
        # The remaining unserved students is the sum of leftover preferences
        return count[0] + count[1]
