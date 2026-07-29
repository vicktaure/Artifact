class personnage:
    def __init__(self, name, hp, x, y,level):
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y
        self.level = level
    def move(self,target_x, target_y):
        self.x = target_x
        self.y = target_y