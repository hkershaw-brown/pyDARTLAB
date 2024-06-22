import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

def hide_negative_numbers(x, pos):
    """Hide negative numbers on an axis."""
    if x < 0:
        return ''
    return f'{x:.1f}'

class PosteriorStyle:
    linestyle = '-.'
    marker = 'g+'
    linecolor = 'g'

class PriorStyle:
    linestyle = '-'
    marker = 'b.'
    linecolor = 'b'
        
class ObservationStyle:
    linestyle = '--'
    marker = 'r*'
    linecolor = 'r'
    markersize = 12


class dartlabplot:
    # class-wide data

    def __init__(self, ax, x_limits):
        self.ax = ax
        self.x_limits = x_limits

    def plot_observation(self, mu, sigma):
        # Define the normal distribution parameters
        #mu = 5  # mean
        #sigma = 1  # standard deviation

        # Generate x values
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

        # Compute y values for the normal distribution
        y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
        self.ax.axhline(y=0, color='k', linestyle='-', linewidth=1)
        self.ax.set_xlim(self.x_limits)
        #ax.set_ylim(bottom=-0.1)  # this is also causing the top limit to be 1
        # Apply the custom formatter to the y-axis of ax3
        self.ax.yaxis.set_major_formatter(FuncFormatter(hide_negative_numbers))
        self.ax.plot(x,y, linestyle=ObservationStyle.linestyle, color=ObservationStyle.linecolor)
        self.ax.plot(mu, 0, ObservationStyle.marker, markersize=ObservationStyle.markersize)
        self.ax.set_xlabel('Observed Quantity')
        self.ax.set_ylabel('Observation Likelihood')

