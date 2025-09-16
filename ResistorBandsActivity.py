import os

def clearConsole():
    """
    Literally 'clear' in the terminal except its automated
    """
    os.system('cls' if os.name == 'nt' else 'clear')

clearConsole()

bands = {
    "BLACK":   {"digit": 0, "multiplier": 1,        "tolerance": "_"},
    "BROWN":   {"digit": 1, "multiplier": 10,       "tolerance": 0.01},
    "RED":     {"digit": 2, "multiplier": 100,      "tolerance": 0.02},
    "ORANGE":  {"digit": 3, "multiplier": 1000,     "tolerance": 0.03},
    "YELLOW":  {"digit": 4, "multiplier": 10000,    "tolerance": 0.04},
    "GREEN":   {"digit": 5, "multiplier": 100000,   "tolerance": 0.005},
    "BLUE":    {"digit": 6, "multiplier": 1000000,  "tolerance": 0.0025},
    "VIOLET":  {"digit": 7, "multiplier": 10000000, "tolerance": 0.001},
    "GREY":    {"digit": 8, "multiplier": 100000000,"tolerance": 0.0005},
    "WHITE":   {"digit": 9, "multiplier": 1000000000,"tolerance": "_"},
    "GOLD":    {"digit": "_", "multiplier": 0.1,    "tolerance": "_"},
    "SILVER":  {"digit": "_", "multiplier": 0.01,   "tolerance": "_"},
    "NONE":    {"digit": "_", "multiplier": "_",    "tolerance": "_"}
}

header = ("Color".center(8), "Value".center(10), "Multiplier".center(10), "Tolerance".center(10))
print(*header,"\n","-"*38)
for color, property in bands.items():
    print(color.ljust(8), str(property["digit"]).center(10), str(property["multiplier"]).rjust(10), str(property["tolerance"]).center(10))

while True:
    bandC1 = input("Enter Color of First Ring: ").upper()
    bandC2 = input("Enter Color of Second Ring:").upper()
    bandC3 = input("Enter Color of Third Ring:").upper()
    bandC4 = input("Enter Color of Fourth Ring:").upper()
    
    inputtedBands = [bandC1,bandC2,bandC3,bandC4]

    if bands[bandC1]["digit"] == 0:
        input("The first band color has no corresponding value. [ENTER TO CONTINUE]")
        continue
    
    if bands[bandC2]["digit"] == 0:
        input("The second band color has no corresponding value. [ENTER TO CONTINUE]")
        continue

    if all(i in bands for i in inputtedBands):
        break
    else:
        print("An unsupported color was entered, please try again")
            

value = ((bands[bandC1]["digit"]*10 + bands[bandC2]["digit"])*bands[bandC3]["multiplier"])
print(value,"\u00B1", bands[bandC4]["tolerance"],"ohms")
