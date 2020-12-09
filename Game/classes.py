class Mario: 

    _lives = 3
    _speed = 30.0

    def Test(self):
        print("yay")
        print("Speed is: ", self._speed)

instanceMario = Mario()
nogEenMario = Mario()
print( instanceMario._lives )

instanceMario.Test()
instanceMario._speed = 50.5


print(instanceMario._lives)
print("InstanceMario snelheid: ", instanceMario)



class Mario1:

    lives = 4
    speed = 30
    points = 0
    item = None

    def __init__(self):
        #Dit is de constructor functie
        print("yay")
    def Walk(self):
        #instructies voor lopen
        print("yayss")

mario2 = Mario1()
mario3 = Mario1()
mario2.points += 50
mario3.Walk()




 