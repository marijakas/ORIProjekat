import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("credit_card_data.csv")
    dropped_cst_id = df.drop("CUST_ID", axis='columns')
    dropped_poslednja = dropped_cst_id.drop("TENURE", axis='columns')
    dropped_poslednja = dropped_poslednja.dropna()
    return dropped_poslednja

def kmeans(X):
    Sum_of_squared_distances = []
    K = range(1, 16)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(X)
        Sum_of_squared_distances.append(km.inertia_)
    return Sum_of_squared_distances


if __name__ == '__main__':
    X = load_data()
    sq_distacnes = kmeans(X)
    print(sq_distacnes)

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    plt.scatter(a, sq_distacnes)
    plt.show()