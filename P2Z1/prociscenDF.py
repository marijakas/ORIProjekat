import pandas as pd
from sklearn.cluster import KMeans
import glob
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("credit_card_data.csv")
    dropped_cst_id = df.drop("CUST_ID", axis='columns')
    dropped_tenure = dropped_cst_id.drop("TENURE", axis='columns')
    dropped_oneoffpurchases = dropped_tenure.drop("ONEOFF_PURCHASES", axis='columns')
    dropped_installmentspurchases = dropped_oneoffpurchases.drop("INSTALLMENTS_PURCHASES", axis='columns')
    dropped_purchasesinstallmentsfre = dropped_installmentspurchases.drop("PURCHASES_INSTALLMENTS_FREQUENCY", axis='columns')
    dropped_caf = dropped_purchasesinstallmentsfre.drop("CASH_ADVANCE_FREQUENCY", axis='columns')



    #df1 = pd.DataFrame(dropped_payments.BALANCE)
    #df1.insert(1, "BALANCE_FREQUENCY",dropped_payments.BALANCE_FREQUENCY, True)

    dropped_poslednja = dropped_caf.dropna()
    return dropped_poslednja
    #return df1

def kmeans(X):
    km = KMeans(n_clusters=8)
    km = km.fit(X)
    X['cluster'] = km.labels_
    print (X)
    #C:\Users\Ana\Desktop\izlazni.csv
    filename = 'izlazni.csv'
    files_present = glob.glob(filename)
    if not files_present:
        X.to_csv(r'.\izlazni.csv', index = False, header=True)
    else:
        print 'WARNING: This file already exists!'

if __name__ == '__main__':
    X = load_data()
    kmeans(X)
    #print X