"""
Calculates amount of diagonal spreads required to hedge a portfolio
Refer to 'Finance and Investing' doc for more explanation
"""
# Hedge instrument: SPY puts

# NOTE: This calculates a 1:1 put spread, not the 1:1.1 as described in the 'Options Edge' book
#    A 1:1.1 spread ratio would make sense if I'm buying 10 options or more
# Market value of portfolio (that is what is hedged, not invested amount)
# Note: As I am only hedging CSPX and IWDA, beta for my portfolio is 1
# Take beta of IWDA to be 0.89 for now (see 'Finance and Investing' doc)
# Beta of DPYA = IWDP = 0.99
# 5yr beta of ISAC = 1
# 5yr beta of
# Move more than how much then to sell?
mkt_val = float(input('Beta-weighted portfolio value in USD: '))

# SPY price
spy = float(input('Current price of SPY: '))

# OTM spread strike 8.6% OTM
spy_otm_put = 0.914 * spy
print(f'OTM Put Strike to sell: {spy_otm_put}')

# Hedge ratio
ratio = 0.47
print(f'Hedge ratio: {ratio}')

# Notional amount
notional = mkt_val * ratio
print(f'Notional amount: {notional}')

# Delta of each spread with OTM 8.6% put sold (get from market)
delta = abs(float(input('Delta of 8.6% OTM put spread: ')))

# Spreads required
spreads = notional / (delta * spy * 100)

print(f'Number of spreads required (i.e. option contracts): {spreads}')
