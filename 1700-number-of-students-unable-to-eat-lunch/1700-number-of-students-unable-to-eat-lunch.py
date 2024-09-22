class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = 0
        
        while c < 2*len(students):
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                c = 0
            else:
                students.append(students.pop(0))
            
            c += 1
        return len(sandwiches)