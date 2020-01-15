import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

# purchases = pd.DataFrame(data['apples'])
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
purchases.loc['June']
# print(purchases.loc['June'])

# df = pd.read_csv('VKDATA.csv',  index_col=0)
# df  = df.loc['countFriend']
# print(data)
# print(df)


with open('VKDATA.csv', 'r') as csv_file:
    lines = csv_file.readlines()

ID = []
countFriend = []
countFollowers = []
boolComments = []
countOwnerPosts = []
countOwnerReposts = []
countPhotos = []
countVideos = []
countLikesPhotoes = []
sex = []
for line in lines:
    # print(line)
    data = line.split(',')
    ID.append(data[0])
    # countFriend.append(float(data[1]))
    countFollowers.append(int(data[2]))
    boolComments.append(data[3])
    countOwnerPosts.append(data[4])
    countOwnerReposts.append(data[5])
    countPhotos.append(int(data[6]))
    countVideos.append(data[7])
    countLikesPhotoes.append(int(data[8]))
    sex.append(data[9])

# X = np.array([countPhotos])
# y =  np.array([countLikesPhotoes])
# reg = LinearRegression().fit(X, y)
# print(reg.score(X, y))


# print(X)
# print(y)

# import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    # observations
    x = np.array(countPhotos)
    y = np.array(countFollowers)

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
    \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()
