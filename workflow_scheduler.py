from collections import defaultdict, deque

class WorkflowScheduler:
    def __init__(self):
        self.tasks = defaultdict(dict)
        self.indegree = defaultdict(int)
        self.duration = {}
        
    def add_task(self, task, duration):
        self.tasks[task] = []
        self.duration[task] = duration
        
    def add_dependency(self, from_task, to_task):
        self.tasks[from_task].append(to_task)
        self.indegree[to_task] += 1

    def calculate_times(self):
        EST = defaultdict(int)
        EFT = {}
        LST = {}
        LFT = {}
        
        # Topological sort using Kahn's algorithm
        zero_indegree = deque([task for task in self.tasks if self.indegree[task] == 0])
        topological_order = []

        while zero_indegree:
            task = zero_indegree.popleft()
            topological_order.append(task)
            for neighbor in self.tasks[task]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    zero_indegree.append(neighbor)

        # Calculate EST and EFT
        for task in topological_order:
            EFT[task] = EST[task] + self.duration[task]
            for neighbor in self.tasks[task]:
                EST[neighbor] = max(EST[neighbor], EFT[task])

        # Calculate LFT and LST
        max_eft = max(EFT.values())
        for task in topological_order:
            LFT[task] = max_eft

        for task in reversed(topological_order):
            LST[task] = LFT[task] - self.duration[task]
            for neighbor in self.tasks[task]:
                LFT[task] = min(LFT[task], LST[neighbor])

        return max_eft, max(LFT.values())

# Example usage
scheduler = WorkflowScheduler()
scheduler.add_task('T_START', 0)
scheduler.add_task('A', 3)
scheduler.add_task('B', 2)
scheduler.add_task('C', 4)
scheduler.add_task('D', 2)

scheduler.add_dependency('T_START', 'A')
scheduler.add_dependency('A', 'B')
scheduler.add_dependency('A', 'C')
scheduler.add_dependency('B', 'D')
scheduler.add_dependency('C', 'D')

earliest_time, latest_time = scheduler.calculate_times()
print(f"Earliest time all tasks will be completed: {earliest_time}")
print(f"Latest time all tasks will be completed: {latest_time}")
