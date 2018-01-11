# ---------------------------------------------
# ---------------------------------------------
# Author: Brian Cubero
# Date:   2018-01-10 20:07:41
# Last Modified by:   cubero.bv
# Last Modified time: 2018-01-10 20:31:55
# ---------------------------------------------
# ---------------------------------------------

import gym

env = gym.make('CartPole-v0')

print('INITIAL OBSERVATIONS:')
observation = env.reset()
print(observation)

for t in range(2):

    env.render()

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    cart_pos, cart_vel, pole_ang, ang_vel = observation

    if pole_ang > 0:
        action = 1
    else:
        action = 0

    observation, reward, done, info = env.step(action)

    print('\n\nobservation', observation, '\n')
    print('reward', reward, '\n')
    print('done', done, '\n')
    print('info', info, '\n')
