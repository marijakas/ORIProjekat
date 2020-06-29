import pandas as pd
#from sklearn.cluster import KMeans
from kmeans import KMeans
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("credit_card_data.csv")
    dropped_cst_id = df.drop("CUST_ID", axis='columns')
    dropped_tenure = dropped_cst_id.drop("TENURE", axis='columns')
    dropped_oneoffpurchases = dropped_tenure.drop("ONEOFF_PURCHASES", axis='columns')
    dropped_cashadvance = dropped_oneoffpurchases.drop("CASH_ADVANCE", axis='columns')
    dropped_purchasesinstallmentsfrequency = dropped_cashadvance.drop("PURCHASES_INSTALLMENTS_FREQUENCY", axis='columns')
    dropped_cashadvancefrequency = dropped_purchasesinstallmentsfrequency.drop("CASH_ADVANCE_FREQUENCY", axis='columns')
    dropped_purchasestrx = dropped_cashadvancefrequency.drop("PURCHASES_TRX", axis='columns')
    dropped_creditlimit = dropped_purchasestrx.drop("CREDIT_LIMIT", axis='columns')
    dropped_payments = dropped_creditlimit.drop("PAYMENTS", axis='columns')

    df1 = pd.DataFrame(dropped_payments.BALANCE)
    df1.insert(1, "BALANCE_FREQUENCY",dropped_payments.BALANCE_FREQUENCY, True)

    #dropped_poslednja = dropped_payments.dropna()
    #return dropped_payments
    return df1

def kmeans(iris_data):
    #K = range(1, 9)
    #for k in K:
     #   km = KMeans(n_clusters=k)
      #  km = km.fit(X)

    kmeans = KMeans(n_clusters=2, max_iter=100)
    kmeans.fit(iris_data, normalize=False)

    colors = {0: 'red', 1: 'green'}
    plt.figure()
    for idx, cluster in enumerate(kmeans.clusters):
        plt.scatter(cluster.center[0], cluster.center[1], c=colors[idx], marker='x', s=200)  # iscrtavanje centara
        for datum in cluster.data:  # iscrtavanje tacaka
            plt.scatter(datum[0], datum[1], c=colors[idx])

    plt.xlabel('balance')
    plt.ylabel('balance fr')
    plt.show()



if __name__ == '__main__':
    X = load_data()
    #kmeans(X)
    #print X