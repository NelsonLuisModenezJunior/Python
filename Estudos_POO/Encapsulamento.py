class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)

    def correr(self):
        print('Correndo...')


davi = Pessoa('Davi', 18, '1892317f39')
print(davi.nome)
print(davi.idade)
# davi.__apresentar_documento()
# O objeto não utiliza esse metodo, já a classe tem conhecimento deste elemento
davi.beber('cerveja')
davi.beber('agua')
davi.correr
# print(davi.__cpf)
# Não da para printar o cpf desta forma pois os dois underlines deixam seu acesso privado
print("-------------------------------------")
print(" ")


class Calculadora:
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print('Operação Inválida!')

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2


calculadora = Calculadora()
resultado = calculadora.calcular('-', 4, 5)
resultado2 = calculadora.calcular('+', 4, 5)
print(resultado)
print(resultado2)

print("-------------------------------------")
print(" ")


class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor


al = Alarme(False)
print(al.get_estado())
al.set_estado('ola')
print(al.get_estado())
al.set_estado(True)
print(al.get_estado())
