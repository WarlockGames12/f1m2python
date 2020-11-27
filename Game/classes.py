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

    def Stands(self):
        print("The stand's power is: ", self._Power)
        print("The stand's speed is: ", self._Speed)
        print("The stand's range is: ", self._Range)
        print("The stand's Durability is: ", self._Durability)
        print("The stand's Precision is: ", self._Precision)
        print("The stand's Potential is: ", self._Potential)

instanceStand = Stand()
nogEenStand = Stand()
print( instanceStand._Power )


instanceMario._Speed = 'B'


print(instanceStand._Speed)
print("InstanceStand snelheid: ", instanceStand)




 