class Ventana:
    __titulo = ""
    __x1 = 0
    __y1 = 0
    __x2 = 0
    __y2 = 0

    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        self.__titulo = titulo
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def mostrar(self):
        print(f"{self.__titulo}, ({self.__x1}, {self.__y1}), ({self.__x2}, {self.__y2})")
    
    def ancho(self):
        return self.__x2 - self.__x1 
    
    def alto(self):
        return self.__y2 - self.__y1
    
    def getTitulo(self):
        return self.__titulo
    
    def moverDerecha(self, valor=500):
        i = 0
        while i < valor and self.__x2 < 500:
            self.__x1 += 1
            self.__x2 += 1
            i += 1
    
    def moverIzquierda(self, valor=500):
        i = 0
        while i < valor and self.__x1 > 0:
            self.__x1 -= 1
            self.__x2 -= 1
            i += 1

    def bajar(self, valor=500):
        i = 0
        while i < valor and self.__y2 < 500:
            self.__y1 += 1
            self.__y2 += 1
            i += 1

    def subir(self, valor=500):
        i = 0
        while i < valor and self.__y1 > 0:
            self.__y1 -= 1
            self.__y2 -= 1
            i += 1

