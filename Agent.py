import numpy as np
import random
import CartPole
from CartPole import RIGHT, LEFT    # Importing Actions
# import keyboard

class Agent():
    """
    Class containing the Agent
    Arguments: 
    M: number of fourier basis. There will 4M + 1 features for M basis
    """
    
    def __init__(self, M, theta = None) -> None:
        self.M = M
        
        if theta is not None:
            self.theta = theta
        else:
            self.theta = np.zeros(4*M + 1)
            
        return
    
    def randomize_theta(self):
        self.theta = np.random.normal(size=4*self.M+1)
        return

        
    def set_theta(self, theta):
        self.theta = theta

    
    def get_theta(self):
        return self.theta

        
    def get_action_alternate_left_rights(self, t_step):
        if t_step % 2:
            return LEFT
        return RIGHT

    
    def get_action_left(self):
        return LEFT

    
    def get_action_right(self):
        return RIGHT

    def get_action(self, phi):
        """Function to return action by taking the dot product of theta and phi""" 
        # print(f"Shape of phi: {phi.shape}, shape of theta {self.theta.shape}")
        threshold = np.dot(phi, self.theta)
        if threshold <= 0:
            return LEFT
        else:
            return RIGHT 

        
    # def get_keyboard_action():
    #     pass

        
def main():
    
    # agent = Agent()
    # while(True):
    #     agent.get_keyboard_action()
    
    print(np.random.normal(size=(10)))
    return

if __name__ == "__main__":
    main()
