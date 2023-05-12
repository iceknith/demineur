class Case:
    
    def __init__(self, posX, posY, isBombe = False, hasDrapeau = False, nombre = 0, image = None) -> None:
        
        self.x = posX
        self.y = posY
        
        self.isBombe = isBombe
        self.hasDrapeau = hasDrapeau
        self.nombre = nombre
        self.image = image
        self.estDecouverte = False
        
    def set_image(self,image):
        self.image=image
    
    def __str__(self) -> str:
        if self.isBombe:
            return "B"
        if self.hasDrapeau:
            return "D"
        return str(self.nombre)
        