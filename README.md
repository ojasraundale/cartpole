# cartpole
Implementation of Black Box Optimization methods and using Fourier State Vectors on the Cartpole Domain. 

## About the domain
This a classic Reinforcement Learning domain. [Gymnasium](https://gymnasium.farama.org/ "Gymnasium's Homepage") already provides an excellent API for running environments. However I decided to create my own environment on Python for the purpose of the algorithm's implementation, just because it was fun! [CartPole.py](/CartPole.py) has my own implementation of the Cartpole environment. 

## Fourier State Vectors
The state of a cartpole environment is determined by 4 state vectors: $x$ (Cart Position), $v$ (Cart Velocity), $w$ (Pole Angle w.r.t to vertical), $\dot$ $\omega$ ()



Need python on your machine to run this code.

To run the program, enter the following commands: 

``python Simulation.py``

Simulation.py's main function can be edited to change the hyperparameters. It makes a simple call: 
Simulation(M = 8, n_pert=200, sigma=0.2, alpha=0.002, n_episodes=1, iterations= 500)

where the arguments are the hyperparameters. 


CartPole.py implements a class to simulate the CartPole environment. 
Agent.py implements the policy and gets an action based on theta values. It has other custom actions as well. 
Simulation.py runs the episodes, J_estimates, and the ES algorithm
