# @Author: Ozan YILDIZ@2022
# Dictionary is an unordered key-value mapping list and enclosed by {}

countries = {"Turkey": "Turkey", "Azerbajian": "Azerbajian"}
countryLetters = {'T': 'T', 'u': 'u', 'r': 'r', 'k': 'k', 'e': 'e', 'y': 'y'}

if __name__ == '__main__':
    print("Countries:", countries)
    print("Country Letters of Turkey:", countryLetters)
    print("T Key's Value:", countryLetters.get("T"))
    print("Azerbajian Key's Value:", countries.get("Azerbajian"))
