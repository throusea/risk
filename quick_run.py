import numpy as np
from record import Record
def main():

    # Record(1).draw_frame_risk(2) # draw one frame
    # Record(1).calculate_risk(1,2) # test one frame,test the risk of one vehicle in one frame
    X = np.arange(1, 15)
    Y = []
    for i in range(1,15):
        _, risk, _ = Record(1).calculate_risk(i,2) # test one frame,test the risk of one vehicle in one frame
        Y.append(risk)
    Y = np.array(Y)
    import matplotlib.pyplot as plt
    plt.plot(X, Y)
    plt.xlabel('Vehicle ID')
    plt.ylabel('Risk')
    plt.title('Risk vs Vehicle ID')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()