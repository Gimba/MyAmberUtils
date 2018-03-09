import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import matplotlib.mlab as mlab
from scipy.stats import norm

with open('all_out.dat', 'r') as f:
    content = f.read().splitlines()
    data = {}
    mutation = ""
    values = []
    for line in content:
        if line == 'TOTAL':
            if mutation:
                data[mutation] = values
                values = []
            mutation = last.strip("/")
        if line.strip("-")[0].isdigit():
            values.append(float(line))
        last = line
    data[mutation] = values

    n = 5
    variances = {}
    rngs = {}
    max_var = 0
    for key in data.keys():
        var = []
        rng = []
        for i in range(0, len(data[key]), n):
            values = data[key]
            variance = np.var(values[i:i + n])
            var.append(variance)
            if variance > max_var:
                max_var = variance
            r = np.ptp(values[i:i + n])
            rng.append(r)
        variances[key] = var
        rngs[key] = rng

    with open('all_out_var.dat','w') as f:
        for key in variances.keys():
            counter = 1
            maximum = 0
            for i in range(len(variances[key])):
                if variances[key][i] > maximum:
                    maximum = variances[key][i]
                    frame = counter
                counter += 1

            f.writelines(key + " " + str(frame) + " " + str(maximum))
            f.write("\n")



    num_plots = len(variances)

    if num_plots > 10:
        x = 3
        y = int(ceil(float(num_plots) / 3))
    else:
        x = 2
        y = num_plots / 2

    f, ax = plt.subplots(y, x, sharex='col', sharey='row', figsize=(20, 10))
    f.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.grid(False)
    plt.xlabel("variance values")
    plt.ylabel("frequency")
    f.tight_layout(rect=[0, 0.03, 1, 0.93])

    f.suptitle('Variances of energy values of trajectories involved in the calculation of ddG (back muta)', fontsize=20)
    subplots = []
    for i in range(y):
        for j in range(x):
            subplots.append(ax[i,j])

    for k in range(len(variances)):
        temp = variances.items()[k][1]
        n, bins, patches = subplots[k].hist(temp, 30, normed=1, facecolor='green', alpha=0.75)
        subplots[k].set_title(variances.keys()[k])
        subplots[k].set_ylim([0,0.1])
        subplots[k].set_xlim([0, max_var])

        # best fit of data
        (mu, sigma) = norm.fit(var)

        # add a 'best fit' line
        y = mlab.normpdf(bins, mu, sigma)
        l = subplots[k].plot(bins, y, 'r--', linewidth=1)

    plt.show()
