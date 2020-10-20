class Car(): 
    def __init__(self, name, gaz = 0):
        self.name = name
        self.gaz = gaz
    def fill(self):
        self.gaz += 100
        return True
    def go(self): 
        road = int(input('Pick the distanse: '))
        req = road / 10
        if self.gaz >= req: 
            self.gaz -= req
            return True
        else: 
            return False
    def level(self):
        return self.gaz
    
def main(): 
    car = Car(input('Name it: '))
    f = None 
    while f != 0: 
        print("""
                    
                    0 - Exit
                    1 - Fill
                    2 - Go 
                    3 - Level
                    
              """)
        try:
            f = int(input('Pick: '))
        except ValueError: 
            print('Nice pick, fuck yourself!')
        if f == 0: 
            print('BB!')
            break
        if f == 1: 
            car.fill()
            print('Level:', car.gaz)
        if f == 2: 
            if car.go():
                print('Nice way!', f'Your level of oil: {int(car.gaz)}', sep = '\n')
            else: 
                print('Not enough oil!', f"Your oil for: {int(car.gaz*10)} km", sep = '\n')
            
        if f == 3: 
            print('Level', car.level())
        
main()
