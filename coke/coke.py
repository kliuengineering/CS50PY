def main():
    debit = 50
    change = 0

    while debit > 0:
        print(f"Amount Due: {debit}")
        payment = int( input("Insert Coin: ") )
        if(payment == 5 or payment == 10 or payment == 25):
            debit -= payment
    if(debit <= 0):
        change = -debit
        print(f"Change Owed: {change}")
main()
