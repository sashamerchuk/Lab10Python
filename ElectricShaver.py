class ElectricShaver:
    amount = 0

    def __init__(self, companyManufacturer="Philips", numberOfNuzzle=2, powerSupply="battery", numberOfBlades=5,
                 typeOfShaving="damp", batteryLife=25, price=100):
        self.companyManufacturer = companyManufacturer
        self.numberOfNuzzle = numberOfNuzzle
        self.powerSupply = powerSupply
        self.numberOfBlades = numberOfBlades
        self.typeOfShaving = typeOfShaving
        self.batteryLife = batteryLife
        self.price = price

    def __del__(self):
        print("Destructor was called")

    def __str__(self):
        return "ElectricShaver : " \
            + " companyManufacturer  " + self.companyManufacturer \
            + "; numberOfNuzzle  " + str(self.numberOfNuzzle) \
            + "; powerSupply  " + self.powerSupply \
            + "; numberOfBlades  " + str(self.numberOfBlades) \
            + "; typeOfShaving  " + self.typeOfShaving \
            + "; batteryLife  " + str(self.batteryLife) \
            + "; price  " + str(self.price)

    @staticmethod
    def get_static_amount():
        return ElectricShaver.amount
