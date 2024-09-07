SYMBOLS = ["$", "€", "¥"]
CURRENCIES = ["USD", "EUR", "JPY"]
RATES = {
    ("USD", "EUR"): 0.90,
    ("EUR", "USD"): 1 / 0.90,
    ("EUR", "JPY"): 135.00,
    ("JPY", "EUR"): 1 / 135.00,
    ("JPY", "USD"): 0.0085,
    ("USD", "JPY"): 1 / 0.0085
}

def brute_force_arbitrage(initial_amount, initial_currency):

    possible_cycles = []

    for i in range(len(CURRENCIES)):
        if CURRENCIES[i] != initial_currency:
            cycle = [initial_currency, CURRENCIES[i]]

            for j in range(len(CURRENCIES)):
                if CURRENCIES[j] not in cycle:
                    cycle.append(CURRENCIES[j])

            possible_cycles.append(cycle + [initial_currency])

    best = initial_amount
    current = initial_amount
    
    for cycle in possible_cycles:
        for conversion in range(len(cycle) - 1):
            current *= RATES[(cycle[conversion], cycle[conversion + 1])]

        best = max(best, current)
    
    return best

margin = float(input("What is your margin? > "))
index = int(input("What currency would you like to start in? [0] USD, [1] EUR, [2] JPY > "))

margin_currency = CURRENCIES[index]
margin_symbol = SYMBOLS[index]
final_amount = brute_force_arbitrage(margin, margin_currency)

print("Maximum amount after conversions: " + margin_symbol + str(final_amount) + " " + margin_currency)
