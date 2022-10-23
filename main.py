from Vehiculo import Vehiculo


class Coche(Vehiculo):
    color: str
    ruedas: int
    puertas: int

    def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
        super().__init__(velocidad, cilindrada)
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Velocidad máxima: {}Km/h\nCilindrada motor: {}cc" \
               "\nColor: {}\nNúmero de ruedas: {}\nNúmero de puertas: {}\n". \
            format(self.velocidad, self.cilindrada, self.color, self.ruedas, self.puertas)


renault = Coche(200, 2000, "rojo", 4, 5)
print(renault)
