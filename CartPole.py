import numpy as np
import random

RIGHT = 10
LEFT = -10


class CartPole:
    """
    Class containing the CartPole Environment
    
    Arguments: 
    M: number of fourier basis. 
    fourier_type: 0 for cosine based, 1 for sine based
    """
    
    def __init__(self, M=0, fourier_type = 0) -> None:
        
        # Intitializing Environment Variables
        self.g = 9.8                            # Gravity
        self.m_c = 1.0                          # Cart's mass
        self.m_p = 0.1                          # Pole's mass
        self.m_t = self.m_c + self.m_p          # Total mass
        self.l = 0.5                            # Pole's length
        self.t = 0                              # Current time in seconds
        self.t_delta = 0.02                     # Time delta update (States updated every 0.02 seconds)
        self.t_step = 0                         # Current step
        
        # State Variables intialized to 0
        self.x = 0                              # Cart Position; Out of bounds when not : -2.4 <= x <= 2.4
        self.v = 0                              # Velocity of the cart
        self.w = 0                              # Cart Angle wrt vertical; Out of bounds when not: -pi/12 <= w <= pi/12
        self.w_dot = 0                          # Angular velocity of the pole

        # Initializing the state fourier basis vector
        self.M = M
        self.fourier_type = fourier_type
        self.phi = np.zeros(4*M + 1)            # Creating phi(s) of size 4M + 1. 
        self.update_phi()
        return

    
    def reset_state_to_start_position(self):
        self.__init__(self.M, self.fourier_type)
        
    def update_phi(self):
        # Fourier Type = 0; Cos based fourier Basis
        # Normalizing between 0 and 1
        x_norm = (self.x + 2.4)/4.8
        v_norm = (self.v + 1.8)/3.6                           # Max v I found is 1.760381125768309
        w_norm = (self.w + np.pi/12) / (np.pi/6)
        w_dot_norm = (self.w_dot + 2.8)/ 5.6                  # Max w_dot I found is 2.777886494012814
        
        # (1pi, 2pi, 3pi, 4pi, ...., M)
        pi_series = np.array([n*np.pi for n in range(1, self.M+1)])
        
        # Fourier Basis: 
        # cos(i * pi * var) for i in (1 to M), var in [x_norm, v_norm, w_norm, w_dot_norm]
        x_series        = np.cos(pi_series * x_norm)
        v_series        = np.cos(pi_series * v_norm)
        w_series        = np.cos(pi_series * w_norm)
        w_dot_series    = np.cos(pi_series * w_dot_norm)
        
        # Appending the fourier bases
        fourier_series = np.concatenate(
            (
                np.array([1]),
                x_series,
                v_series, 
                w_series,
                w_dot_series
            ))
        
        # TODO Sin based fourier basis
        
        self.phi = fourier_series   
        # print(f"Fourier Series Shape = {fourier_series.shape}") 
        return
        
    
    def intermediate_variables(self, action):
        b = (action + self.m_p * self.l * self.w_dot**2 * np.sin(self.w)) \
            / \
            self.m_t
        
        c = (self.g * np.sin(self.w) - b * np.cos(self.w)) \
            / \
            (self.l * (4/3 - (self.m_p * np.cos(self.w)**2)/self.m_t))
        
        d = b - (self.m_p * self.l * c * np.cos(self.w))/self.m_t
        
        return b,c,d
    
    
    def return_next_state(self, action):
        b, c, d = self.intermediate_variables(action=action)
        
        x = self.x + (self.t_delta * self.v)
        v = self.v + (self.t_delta * d)
        w = self.w + (self.t_delta * self.w_dot)
        w_dot = self.w_dot + (self.t_delta * c)
        
        return x, v, w, w_dot
    
    
    def update_state_and_return_reward(self, action):
        x, v, w, w_dot = self.return_next_state(action=action)
        self.x = x
        self.v = v
        self.w = w
        self.w_dot = w_dot
        self.t = self.t + self.t_delta
        self.t_step+= 1
        self.update_phi()
        
        if self.CheckValidity():
            return 1
        else:
            return 0
    
        
    def CheckValidity(self):
        if(self.x < -2.4 or self.x > 2.4):
            return False
        if(self.w < -np.pi/15 or self.w > np.pi/15):
            return False
        # if(self.t/self.t_delta > 500):
        #     return False
        
        return True
    
    
    def get_state(self):
        return self.x, self.v, self.w, self.w_dot
    
    
    def get_state_features(self):
        return self.phi
    

def main():
    # print("ehllow")
    # print(np.sin(np.pi/2))
    
    cartpole = CartPole(2)
    print(cartpole.M)
    
    print(cartpole.phi)
    print(f"Phi shape = {cartpole.phi.shape}")
    
    # print(np.cos(np.zeros(shape=4*1+1)))
    # pi_series = np.array([i*np.pi for i in range(5)])
    
    # x = 1.5
    # y = 1.5
    # print(pi_series)
    # print(np.append(np.cos(pi_series + x) , np.cos(np.pi - pi_series - x) ))


    # print([i for i in range(1,11)])

if __name__ == "__main__":
    main()