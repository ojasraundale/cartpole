# cartpole
Implementation of Black Box Optimization methods and using Fourier State Vectors on the Cartpole Domain. 

## About the domain
This a classic Reinforcement Learning domain. [Gymnasium](https://gymnasium.farama.org/ "Gymnasium's Homepage") already provides an excellent API for running environments. However I decided to create my own environment on Python for the purpose of the algorithm's implementation, just because it was fun! [CartPole.py](/CartPole.py) has my own implementation of the Cartpole environment. 


## Cartpole Environement

### State Space of Cartpole
The state of a cartpole environment is determined by 4-length state vectors: 

$x$ (Cart Position), 

$v$ (Cart Velocity), 

$\omega$ (Pole Angle w.r.t to vertical), 

$\dot \omega$ (Angular velocity of the pole). 

Following are the limits I chose for my environment. The simulation ends whenever the cartpole moves out of the limits. 

| Num | Observation              | Min    | Max    |
| --- | ------------------------ | ------ | ------ |
| 0   | Cart Position            | -2.4   | 2.4    |
| 1   | Cart Velocity            | -Inf   | Inf    |
| 2   | Pole Angle               | $-\pi/15$ | $-\pi/15$ |
| 3   | Pole Angular Velocity    | -Inf   | Inf    |

### Action Space and State Update: 
The agent can take two actions: Left or Right. Each corresponds to either a force of -10 Newtons or +10 newtons. 
The game state updates at every 0.02 seconds. The particular physics are as follows: 

$x_{t+1} \gets x_t + \tau v_t $

$v_{t+1} \gets v_t + \tau \, d $

$\omega_{t+1} \gets \omega_t + \tau \, \dot \omega_t$

$\dot \omega_{t+1} \gets \dot \omega_t + \tau \, c$

Where, 
$b = \frac{F + m_p\,l\,\dot\omega_t^2\sin(\omega_t)}{m_t} \\$
$c = \frac{g\,\sin(\omega_t) - cos(\omega_t)\,b}{l \Big( \frac{4}{3} - \frac{m_p\,\cos(\omega_t)^2}{m_t} \Big)} \\$
$d = b - \frac{m_p \, l \, c \, \cos(\omega_t)}{m_t}$





## Fourier State Vectors and the agent
The 4-length 






Need python on your machine to run this code.

To run the program, enter the following commands: 

``python Simulation.py``

Simulation.py's main function can be edited to change the hyperparameters. It makes a simple call: 
Simulation(M = 8, n_pert=200, sigma=0.2, alpha=0.002, n_episodes=1, iterations= 500)

where the arguments are the hyperparameters. 


CartPole.py implements a class to simulate the CartPole environment. 
Agent.py implements the policy and gets an action based on theta values. It has other custom actions as well. 
Simulation.py runs the episodes, J_estimates, and the ES algorithm
