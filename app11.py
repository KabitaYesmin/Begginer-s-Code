price =10000000
has_good_Credit = False
if has_good_Credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
    print(f"Down Payment:${ down_payment}")