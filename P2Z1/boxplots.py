import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from prettytable import PrettyTable

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

    #dropped_poslednja = dropped_payments.dropna()
    return dropped_payments

if __name__ == '__main__':
    X = load_data()
    #X.boxplot(column=['BALANCE', 'PURCHASES', 'INSTALLMENTS_PURCHASES', 'MINIMUM_PAYMENTS'])
    X.boxplot(column=['BALANCE'])
    medijana =  X.BALANCE.median() #medijana za kolonu BALANCE
    srvr = X.BALANCE.mean() #srednja vrednost za kolonu BALANCE
    min1 =  X.BALANCE.min() #
    max1 = X.BALANCE.max() #max koji je outlier
    Q1 = 128.272
    Q3 = 2054.16
    IQR = Q3 - Q1
    min = Q1 - 1.5*IQR
    max = Q3 + 1.5*IQR
    #print "Minimalna vrednost ", min #???????
    #print "Maximalana vrednost ", max

    tabela = PrettyTable()
    tabela.field_names = ["Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela.add_row(["BALANCE", round(min1, 3), round(medijana, 3), round(max, 3), round(srvr, 3)])
    print tabela

    #X.boxplot(column=['CASH_ADVANCE_TRX']) #izdvojeno kao zasebno jer se ovi podaci u okviru prvog boxplota ne vide dobro
    #X.boxplot(column=['PRC_FULL_PAYMENT']) #izdvojeno kao zasebno jer se ovi podaci u okviru prvog boxplota ne vide dobro
    plt.show()

    #print X