
import numpy as np
import random

maze = np.array([
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
])

start = (0, 0)
goal = (3, 3)

actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = np.zeros((4, 4, 4))

alpha = 0.8 
gamma = 0.9  
epsilon = 0.2 
for episode in range(1000):
    state = start

    for step in range(100):

        if random.random() < epsilon:
            a = random.randint(0, 3)
        else:
            a = np.argmax(q[state])

        r = state[0] + actions[a][0]
        c = state[1] + actions[a][1]

        if r < 0 or r >= 4 or c < 0 or c >= 4 or maze[r, c] == 1:
            reward = -10
            next_state = state
        else:
            next_state = (r, c)
            reward = 100 if next_state == goal else -1

        q[state][a] += alpha * (
            reward + gamma * np.max(q[next_state]) - q[state][a]
        )

        state = next_state

        if state == goal:
            break

state = start
path = [state]

for _ in range(30):
    if state == goal:
        break

    a = np.argmax(q[state])
    r = state[0] + actions[a][0]
    c = state[1] + actions[a][1]

    if r < 0 or r >= 4 or c < 0 or c >= 4 or maze[r, c] == 1:
        break

    state = (r, c)
    path.append(state)

print("Learned Path:", path)
print("Goal Reached!" if state == goal else "Goal Not Reached!")
