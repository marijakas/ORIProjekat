import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def load_data():
    df = pd.read_csv("izlazni.csv")
    return df

if __name__ == '__main__':
    X = load_data()
    klaster0 = X.loc[X['cluster'] == 0]
    #print (klaster0)
    klaster1 = X.loc[X['cluster'] == 1]
    #print (klaster1)
    klaster2 = X.loc[X['cluster'] == 2]
    #print (klaster2)
    klaster3 = X.loc[X['cluster'] == 3]
    #print (klaster3)
    klaster4 = X.loc[X['cluster'] == 4]
    #print (klaster4)
    klaster5 = X.loc[X['cluster'] == 5]
    #print (klaster5)
    klaster6 = X.loc[X['cluster'] == 6]
    #print (klaster6)
    klaster7 = X.loc[X['cluster'] == 7]
    #print (klaster7)

    #klaster0.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster0.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster1.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster1.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster2.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster2.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster3.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster3.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster4.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster4.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster5.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster5.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster6.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster6.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])
    #klaster7.boxplot(column=['BALANCE', 'PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT'])
    #klaster7.boxplot(column=['CASH_ADVANCE_TRX', 'PURCHASES_TRX'])

    medijanaK0 =  klaster0.BALANCE.median() #medijana za kolonu BALANCE
    srvr = klaster0.BALANCE.mean() #srednja vrednost za kolonu BALANCE
    min1 =  klaster0.BALANCE.min() #
    max1 = klaster0.BALANCE.max() #max koji je outlier
    Q1 = 128.272
    Q3 = 2054.16
    IQR = Q3 - Q1
    min = Q1 - 1.5*IQR
    max = Q3 + 1.5*IQR

    tabela = PrettyTable()
    tabela1 = PrettyTable()
    tabela2 = PrettyTable()
    tabela3 = PrettyTable()
    tabela4 = PrettyTable()
    tabela5 = PrettyTable()
    tabela6 = PrettyTable()
    tabela7 = PrettyTable()
    tabela.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela.add_row([0, "BALANCE", round(klaster0.BALANCE.min(), 3), round(klaster0.BALANCE.median(), 3), round(klaster0.BALANCE.max(), 3), round(klaster0.BALANCE.mean(), 3)])
    tabela.add_row([0, "PURCHASES", round(klaster0.PURCHASES.min(), 3), round(klaster0.PURCHASES.median(), 3), round(klaster0.PURCHASES.max(), 3), round(klaster0.PURCHASES.mean(), 3)])
    tabela.add_row([0, "CASH_ADVANCE", round(klaster0.CASH_ADVANCE.min(), 3), round(klaster0.CASH_ADVANCE.median(), 3), round(klaster0.CASH_ADVANCE.max(), 3), round(klaster0.CASH_ADVANCE.mean(), 3)])
    tabela.add_row([0, "CASH_ADVANCE_TRX", round(klaster0.CASH_ADVANCE_TRX.min(), 3), round(klaster0.CASH_ADVANCE_TRX.median(), 3), round(klaster0.CASH_ADVANCE_TRX.max(), 3), round(klaster0.CASH_ADVANCE_TRX.mean(), 3)])
    tabela.add_row([0, "PURCHASES_TRX", round(klaster0.PURCHASES_TRX.min(), 3), round(klaster0.PURCHASES_TRX.median(), 3), round(klaster0.PURCHASES_TRX.max(), 3), round(klaster0.PURCHASES_TRX.mean(), 3)])
    tabela.add_row([0, "CREDIT_LIMIT", round(klaster0.CREDIT_LIMIT.min(), 3), round(klaster0.CREDIT_LIMIT.median(), 3), round(klaster0.CREDIT_LIMIT.max(), 3), round(klaster0.CREDIT_LIMIT.mean(), 3)])
    tabela.add_row([0, "PAYMENTS", round(klaster0.PAYMENTS.min(), 3), round(klaster0.PAYMENTS.median(), 3), round(klaster0.PAYMENTS.max(), 3), round(klaster0.PAYMENTS.mean(), 3)])
    tabela.add_row([0, "MINIMUM_PAYMENTS", round(klaster0.MINIMUM_PAYMENTS.min(), 3), round(klaster0.MINIMUM_PAYMENTS.median(), 3), round(klaster0.MINIMUM_PAYMENTS.max(), 3), round(klaster0.MINIMUM_PAYMENTS.mean(), 3)])
    tabela.add_row([0, "PRC_FULL_PAYMENT", round(klaster0.PRC_FULL_PAYMENT.min(), 3), round(klaster0.PRC_FULL_PAYMENT.median(), 3), round(klaster0.PRC_FULL_PAYMENT.max(), 3), round(klaster0.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela

    tabela1.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela1.add_row([1, "BALANCE", round(klaster1.BALANCE.min(), 3), round(klaster1.BALANCE.median(), 3), round(klaster1.BALANCE.max(), 3), round(klaster1.BALANCE.mean(), 3)])
    tabela1.add_row([1, "PURCHASES", round(klaster1.PURCHASES.min(), 3), round(klaster1.PURCHASES.median(), 3), round(klaster1.PURCHASES.max(), 3), round(klaster1.PURCHASES.mean(), 3)])
    tabela1.add_row([1, "CASH_ADVANCE", round(klaster1.CASH_ADVANCE.min(), 3), round(klaster1.CASH_ADVANCE.median(), 3), round(klaster1.CASH_ADVANCE.max(), 3), round(klaster1.CASH_ADVANCE.mean(), 3)])
    tabela1.add_row([1, "CASH_ADVANCE_TRX", round(klaster1.CASH_ADVANCE_TRX.min(), 3), round(klaster1.CASH_ADVANCE_TRX.median(), 3), round(klaster1.CASH_ADVANCE_TRX.max(), 3), round(klaster1.CASH_ADVANCE_TRX.mean(), 3)])
    tabela1.add_row([1, "PURCHASES_TRX", round(klaster1.PURCHASES_TRX.min(), 3), round(klaster1.PURCHASES_TRX.median(), 3), round(klaster1.PURCHASES_TRX.max(), 3), round(klaster1.PURCHASES_TRX.mean(), 3)])
    tabela1.add_row([1, "CREDIT_LIMIT", round(klaster1.CREDIT_LIMIT.min(), 3), round(klaster1.CREDIT_LIMIT.median(), 3), round(klaster1.CREDIT_LIMIT.max(), 3), round(klaster1.CREDIT_LIMIT.mean(), 3)])
    tabela1.add_row([1, "PAYMENTS", round(klaster1.PAYMENTS.min(), 3), round(klaster1.PAYMENTS.median(), 3), round(klaster1.PAYMENTS.max(), 3), round(klaster1.PAYMENTS.mean(), 3)])
    tabela1.add_row([1, "MINIMUM_PAYMENTS", round(klaster1.MINIMUM_PAYMENTS.min(), 3), round(klaster1.MINIMUM_PAYMENTS.median(), 3), round(klaster1.MINIMUM_PAYMENTS.max(), 3), round(klaster1.MINIMUM_PAYMENTS.mean(), 3)])
    tabela1.add_row([1, "PRC_FULL_PAYMENT", round(klaster1.PRC_FULL_PAYMENT.min(), 3), round(klaster1.PRC_FULL_PAYMENT.median(), 3),round(klaster1.PRC_FULL_PAYMENT.max(), 3), round(klaster1.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela1

    tabela2.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela2.add_row([2, "BALANCE", round(klaster2.BALANCE.min(), 3), round(klaster2.BALANCE.median(), 3), round(klaster2.BALANCE.max(), 3), round(klaster2.BALANCE.mean(), 3)])
    tabela2.add_row([2, "PURCHASES", round(klaster2.PURCHASES.min(), 3), round(klaster2.PURCHASES.median(), 3), round(klaster2.PURCHASES.max(), 3), round(klaster2.PURCHASES.mean(), 3)])
    tabela2.add_row([2, "CASH_ADVANCE", round(klaster2.CASH_ADVANCE.min(), 3), round(klaster2.CASH_ADVANCE.median(), 3), round(klaster2.CASH_ADVANCE.max(), 3), round(klaster2.CASH_ADVANCE.mean(), 3)])
    tabela2.add_row([2, "CASH_ADVANCE_TRX", round(klaster2.CASH_ADVANCE_TRX.min(), 3), round(klaster2.CASH_ADVANCE_TRX.median(), 3), round(klaster2.CASH_ADVANCE_TRX.max(), 3), round(klaster2.CASH_ADVANCE_TRX.mean(), 3)])
    tabela2.add_row([2, "PURCHASES_TRX", round(klaster2.PURCHASES_TRX.min(), 3), round(klaster2.PURCHASES_TRX.median(), 3), round(klaster2.PURCHASES_TRX.max(), 3), round(klaster2.PURCHASES_TRX.mean(), 3)])
    tabela2.add_row([2, "CREDIT_LIMIT", round(klaster2.CREDIT_LIMIT.min(), 3), round(klaster2.CREDIT_LIMIT.median(), 3), round(klaster2.CREDIT_LIMIT.max(), 3), round(klaster2.CREDIT_LIMIT.mean(), 3)])
    tabela2.add_row([2, "PAYMENTS", round(klaster2.PAYMENTS.min(), 3), round(klaster2.PAYMENTS.median(), 3), round(klaster2.PAYMENTS.max(), 3), round(klaster2.PAYMENTS.mean(), 3)])
    tabela2.add_row([2, "MINIMUM_PAYMENTS", round(klaster2.MINIMUM_PAYMENTS.min(), 3), round(klaster2.MINIMUM_PAYMENTS.median(), 3), round(klaster2.MINIMUM_PAYMENTS.max(), 3), round(klaster2.MINIMUM_PAYMENTS.mean(), 3)])
    tabela2.add_row([2, "PRC_FULL_PAYMENT", round(klaster2.PRC_FULL_PAYMENT.min(), 3), round(klaster2.PRC_FULL_PAYMENT.median(), 3), round(klaster2.PRC_FULL_PAYMENT.max(), 3), round(klaster2.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela2

    tabela3.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela3.add_row([3, "BALANCE", round(klaster3.BALANCE.min(), 3), round(klaster3.BALANCE.median(), 3), round(klaster3.BALANCE.max(), 3), round(klaster3.BALANCE.mean(), 3)])
    tabela3.add_row([3, "PURCHASES", round(klaster3.PURCHASES.min(), 3), round(klaster3.PURCHASES.median(), 3), round(klaster3.PURCHASES.max(), 3), round(klaster3.PURCHASES.mean(), 3)])
    tabela3.add_row([3, "CASH_ADVANCE", round(klaster3.CASH_ADVANCE.min(), 3), round(klaster3.CASH_ADVANCE.median(), 3), round(klaster3.CASH_ADVANCE.max(), 3), round(klaster3.CASH_ADVANCE.mean(), 3)])
    tabela3.add_row([3, "CASH_ADVANCE_TRX", round(klaster3.CASH_ADVANCE_TRX.min(), 3), round(klaster3.CASH_ADVANCE_TRX.median(), 3), round(klaster3.CASH_ADVANCE_TRX.max(), 3), round(klaster3.CASH_ADVANCE_TRX.mean(), 3)])
    tabela3.add_row([3, "PURCHASES_TRX", round(klaster3.PURCHASES_TRX.min(), 3), round(klaster3.PURCHASES_TRX.median(), 3), round(klaster3.PURCHASES_TRX.max(), 3), round(klaster3.PURCHASES_TRX.mean(), 3)])
    tabela3.add_row([3, "CREDIT_LIMIT", round(klaster3.CREDIT_LIMIT.min(), 3), round(klaster3.CREDIT_LIMIT.median(), 3), round(klaster3.CREDIT_LIMIT.max(), 3), round(klaster3.CREDIT_LIMIT.mean(), 3)])
    tabela3.add_row([3, "PAYMENTS", round(klaster3.PAYMENTS.min(), 3), round(klaster3.PAYMENTS.median(), 3), round(klaster3.PAYMENTS.max(), 3), round(klaster3.PAYMENTS.mean(), 3)])
    tabela3.add_row([3, "MINIMUM_PAYMENTS", round(klaster3.MINIMUM_PAYMENTS.min(), 3), round(klaster3.MINIMUM_PAYMENTS.median(), 3), round(klaster3.MINIMUM_PAYMENTS.max(), 3), round(klaster3.MINIMUM_PAYMENTS.mean(), 3)])
    tabela3.add_row([3, "PRC_FULL_PAYMENT", round(klaster3.PRC_FULL_PAYMENT.min(), 3), round(klaster3.PRC_FULL_PAYMENT.median(), 3), round(klaster3.PRC_FULL_PAYMENT.max(), 3), round(klaster3.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela3

    tabela4.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela4.add_row([4, "BALANCE", round(klaster4.BALANCE.min(), 3), round(klaster4.BALANCE.median(), 3), round(klaster4.BALANCE.max(), 3), round(klaster4.BALANCE.mean(), 3)])
    tabela4.add_row([4, "PURCHASES", round(klaster4.PURCHASES.min(), 3), round(klaster4.PURCHASES.median(), 3), round(klaster4.PURCHASES.max(), 3), round(klaster4.PURCHASES.mean(), 3)])
    tabela4.add_row([4, "CASH_ADVANCE", round(klaster4.CASH_ADVANCE.min(), 3), round(klaster4.CASH_ADVANCE.median(), 3), round(klaster4.CASH_ADVANCE.max(), 3), round(klaster4.CASH_ADVANCE.mean(), 3)])
    tabela4.add_row([4, "CASH_ADVANCE_TRX", round(klaster4.CASH_ADVANCE_TRX.min(), 3), round(klaster4.CASH_ADVANCE_TRX.median(), 3), round(klaster4.CASH_ADVANCE_TRX.max(), 3), round(klaster4.CASH_ADVANCE_TRX.mean(), 3)])
    tabela4.add_row([4, "PURCHASES_TRX", round(klaster4.PURCHASES_TRX.min(), 3), round(klaster4.PURCHASES_TRX.median(), 3),round(klaster4.PURCHASES_TRX.max(), 3), round(klaster4.PURCHASES_TRX.mean(), 3)])
    tabela4.add_row([4, "CREDIT_LIMIT", round(klaster4.CREDIT_LIMIT.min(), 3), round(klaster4.CREDIT_LIMIT.median(), 3), round(klaster4.CREDIT_LIMIT.max(), 3), round(klaster4.CREDIT_LIMIT.mean(), 3)])
    tabela4.add_row([4, "PAYMENTS", round(klaster4.PAYMENTS.min(), 3), round(klaster4.PAYMENTS.median(), 3), round(klaster4.PAYMENTS.max(), 3), round(klaster4.PAYMENTS.mean(), 3)])
    tabela4.add_row([4, "MINIMUM_PAYMENTS", round(klaster4.MINIMUM_PAYMENTS.min(), 3), round(klaster4.MINIMUM_PAYMENTS.median(), 3), round(klaster4.MINIMUM_PAYMENTS.max(), 3), round(klaster4.MINIMUM_PAYMENTS.mean(), 3)])
    tabela4.add_row([4, "PRC_FULL_PAYMENT", round(klaster4.PRC_FULL_PAYMENT.min(), 3), round(klaster4.PRC_FULL_PAYMENT.median(), 3), round(klaster4.PRC_FULL_PAYMENT.max(), 3), round(klaster4.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela4

    tabela5.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela5.add_row([5, "BALANCE", round(klaster5.BALANCE.min(), 3), round(klaster5.BALANCE.median(), 3), round(klaster5.BALANCE.max(), 3), round(klaster5.BALANCE.mean(), 3)])
    tabela5.add_row([5, "PURCHASES", round(klaster5.PURCHASES.min(), 3), round(klaster5.PURCHASES.median(), 3), round(klaster5.PURCHASES.max(), 3), round(klaster5.PURCHASES.mean(), 3)])
    tabela5.add_row([5, "CASH_ADVANCE", round(klaster5.CASH_ADVANCE.min(), 3), round(klaster5.CASH_ADVANCE.median(), 3), round(klaster5.CASH_ADVANCE.max(), 3), round(klaster5.CASH_ADVANCE.mean(), 3)])
    tabela5.add_row([5, "CASH_ADVANCE_TRX", round(klaster5.CASH_ADVANCE_TRX.min(), 3), round(klaster5.CASH_ADVANCE_TRX.median(), 3), round(klaster5.CASH_ADVANCE_TRX.max(), 3), round(klaster5.CASH_ADVANCE_TRX.mean(), 3)])
    tabela5.add_row([5, "PURCHASES_TRX", round(klaster5.PURCHASES_TRX.min(), 3), round(klaster5.PURCHASES_TRX.median(), 3),round(klaster5.PURCHASES_TRX.max(), 3), round(klaster5.PURCHASES_TRX.mean(), 3)])
    tabela5.add_row([5, "CREDIT_LIMIT", round(klaster5.CREDIT_LIMIT.min(), 3), round(klaster5.CREDIT_LIMIT.median(), 3), round(klaster5.CREDIT_LIMIT.max(), 3), round(klaster5.CREDIT_LIMIT.mean(), 3)])
    tabela5.add_row([5, "PAYMENTS", round(klaster5.PAYMENTS.min(), 3), round(klaster5.PAYMENTS.median(), 3), round(klaster5.PAYMENTS.max(), 3), round(klaster5.PAYMENTS.mean(), 3)])
    tabela5.add_row([5, "MINIMUM_PAYMENTS", round(klaster5.MINIMUM_PAYMENTS.min(), 3), round(klaster5.MINIMUM_PAYMENTS.median(), 3),round(klaster5.MINIMUM_PAYMENTS.max(), 3), round(klaster5.MINIMUM_PAYMENTS.mean(), 3)])
    tabela5.add_row([5, "PRC_FULL_PAYMENT", round(klaster5.PRC_FULL_PAYMENT.min(), 3), round(klaster5.PRC_FULL_PAYMENT.median(), 3), round(klaster5.PRC_FULL_PAYMENT.max(), 3), round(klaster5.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela5

    tabela6.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela6.add_row([6, "BALANCE", round(klaster6.BALANCE.min(), 3), round(klaster6.BALANCE.median(), 3),round(klaster6.BALANCE.max(), 3), round(klaster6.BALANCE.mean(), 3)])
    tabela6.add_row([6, "PURCHASES", round(klaster6.PURCHASES.min(), 3), round(klaster6.PURCHASES.median(), 3),round(klaster6.PURCHASES.max(), 3), round(klaster6.PURCHASES.mean(), 3)])
    tabela6.add_row([6, "CASH_ADVANCE", round(klaster6.CASH_ADVANCE.min(), 3), round(klaster6.CASH_ADVANCE.median(), 3),round(klaster6.CASH_ADVANCE.max(), 3), round(klaster6.CASH_ADVANCE.mean(), 3)])
    tabela6.add_row([6, "CASH_ADVANCE_TRX", round(klaster6.CASH_ADVANCE_TRX.min(), 3), round(klaster6.CASH_ADVANCE_TRX.median(), 3),round(klaster6.CASH_ADVANCE_TRX.max(), 3), round(klaster6.CASH_ADVANCE_TRX.mean(), 3)])
    tabela6.add_row([6, "PURCHASES_TRX", round(klaster6.PURCHASES_TRX.min(), 3), round(klaster6.PURCHASES_TRX.median(), 3),round(klaster6.PURCHASES_TRX.max(), 3), round(klaster6.PURCHASES_TRX.mean(), 3)])
    tabela6.add_row([6, "CREDIT_LIMIT", round(klaster6.CREDIT_LIMIT.min(), 3), round(klaster6.CREDIT_LIMIT.median(), 3),round(klaster6.CREDIT_LIMIT.max(), 3), round(klaster6.CREDIT_LIMIT.mean(), 3)])
    tabela6.add_row([6, "PAYMENTS", round(klaster6.PAYMENTS.min(), 3), round(klaster6.PAYMENTS.median(), 3),round(klaster6.PAYMENTS.max(), 3), round(klaster6.PAYMENTS.mean(), 3)])
    tabela6.add_row([6, "MINIMUM_PAYMENTS", round(klaster6.MINIMUM_PAYMENTS.min(), 3), round(klaster6.MINIMUM_PAYMENTS.median(), 3),round(klaster6.MINIMUM_PAYMENTS.max(), 3), round(klaster6.MINIMUM_PAYMENTS.mean(), 3)])
    tabela6.add_row([6, "PRC_FULL_PAYMENT", round(klaster6.PRC_FULL_PAYMENT.min(), 3), round(klaster6.PRC_FULL_PAYMENT.median(), 3),round(klaster6.PRC_FULL_PAYMENT.max(), 3), round(klaster6.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela6

    tabela7.field_names = ["Klaster", "Kolona", "Minimum", "Medijana", "Maximum", "Srednja vrednost"]
    tabela7.add_row([7, "BALANCE", round(klaster7.BALANCE.min(), 3), round(klaster7.BALANCE.median(), 3),round(klaster7.BALANCE.max(), 3), round(klaster7.BALANCE.mean(), 3)])
    tabela7.add_row([7, "PURCHASES", round(klaster7.PURCHASES.min(), 3), round(klaster7.PURCHASES.median(), 3),round(klaster7.PURCHASES.max(), 3), round(klaster7.PURCHASES.mean(), 3)])
    tabela7.add_row([7, "CASH_ADVANCE", round(klaster7.CASH_ADVANCE.min(), 3), round(klaster7.CASH_ADVANCE.median(), 3),round(klaster7.CASH_ADVANCE.max(), 3), round(klaster7.CASH_ADVANCE.mean(), 3)])
    tabela7.add_row([7, "CASH_ADVANCE_TRX", round(klaster7.CASH_ADVANCE_TRX.min(), 3), round(klaster7.CASH_ADVANCE_TRX.median(), 3),round(klaster7.CASH_ADVANCE_TRX.max(), 3), round(klaster7.CASH_ADVANCE_TRX.mean(), 3)])
    tabela7.add_row([7, "PURCHASES_TRX", round(klaster7.PURCHASES_TRX.min(), 3), round(klaster7.PURCHASES_TRX.median(), 3),round(klaster7.PURCHASES_TRX.max(), 3), round(klaster7.PURCHASES_TRX.mean(), 3)])
    tabela7.add_row([7, "CREDIT_LIMIT", round(klaster7.CREDIT_LIMIT.min(), 3), round(klaster7.CREDIT_LIMIT.median(), 3),round(klaster7.CREDIT_LIMIT.max(), 3), round(klaster7.CREDIT_LIMIT.mean(), 3)])
    tabela7.add_row([7, "PAYMENTS", round(klaster7.PAYMENTS.min(), 3), round(klaster7.PAYMENTS.median(), 3),round(klaster7.PAYMENTS.max(), 3), round(klaster7.PAYMENTS.mean(), 3)])
    tabela7.add_row([7, "MINIMUM_PAYMENTS", round(klaster7.MINIMUM_PAYMENTS.min(), 3), round(klaster7.MINIMUM_PAYMENTS.median(), 3),round(klaster7.MINIMUM_PAYMENTS.max(), 3), round(klaster7.MINIMUM_PAYMENTS.mean(), 3)])
    tabela7.add_row([7, "PRC_FULL_PAYMENT", round(klaster7.PRC_FULL_PAYMENT.min(), 3), round(klaster7.PRC_FULL_PAYMENT.median(), 3),round(klaster7.PRC_FULL_PAYMENT.max(), 3), round(klaster7.PRC_FULL_PAYMENT.mean(), 3)])
    print tabela7

    plt.show()
