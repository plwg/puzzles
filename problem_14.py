# You have 52 playing cards (26 red, 26 black). You draw cards one by one.
# A red card pays you a dollar. A black one fines you a dollar.
# You can stop any time you want. Cards are not returned to the deck after being drawn.
# What is the optimal stopping rule in terms of maximizing expected payoff?
# Also, what is the expected payoff following this optimal rule?
# https://gwern.net/problem-14

from itertools import product

num_cards = 26
card_left = range(0, num_cards + 1)
all_scenario = product(card_left, card_left)

pay_off = {}

for scenario in all_scenario:
    pay_off[scenario] = None


for k in pay_off.keys():
    if k[0] == 0:
        pay_off[k] = 0
        continue

    if k[1] == 0:
        pay_off[k] = k[0]
        continue

    p = (
        k[0] * (1 + pay_off[(k[0] - 1, k[1])]) + k[1] * (-1 + pay_off[(k[0], k[1] - 1)])
    ) / (k[0] + k[1])

    pay_off[k] = max(p, 0)

print(pay_off[(26, 26)])

# Optimal stopping is refering to the pay_off table and draw whenever the expected future pay off is not zero.
