from ElectricShaver import ElectricShaver

def main():
        shaver = ElectricShaver()
        shaver1 = ElectricShaver("Samsung",3,"battery",2,"dry",30,150)
        shaver2 = ElectricShaver("Philips",1,"Litiy battery",1,"damp",10,50)
        print(shaver)
        print(shaver1)
        print(shaver2)
        print(ElectricShaver.get_static_amount())
main()