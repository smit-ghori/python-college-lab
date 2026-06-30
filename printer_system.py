# Priority-Based Printer Queue System

# Design and implement a Printer Queue Management System using Python's collections.deque. The system should manage print jobs based on their priority.

# The printer maintains two separate queues:
# Urgent Queue for high-priority print jobs.
# Normal Queue for regular print jobs.
# Users can add print jobs by specifying the job name and its priority.
# When printing, the printer should always process urgent jobs first.
# If there are no urgent jobs, it should print jobs from the normal queue.
# The system should follow the FIFO (First-In, First-Out) principle for each queue.
# Objective


from collections import deque

class Printer:

    def __init__(self, total_prints=5):
        self.urgent_queue = deque(maxlen=total_prints)
        self.normal_queue = deque(maxlen=total_prints)
        self.total_prints = total_prints

    def printing(self, job, priority="normal"):
        if priority == "urgent":
            if len(self.urgent_queue) < self.total_prints:
                self.urgent_queue.append(job)
        else:
            if len(self.normal_queue) < self.total_prints:
                self.normal_queue.append(job)

    def next_print(self):
        if self.urgent_queue:
            print("Urgent:", self.urgent_queue.popleft())
        elif self.normal_queue:
            print("Normal:", self.normal_queue.popleft())
        else:
            print("No print jobs available.")


no_of_prints = int(input("Enter no of prints: "))

p = Printer(no_of_prints)

for i in range(1, no_of_prints + 1):
    job = input(f"Enter job{i}: ")
    priority = input("Enter priority: ")
    p.printing(job=job, priority=priority)

print("\n\n--------Print the copy-----")
for i in range(1, no_of_prints + 1):
    enter = input("")
    p.next_print()
