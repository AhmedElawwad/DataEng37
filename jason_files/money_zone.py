from rates_parser import RatesPasrer

rp = RatesPasrer("exchange_rates.json")

print(f"{rp.date} the base rate")