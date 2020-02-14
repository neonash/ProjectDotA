import numpy as np
import matplotlib.pyplot as plt


class GaussPlay:
    """Gaussian Data Creation and functional tool"""

    def __init__(self):
        """
        Constructor: to instantiate the data
        """
        self.data = np.random.randn(2, 200)

    def scatter(self):
        """
        Scatter Plot the intermediate result
        :return:
        """
        plt.scatter(self.data[0, :], self.data[1, :])
        plt.xlim([-5, 5])
        plt.ylim([-5, 5])
        return self

    def scale(self, x, y):
        """
        Scaling the matrix with different scales
        :return:
        """
        S = np.array([[x, 0], [0, y]])
        self.data = S @ self.data
        return self

    def rotate(self, theta):
        """
        Rotation by the required angle
        """
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        self.data = R @ self.data
        return self

    def plot(self):
        """
        Plot the  result in case scatter is not sufficient
        :return:
        """
        plt.plot(self.data)
        plt.show()
        return self


A = GaussPlay()
A.scale(2,0.5).rotate(45).rotate(45).scatter()