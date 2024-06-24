import numpy as np

class Lorenz96:

    def __init__(self, model_size):
        self.model_size = model_size

    def step(self, x, forcing, delta_t):
        """
        Does a single time step advance for Lorenz 96 40-variable model using four-step Runge-Kutta time step.
        
        Parameters:
        - x: The model_size state.
        - forcing: The forcing term.
        - delta_t: The time step.
        
        Returns:
        - x_new: The new state vector after the time step.
        """

        # Compute the four steps of the Runge-Kutta method using numpy operations
        dx = self.comp_dt(x, forcing)
        x1 = delta_t * dx
        inter = x + x1 / 2
        
        dx = self.comp_dt(inter, forcing)
        x2 = delta_t * dx
        inter = x + x2 / 2

        dx = self.comp_dt(inter, forcing)
        x3 = delta_t * dx
        inter = x + x3

        dx = self.comp_dt(inter, forcing)
        x4 = delta_t * dx

        x_new = x + x1/6 + x2/3 + x3/3 + x4/6

        return x_new


    def comp_dt(self, x, forcing):
        """
        Computes the derivative of the state vector using numpy operations for efficiency.
        
        Parameters:
        - x: The state vector.
        - forcing: The forcing term.
        
        Returns:
        - dt: The derivative of the state vector.
        """
        dt = np.zeros(self.model_size)
        for j in range(self.model_size):
            jp1 = (j + 1) % self.model_size
            jm2 = (j - 2) % self.model_size
            jm1 = (j - 1) % self.model_size
            dt[j] = (x[jp1] - x[jm2]) * x[jm1] - x[j] + forcing
        return dt