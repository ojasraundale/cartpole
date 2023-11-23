# cartpole
Implementation of Black Box Optimization methods on the Cartpole Domain


Need python on your machine to run this code.

To run the program, enter the following commands: 

$python Simulation.py 

Simulation.py's main function can be edited to change the hyperparameters. It makes a simple call: 
Simulation(M = 8, n_pert=200, sigma=0.2, alpha=0.002, n_episodes=1, iterations= 500)

where the arguments are the hyperparameters. 


CartPole.py implements a class to simulate the CartPole environment. 
Agent.py implements the policy and gets an action based on theta values. It has other custom actions as well. 
Simulation.py runs the episodes, J_estimates, and the ES algorithm
