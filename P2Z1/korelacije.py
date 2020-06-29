import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv("credit_card_data.csv")
    dropped_cst_id = df.drop("CUST_ID", axis='columns')
    dropped_poslednja = dropped_cst_id.drop("TENURE", axis='columns')
    dropped_poslednja = dropped_poslednja.dropna()
    return dropped_poslednja

if __name__ == '__main__':
    podaci = load_data()
    #x = podaci.CASH_ADVANCE_FREQUENCY
    #y = podaci.CASH_ADVANCE_TRX
    #korelacija: 0.79959285 -> dobra korelacija

    #x = podaci.PURCHASES
    #y = podaci.ONEOFF_PURCHASES
    # korelacija: 0.91678022 -> odlicna korelacija

    #x = podaci.PURCHASES_FREQUENCY
    #y = podaci.PURCHASES_INSTALLMENTS_FREQUENCY
    # korelacija: 0.86233791 -> odlicna korelacija

    # BALANCE CASH_ADVANCE umerena: 0.49558562
    # BALANCE CASH_ADVANCE_FREQUENCY umerena: 0.44530716
    # BALANCE CREDIT_LIMIT umerena: 0.53551818

    #------------------------------------PURCHASES INSTALLMENTS_PURCHASES umerena: 0.6792589
    #PURCHASES ONEOFF_PURCHASES_FREQUENCY umerena: 0.49738407
    #PURCHASES PURCHASES_TRX umerena: 0.68873161
    #PURCHASES PAYMENTS umerena: 0.60678236

    #ONEOFF_PURCHASES ONEOFF_PURCHASES_FREQUENCY umerena: 0.52451406
    #ONEOFF_PURCHASES PURCHASES_TRX umerena: 0.54531267
    #ONEOFF_PURCHASES PAYMENTS umerena: 0.57085035

    #INSTALLMENTS_PURCHASES PURCHASES_FREQUENCY umerena: 0.44119344
    #INSTALLMENTS_PURCHASES PURCHASES_INSTALLMENTS_FREQUENCY umerena: 0.5111303
    #INSTALLMENTS_PURCHASES PURCHASES_TRX umerena: 0.62608254

    #CASH_ADVANCE CASH_ADVANCE_FREQUENCY umerena: 0.62903025
    #CASH_ADVANCE CASH_ADVANCE_TRX umerena: 0.65691147
    #CASH_ADVANCE PAYMENTS umerena: 0.45934244

    #PURCHASES_FREQUENCY ONEOFF_PURCHASES_FREQUENCY umerena: 0.50212327
    #PURCHASES_FREQUENCY PURCHASES_TRX umerena: 0.56716826

    #ONEOFF_PURCHASES_FREQUENCY PURCHASES_TRX umerena: 0.54436419

    #PURCHASES_INSTALLMENTS_FREQUENCY PURCHASES_TRX umerena: 0.52919156

    #CREDIT_LIMIT PAYMENTS umerena: 0.42695139
    x = podaci.MINIMUM_PAYMENTS
    y = podaci.PRC_FULL_PAYMENT
    print np.corrcoef(x, y)