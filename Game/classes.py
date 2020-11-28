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

class Stand:
    _Power = 'C'
    _Speed = 'A'
    _Range = 'A'
    _Durability = 'D'
    _Precision = 'A'
    _Potential = 'C'

    def Power(self):
        print("The stand's power is: ", self._Power)
    def Speed(self):
        print("The stand's speed is: ", self._Speed)
    def Range(self):
        print("The stand's range is: ", self._Range)
    def Durability(self):
        print("The stand's durability is: ", self._Durability)
    def Precision(self):
        print("The stand's precision is: ", self._Precision)
    def Potential(self):
        print("The stand's potential is: ", self._Potential)

instanceStand = Stand()
nogEenStand = Stand()
print( instanceStand._Power )

instanceStand._Power = 'A'
instanceStand._Speed = 'B'
instanceStand._Range = 'A'
instanceStand._Durability = 'C'
instanceStand._Precision = 'B'
instanceStand._Potential = 'B'


print(instanceStand._Power)
print(instanceStand._Speed)
print(instanceStand._Range)
print(instanceStand._Durability)
print(instanceStand._Precision)
print(instanceStand._Potential)
print("InstanceStand snelheid: ", instanceStand)




 