class Auto:
    def __init__(self,marca,modelo,placa) :
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    def imprimirObjetos(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}')

taxi = Auto("nissan",2003,"MFV301")
print(taxi.imprimirObjetos())
