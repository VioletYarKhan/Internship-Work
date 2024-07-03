import numpy as np
import matplotlib.pyplot as plt

Xs = 1
Xi = 0
Xr = 0
Xd = 0

all_values = [[Xs, Xi, Xr, Xd]]

# Defining translation matrix
translator = np.array([ [0.95, 0.04, 0, 0],
                        [0.05, 0.85, 0, 0],
                        [0.00, 0.10, 1, 0],
                        [0.00, 0.01, 0, 1]], dtype = 'float')

# Translation function
def translate(BXs, BXi, BXr, BXd):
    return(np.dot(translator, [BXs, BXi, BXr, BXd]))

def values_to_plot_input(valueList, cycles):
    plot_input_list = []
    for i in range(0, cycles + 1):
        for j in range(0, 4):
            plot_input_list.append(i)
            plot_input_list.append(valueList[i][j])
    return plot_input_list


times = int(input('How many cycles do you want to run? '))

for t in range (1, times + 1):
    Xs, Xi, Xr, Xd = translate(Xs, Xi, Xr, Xd)
    curr_values = [Xs, Xi, Xr, Xd]
    
    print(curr_values)
    all_values.append(curr_values)

plt.plot(all_values)

plt.show()