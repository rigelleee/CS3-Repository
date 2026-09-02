class Starship: 

    def __init__(self, baseweight, cargoweight):
        self.baseweight= baseweight
        self.cargoweight=cargoweight

    def cargo_load(self):
        self.finalfuel=self.baseweight+self.cargoweight
        return self.finalfuel

    def calculate_fuel(self):
        fuel=(self.cargo_load())*3
        print("Final Fuel Needed: ", fuel)

starship=Starship(50000, 1000)
starship.cargo_load()
starship.cargo_load()
starship.cargo_load()
starship.calculate_fuel()