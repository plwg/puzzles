# You have 52 playing cards (26 red, 26 black). You draw cards one by one.
# A red card pays you a dollar. A black one fines you a dollar.
# You can stop any time you want. Cards are not returned to the deck after being drawn.
# What is the optimal stopping rule in terms of maximizing expected payoff?
# Also, what is the expected payoff following this optimal rule?
# https://gwern.net/problem-14

from itertools import product

num_cards = 26
card_left = range(0, num_cards + 1)
all_scenario = product(*([card_left] * 2))

pay_off = {}

for s in all_scenario:
    if s[0] == 0:
        pay_off[s] = 0
        continue

    if s[1] == 0:
        pay_off[s] = s[0]
        continue

    p = (
        s[0] * (1 + pay_off[(s[0] - 1, s[1])]) + s[1] * (-1 + pay_off[(s[0], s[1] - 1)])
    ) / (s[0] + s[1])

    pay_off[s] = max(p, 0)

# Optimal stopping is refering to the pay_off table and
# 1. draw whenever the expected future pay off is not zero.
# 2. stop drawing if the expected future pay off is zero

# Expected return of optimal pay
print(pay_off[(num_cards, num_cards)])
