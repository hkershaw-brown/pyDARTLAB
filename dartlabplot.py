import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button
from dataclasses import dataclass

def hide_negative_numbers(x, pos):
    """Hide negative numbers on an axis."""
    if x < 0:
        return ''
    return f'{x:.2f}'
@dataclass
class PosteriorStyle:
    linestyle: str = '-.'
    marker: str = 'g+'
    linecolor: str = 'g'

@dataclass
class PriorStyle:
    linestyle: str = '-'
    marker: str = 'b.'
    linecolor: str = 'b'
        
@dataclass
class ObservationStyle:
    linestyle: str = '--'
    marker: str = 'r*'
    linecolor: str = 'r'
    markersize: int = 12

class dartlabplot:

    def __init__(self, ax, x_limits):
        self.ax = ax
        #self.fig = fig # do you want the figure?
        self.x_limits = x_limits # Helen do you want this?
        self.current_filter_selection = 'EAKF'

    def plot_observation(self, mu, sigma):
        # Define the normal distribution parameters
        #mu = 5  # mean
        #sigma = 1  # standard deviation

        # Generate x values
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

        # Compute y values for the normal distribution
        y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # plot
        self.ax.axhline(y=0, color='k', linestyle='-', linewidth=1)
        self.ax.set_xlim(self.x_limits)
        self.ax.yaxis.set_major_formatter(FuncFormatter(hide_negative_numbers))
        self.ax.plot(x,y, linestyle=ObservationStyle.linestyle, color=ObservationStyle.linecolor)
        self.ax.plot(mu, 0, ObservationStyle.marker, markersize=ObservationStyle.markersize)
        self.ax.set_xlabel('Observed Quantity')
        self.ax.set_ylabel('Observation Likelihood')


    def add_filter_options(self, position): # [left, bottom, width, height]
        # Check if position is a list and has exactly four elements
        if not isinstance(position, list) or len(position) != 4:
            raise ValueError("position must be a four-element list")

        self.radio_ax = plt.axes(position) 
        self.radio = RadioButtons(self.radio_ax, ('EAKF', 'EnKF', 'RHF'))

        #self.radio_conn_id = radio.on_clicked(self.handle_radio)
        self.radio_conn_id = self.radio.on_clicked(self.handle_radio)
        print('adding to event connections', self.radio_conn_id)
   
    def handle_radio(self, label):
        self.current_filter_selection = label
        if label == 'EAKF':
            # Handle Option 1
            print("EAKF selected")
        elif label == 'EnKF':
            # Handle Option 2
            print("EnKF selected")
        elif label == 'RHF':
            # Handle Option 3
            print("RHF selected")
        plt.draw()  # Update the plot if necessary

    def add_update_button(self, position): # [left, bottom, width, height]
        # Check if position is a list and has exactly four elements
        if not isinstance(position, list) or len(position) != 4:
            raise ValueError("position must be a four-element list")

        self.button_ax = plt.axes(position)
        self.button = Button(self.button_ax, 'Update Ensemble', color='lightblue', hovercolor='0.975')
        self.add_update_button_conn_id = self.button.on_clicked(self.update_ensemble)
        print('adding to event connections', self.add_update_button_conn_id)
        
    def update_ensemble(self, event):
        print("does nothing")
        
            