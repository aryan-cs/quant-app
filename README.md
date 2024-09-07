
# Quant at Illinois SWE Application

My brute-force solution for searching & optimizing arbitrage opportunities given predetermined currencies & exchange rates. This program assumes these given rates, which can also be reversed to find their inverses:
```
usd_to_eur = 0.90 
eur_to_jpy = 135.00 
jpy_to_usd = 0.0085
```

## 2024 Application Instructions

You are given the exchange rates between three currencies: USD, EUR, and JPY. Your task is to determine if there is an arbitrage opportunity, i.e., a way to start with a given amount of XXX, cycle through the other currencies, and end up with more XXX than you started with.

We ask you code up and submit a solution in one of Python, C++, or Java and then answer some questions about your results for a few test cases. 

While this could very well be done with pen and paper, we would love to see the most optimal solution you can come up with (assuming there are many more inputs than these 3, imagine 10,000+)!

Below are the exchange rates you will need to complete this problem.

```
usd_to_eur = 0.90 
eur_to_jpy = 135.00 
jpy_to_usd = 0.0085
```

Good luck!


## Concept

The program systematically generates all possible cycles from the starting currency type to intermediary currencies and back to the original currency type. It then determines the final value by calculating through the conversion chain and returns the highest arbitrage opportunity.
It can be expanded to include more currency types and rates.


## Authors

- [@aryan-cs](https://www.github.com/aryan-cs)
