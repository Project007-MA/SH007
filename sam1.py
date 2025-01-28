from matplotlib import pyplot as plt
from save_load import *
def res_plot4():

    epochs = range(1, 15)
    a=[0.81,0.7,0.45,0.31,0.19,0.14,0.131,0.08,0.062,0.03,0.031,0.015,0.01,0.01]
    b=[0.66,0.55,0.39,0.27,0.14,0.12,0.074,0.05,0.031,0.029,0.021,0.014,0.01,0.01]

    # Plot good fit learning curves
    plt.figure(figsize=(8, 6))
    #print(load("res2")[0])
    #print(load("res2")[1])
    plt.plot(epochs, a, label='Training ', color='red')
    plt.plot(epochs, b, label='Testing ', color='green')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')

    plt.legend()
    plt.grid(True)
    #plt.savefig('./Results/' + "loss" + '.png', dpi=400)
    plt.show()
res_plot4()