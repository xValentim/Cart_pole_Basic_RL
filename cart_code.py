import gym
import numpy as np

env = gym.make("CartPole-v0")

def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1

totals = []
time = []
t = 0
for episode in range(500):
    episode_rewards = 0
    obs = env.reset()
    for step in range(1000):
        action = basic_policy(obs)
        obs, reward, done, info = env.step(action)
        episode_rewards += reward
        if done:
            break
        env.render()
    print(episode_rewards)
    t += 1
    time.append(t)
    totals.append(episode_rewards)
print(np.mean(totals), np.std(totals), np.min(totals), np.max(totals))


