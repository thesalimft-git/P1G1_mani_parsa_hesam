# oop
# object oriented programming

# class  ==> blueprint, map
# method ==> function
# property ==> variable 
# object, instance, things










class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        print('an object create successfully')
        
    def show_info(self):
        print('I am a', self.color, self.brand)
    



c1 = Car('blue', 'Pegu')
c2 = Car('black', 'bmw')
c1.show_info()












