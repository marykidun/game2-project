earned_coins = 1800
month_coins = 1800
saved_coins = 900

coins = earned_coins
for month in range(1, 13):
    coins = coins + month_coins - saved_coins
    print('Month %s = %s' % (month, coins))


