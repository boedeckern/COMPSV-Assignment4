"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    for i in product_ids:
        product_ids.remove(i)
        count=0
        while count<len(product_ids):
            if product_ids[count]==i:
                return True
            count+=1
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self.front=None
        self.rear=None

    def add_task(self, task):
        new_node=Node(task)
        if not self.front:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node=self.front
        self.front=self.front.next
        if not self.front:
            self.rear=None
        return removed_node.value


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.table={}
        self.count=0

    def add(self, value):
        if value not in self.table:
            self.count+=1
        self.table.add(value)

    def get_unique_count(self):
        return self.count
