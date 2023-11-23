import numpy as np
import random
import CartPole
from CartPole import CartPole
from Agent import Agent
from CartPole import RIGHT, LEFT    # Importing Actions

        
def runEpisode(cartpole: CartPole, agent: Agent):   
    G = 0
    while(True):
        print(f"t = {cartpole.t}, states = {cartpole.get_state()}")
        phi = cartpole.get_state_features()
        action = agent.get_action(phi)
        r = cartpole.update_state_and_return_reward(action=action)
        G += r
        if(r == 0) : break
        
    # print(f"End state; t = {cartpole.t_step}, states = {cartpole.get_state()}; ")
    # print(cartpole.phi)
    # print()
    return G
    

def estimate_J(n_episodes, cartpole: CartPole, agent: Agent):
    # Gs = []
    # for i_episode in range(n_episodes):
    #     cartpole.reset_state_to_start_position()
    #     Gs.append(runEpisode(cartpole, agent))
    # return np.sum(Gs)/n_episodes
    
    G_sum = 0.
    for i_episode in range(n_episodes):
        cartpole.reset_state_to_start_position()
        G_sum += runEpisode(cartpole, agent)
    return G_sum/n_episodes

        
def EvolutionStrategy(cartpole:CartPole, agent:Agent, n_pert, sigma, alpha, n_episodes = 1, iterations = 500):
    """
    Funtion for Running the Evolution Strategy algorithm
    
    Attributes
    ---------- 
    cartpole: CartPole object for the environment.
    agent: Agent object that returns an action based on a policy
    n_pert: No. of perturbation/random thetas generated from sigma * N(0,1) noise
    sigma: Noise factor to generate perturbations
    alpha: Step size
    n_episodes: No. of episodes that a particular policy is run for to Estimate J
    iterations: Max no. of epochs the algorithm will be run for
    """
    intial_theta = agent.get_theta()
    theta_size = intial_theta.shape[0]
    # print(f"Theta size: {theta_size}")
    
    theta_t = intial_theta
    history = []
    for t in range(iterations):
        Js = []
        epsilons = []
        for i_pert in range(n_pert):
            epsilon = np.random.normal(size=(theta_size))
            # print(f"Epsilon shape : {epsilon.shape}")
            # print(f"Theta shape : {theta_t.shape}")
            
            agent.set_theta(theta_t + sigma*epsilon)            # theta_t = theta_t + sigma*epsilon
            J = estimate_J(n_episodes=n_episodes, cartpole=cartpole, agent=agent)
            epsilons.append(epsilon)
            Js.append(J)
        
        # J_np = np.array([Js])
        # epsilon_np = np.array(epsilons)
        # weighted_sum_epsilon = np.matmul(J_np, epsilon_np)
        
        # J_normalized = np.array(Js)                 # Normalizing weights by mean and standard deviation of Js from the perturbations
        # J_normalized = (J_normalized-J_normalized.mean())/J_normalized.std()
        
        weighted_sum_epsilon = np.zeros(theta_size)
        for J,epsilon in zip(Js, epsilons):
        # for J,epsilon in zip(J_normalized, epsilons): # Use this one for normalized weights
            weighted_sum_epsilon += J*epsilon
        
        # print("Weighted Sum Epsilon:")
        # print(weighted_sum_epsilon)
        # print("Theta t-1:")
        # print(theta_t)
        theta_t = (theta_t + ((alpha/(sigma*n_pert)) * weighted_sum_epsilon)).flatten()
        agent.set_theta(theta=theta_t)
        # print("Theta t:")
        # print(theta_t)
        current_J = estimate_J(1, cartpole, agent)
        history.append((t, current_J))
        print(f"Time {t}; J:{current_J}")
        
        if(current_J > 499):
            break
        
        
        # if(current_J==500): return theta_t
    # print(f"J_numpy, epsilon_numpy shape : {J_np.shape, epsilon_np.shape}")
    # print(f"J * epsilons shape : {np.matmul(J_np, epsilon_np).shape}")
    # for 
    return history, theta_t
    
    
    
def Simulation(M, n_pert, sigma, alpha, n_episodes, iterations):
    cartpole = CartPole(M=M, fourier_type=0)        # Creating a object containing the cartpole environment
    agent = Agent(M = M)                            # Agent object
    agent.randomize_theta()                         # Initializing theta from theta_i : N(0,1)
    
    # Best Theta ever! More than 10000000 timestamps!
    # agent.set_theta([-0.06380776, -0.48614546,  1.04039523, -1.76673265, -1.13802136])
    # print(runEpisode(cartpole, agent))
    # return
    history, theta_t = EvolutionStrategy(
        cartpole=cartpole, 
        agent=agent, 
        n_pert=n_pert, 
        sigma=sigma, 
        alpha=alpha, 
        n_episodes=n_episodes, 
        iterations= iterations)
    
    return history,theta_t
    # agent.set_theta(theta_t)
    # print(agent.get_theta())
    # print(cartpole.get_state_features())
    # print(cartpole.get_state())
    
    
    # print(estimate_J(10, cartpole, agent))
    
    # print(np.random.normal(size=(1,17)))
    
    # print(np.random.normal(size=(1,17)).flatten())
    
# [-0.04116622,  0.1994668 , -0.28223446, -1.17767137, -1.45150265], M = 1
# [-0.09634053, -0.14896964,  0.17174984, -2.02189797, -1.80340843]
# [-0.06380776, -0.48614546,  1.04039523, -1.76673265, -1.13802136] M = 1, More than 10000000 timestamps


def BestAgent():
    M = 1
    cartpole = CartPole(M=M, fourier_type=0)        # Creating a object containing the cartpole environment
    agent = Agent(M = M)                            # Agent object
    # agent.randomize_theta()                         # Initializing theta from theta_i : N(0,1)
    
    # Best Theta ever! More than 10000000 timestamps!
    agent.set_theta([-0.06380776, -0.48614546,  1.04039523, -1.76673265, -1.13802136])
    print(runEpisode(cartpole, agent))
    
if __name__ == "__main__":
    # Simulation(M = 8, n_pert=200, sigma=0.2, alpha=0.002, n_episodes=1, iterations= 500)
    # print(Simulation(M = 8, n_pert=5, sigma=1, alpha=0.1, n_episodes=1, iterations= 500)[1])
    BestAgent()

    
