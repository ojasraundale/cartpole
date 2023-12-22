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

Following are the limits I chose for my environment. The simulation ends whenever the cartpole moves out of the limits or if more than 500 timestamps have crossed. 

| Num | Observation              | Min    | Max    |
| --- | ------------------------ | ------ | ------ |
| 0   | Cart Position            | -2.4   | 2.4    |
| 1   | Cart Velocity            | -Inf   | Inf    |
| 2   | Pole Angle               | $-\pi/15$ | $-\pi/15$ |
| 3   | Pole Angular Velocity    | -Inf   | Inf    |

### Action Space and State Update: 
The agent can take two actions: Left or Right. Each corresponds to either a force of -10 Newtons or +10 newtons. 
The game state updates at every 0.02 seconds ($\tau$). The particular physics are as follows: 

$x_{t+1} \gets x_t + \tau v_t $

$v_{t+1} \gets v_t + \tau  d $

$\omega_{t+1} \gets \omega_t + \tau  \dot \omega_t$

$\dot \omega_{t+1} \gets \dot \omega_t + \tau  c$

Where, 

$b = \frac{F + m_p l \dot\omega_t^2\sin(\omega_t)}{m_t}$

$c = \frac{g \sin(\omega_t) - cos(\omega_t) b}{l \Big( \frac{4}{3} - \frac{m_p \cos(\omega_t)^2}{m_t} \Big)}$

$d = b - \frac{m_p l c \cos(\omega_t)}{m_t}$



## Fourier State Vectors and the agent's policy
[Konidaris](https://people.cs.umass.edu/~pthomas/papers/Konidaris2011a.pdf)'s Fourier basis technique is used to construct state features out of the 4-length state vector. However we don't use it to approximate the value function but rather just use it to construct simple parametrized policies. 

The policy is simple linear function over the fourier state vectors. If the weighted sum is greater than zero then the action right is chosen, otherwise the action left is chosen. 

Fourier state vector $\phi(s)$: 

$\phi(s) = [1, \cos(1 \pi x), \cos(2 \pi x), \ldots, \cos(M \pi x), \cos(1 \pi v), \cos(2 \pi v), \ldots, \cos(M \pi v), \cos(1 \pi \omega), \cos(2 \pi \omega), \ldots, \cos(M \pi \omega), \cos(1 \pi \dot{\omega}), \cos(2 \pi \dot{\omega}), \ldots, \cos(M \pi \dot{\omega})]^\top.$

Where $M$ is the order of the fourier transform. 

A policy parameter $\theta$ is chosen. 

If $\phi(s)^\top \theta$ > 0: Action RIGHT is chosen. 

Else: Action LEFT is chosen



## Evolution Strategy for Black Box Optimization methods. 
[Salimans et al.](https://arxiv.org/abs/1703.03864)'s ES method was used to generate new policies and evaluate them. It starts with a policy $\theta_0 \in \mathbb{R}^n$ with random parameters as an initial \textit{guess}. It then repeatedly tweaks the guess a bit, randomly; and moves the current guess slightly towards whatever tweaks worked better. Concretely, at each episode $t$, the algorithm generates many (say *nPerturbations* $=20$) random-noise perturbation vectors $\epsilon_i$. These are then used to generate a population of perturbed policies, each of which is only slightly different than the current one. The parameters of each perturbed policy are $\theta_t + \sigma \epsilon_i$, where $\sigma$ is an exploration parameter. The algorithm evaluates each of the perturbed policies by running it in the environment $N$ times, using the function *estimate\_J*. This produces the corresponding policy performance evaluations, $J_i$. The updated policy parameter vector $\theta_{t+1}$, then, is the weighted sum of the *nPerturbations* random-noise vectors, where each weight is proportional to the performance $J_i$ of the corresponding perturbed policy. Thus the perturbed policies with higher performances have higher weights. 


## Usage

Need python on your machine to run this code. To run the program, simply run: 

``python Simulation.py``

Simulation.py's main function can be edited to change the hyperparameters. It makes a simple call: 
Simulation(M = 8, n_pert=200, sigma=0.2, alpha=0.002, n_episodes=1, iterations= 500)

where the arguments are the hyperparameters. 


## Results
Most of the experiments can be found in [Experiments.ipynb](/Experiments.ipynb). The following parameters gave the best resulting RL agent consitently:

$M = 8, n_{pert} = 200, \sigma = 1, \alpha = 0.01, N = 1$

Folling plot showcases this by running the training algorithm 20 times and plotting the standard deviation:

![Plot](<nruns 20 M 8, n_pert 200, sigma 1, alpha 0.01.jpg>)


I also found an agent with just $M = 1$ that ran for more than 10 million timestamps. Following are the $\theta$ parameters: 

$[-0.06380776, -0.48614546,  1.04039523, -1.76673265, -1.13802136]$


## Further Work
I plan to make a game that visually showcases the simulation and the best agent I found. Even humans could play this version of the cartpole and compare their performance with the best found AI. 
