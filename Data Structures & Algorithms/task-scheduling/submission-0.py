"""
if there are no tasks:
    return 0
make an array of 26 zero counts
for each task:
    inrease that task's count

find the largest count 
count how many task types have that count

frame length = (largest count - 1) * (n + 1) + tied task types
return the larger of frame length and number of tasks

"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        counts = [0] * 26

        for task in tasks:
            task_index = ord(task) - ord('A')
            counts[task_index] += 1
        
        max_count = max(counts)
        num_max_tasks = 0
        for count in counts:
            if count == max_count:
                num_max_tasks += 1
        
        frame_length = (max_count - 1) * (n+1) + num_max_tasks
        return max(len(tasks), frame_length)