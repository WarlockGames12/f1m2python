class Character :

    speed = 10
    points = 0
    sprite = None
    iq = 100

    def __init__(self) : 
        print("De constructor van de character")

    def Walk(self):
        print("Character loopt nu met snelheid ", self.speed)


class Mario(Character):
    
    lives = 4
    item = None
    

    def __init__(self):
        # We vullen aan op de constructor van de Character
        super().__init__()

        #de snelheid van mario is standaard hoger
        self.speed = 30

    def Jump(self) :
        print("Mario Springt!")

    def Walk(self):
        print("Mario loop heel anders, maar wel met de snelheid ", self.speed)


class Goomba(Character):

    chase = 1
    item = None
    lives = 1
    speed = 5

    def __init__(self):
        super().__init__()

        self.speed = 5

    def Walk(self) :
        print("Goomba's speed is", self.speed)

#instanties maken
characterA = Character()
MarioX = Mario()
GoombaX = Goomba()


characterA.Walk()
MarioX.Walk()
GoombaX.Walk()

print(MarioX.speed)
print(characterA.speed)
print(MarioX.lives)
print(GoombaX.speed)

# Het resultaat in de console geeft een geheugenadres weer.
# Dit geheigenadres verwijst naar de locatie van het volledige object:
print(MarioX)





