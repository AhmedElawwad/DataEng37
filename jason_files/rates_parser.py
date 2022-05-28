import json


# class RatesPasrer:
#
#     def __init__(self):
#         pass
#
#
#     def open_json_file(self, filepath: str):
#
#         with open("exchange_rates.json") as jsonfile:
#             exchange = json.load(jsonfile)
#         print(exchange)
#
#
#
#
# rates = RatesPasrer()
#
# rates.open_json_file("DataEng37\jason_files\exchange_rates.json")


class RatesPasrer:

    def __init__(self, filepath):
        rates = self.open_json_file(filepath)
        self.base_rate = rates["base"]
        self.date = rates["date"]
        self.gbp = rates["rates"]["GBP"]
        self.usd = rates["rates"]["USD"]
        self.jpy = rates["rates"]["JPY"]

    def open_json_file(self, filepath: str):
        with open("exchange_rates.json") as jsonfile:
            return json.load(jsonfile)

    def get_gbp(self, rate):
        return self.gbp

    def get_usd(self, rate):
        return self.usd

    def get_jpy(self, rate):
        return self.jpy


if __name__ == "__main__":
    rates = RatesPasrer("exchange_rates.json")

    # rates.open_json_file("exchange_rates.json")
    print(rates.get_usd("usd"))
    print(rates.get_gbp("gbp"))
    print(rates.get_jpy("jpy"))

    print(f"The us rate is {rates.usd} and the GBP is {rates.gbp}")
