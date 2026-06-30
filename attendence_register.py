# Imagine a class with 30 students. The teacher maintains an attendance register where each roll number has a fixed position.

# Roll No. 1 → Index 0

# Roll No. 2 → Index 1

# ...

# Roll No. 30 → Index 29

# Since every student has a fixed slot (index), the teacher can directly go to any student's attendance without checking the previous records.

# For example,

# If the teacher wants to mark the attendance of Roll No. 16, they can directly access Index 15. There is no need to search from Roll No. 1 to Roll No. 16. This is called direct (random) access, which is the most important feature of an array.


class Attendance:
    
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students
        self.register = []
    
    def fill_attendance(self, presents_numbers):
        self.register = ["P" if i in presents_numbers else "A" for i in range(1, self.no_of_students+1)]

    def get_attendance(self):
        return self.register
    
present_roll = [2, 4, 13, 22, 10]
total_students = 30

a = Attendance(total_students)
a.fill_attendance(present_roll)
print(a.get_attendance())