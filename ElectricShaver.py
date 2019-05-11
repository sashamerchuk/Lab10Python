class ElectricShaver:
    amount = 0

    def __init__(self, company_manufacturer="Philips", number_of_nuzzle=2, power_supply="battery", number_of_blades=5,
                 type_of_shaving="damp", battery_life=25, price=100):
        self.company_manufacturer = company_manufacturer
        self.number_of_nuzzle = number_of_nuzzle
        self.power_supply = power_supply
        self.number_of_blades = number_of_blades
        self.type_of_shaving = type_of_shaving
        self.battery_life = battery_life
        self.price = price
    
    def __del__(self):
        print("Destructor was called")

    def __str__(self):
        return "ElectricShaver : " \
            + " companyManufacturer  " + self.company_manufacturer \
            + "; numberOfNuzzle  " + str(self.number_of_nuzzle) \
            + "; powerSupply  " + self.power_supply \
            + "; numberOfBlades  " + str(self.number_of_blades) \
            + "; typeOfShaving  " + self.type_of_shaving \
            + "; batteryLife  " + str(self.battery_life) \
            + "; price  " + str(self.price)

    @staticmethod
    def get_static_amount():
        return ElectricShaver.amount
