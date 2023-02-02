#All parameters need to be non-negative
def buy_shares(share_count, share_price, account_number):
    if share_count < 0 or share_price < 0 or account_number < 0:
        print("Invalid values!")
        return

    # Let's imagine some complicated logic that interfaces with the NYSE
    # servers to actually perform the purchase

    print(f"Trying to buy {share_count} shares at {share_price} account {account_number}")


share_count = 1000
share_value = 54.32
account_num = 1235461633

buy_shares(share_count, share_value, account_num)
