# Workflow Scheduler and Friends Network

## Table of Contents
1. [Introduction](#introduction)
2. [Workflow Scheduler](#workflow-scheduler)
   - [Overview](#overview)
   - [Usage](#usage)
   - [Example](#example)
3. [Friends Network](#friends-network)
   - [Overview](#overview)
   - [Usage](#usage)
   - [Example](#example)
4. [Setup](#setup)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
This repository contains two Python programs:
1. **Workflow Scheduler**: A program to schedule tasks with dependencies and calculate the earliest and latest completion times.
2. **Friends Network**: A program to find common friends and nth-level connections in a social network.

## Workflow Scheduler

### Overview
The Workflow Scheduler program helps in managing a complex workflow of tasks, determining the earliest and latest times by which all tasks can be completed. Each task has dependencies and a duration.

### Usage
1. **Add tasks** with their durations.
2. **Add dependencies** between tasks.
3. **Calculate the earliest and latest completion times** for all tasks.

### Example
```python
from workflow_scheduler import WorkflowScheduler

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



Here's a README file that you can use for your GitHub repository. This README covers both workflow_scheduler.py and friends_network.py programs, explaining their purpose, usage, and examples.

README.md
markdown
Copy code
# Workflow Scheduler and Friends Network

## Table of Contents
1. [Introduction](#introduction)
2. [Workflow Scheduler](#workflow-scheduler)
   - [Overview](#overview)
   - [Usage](#usage)
   - [Example](#example)
3. [Friends Network](#friends-network)
   - [Overview](#overview)
   - [Usage](#usage)
   - [Example](#example)
4. [Setup](#setup)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
This repository contains two Python programs:
1. **Workflow Scheduler**: A program to schedule tasks with dependencies and calculate the earliest and latest completion times.
2. **Friends Network**: A program to find common friends and nth-level connections in a social network.

## Workflow Scheduler

### Overview
The Workflow Scheduler program helps in managing a complex workflow of tasks, determining the earliest and latest times by which all tasks can be completed. Each task has dependencies and a duration.

### Usage
1. **Add tasks** with their durations.
2. **Add dependencies** between tasks.
3. **Calculate the earliest and latest completion times** for all tasks.

### Example
```python
from workflow_scheduler import WorkflowScheduler

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
Friends Network
Overview
The Friends Network program manages a social network, allowing you to find common friends between two people and determine the nth-level connection between two people.

Usage
Add friendships between people.
Find common friends between two people.
Find nth-level connection between two people
from friends_network import FriendsNetwork

network = FriendsNetwork()
network.add_friendship('Alice', 'Bob')
network.add_friendship('Bob', 'Janice')
network.add_friendship('Alice', 'Carol')
network.add_friendship('Carol', 'Dan')

common = network.common_friends('Alice', 'Bob')
nth_connection = network.nth_connection('Alice', 'Janice')

print(f"Common friends of Alice and Bob: {common}")
print(f"Nth connection between Alice and Janice: {nth_connection}")

