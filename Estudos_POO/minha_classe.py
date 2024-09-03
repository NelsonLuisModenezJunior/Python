from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(
            f"Meu nome é {self.nome}, tenho {
                self.idade} anos e meu e-mail é: {self.email}"
        )


sage = Cliente(nome="Sage", email="sagezinha2gmail.com", idade=20)
# print(sage)
print(" ")
print("-----------------------------------------")
sage.exibir()


class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir(self):
        print(self.nome, self.idade, self.email)

    def chamar_exibir(self):
        self.exibir()


junior = Cliente("Júnior", 18, "juninho@gmail.com")

print("-----------------------------------------")
print(" ")
# print(junior.nome, junior.idade, junior.email)
print(junior.exibir())


class Cliente:
    pass

    def exibir(self):
        print("Eu sou um cliente!")


junior = Cliente()
junior.exibir()
print("-----------------------------------------")
print(" ")

# Classe abstrata


class MinhaClasse:
    def __init__(self, att):
        self.meu_atributo = 'Ola Mundo'
        self.meu_atributo2 = att

    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num1, num2):
        return num1 * num2


objeto = MinhaClasse('Meu atributo 2')
att2 = objeto.meu_atributo2
print(att2)
result = objeto.meu_metodo2(3, 2)
print(result)
att = objeto.meu_atributo
print(att)
objeto.meu_metodo()
print("-----------------------------------------")
print(" ")


class ControleRemoto:
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal Avançado')

    def voltar_canal(self):
        print('Canal voltado')

    def escolher_canal(self, canal):
        print('Alterado para o canal: {}'.format(canal))


controle_sala = ControleRemoto('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(15)

controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)
controle_quarto.voltar_canal()
controle_quarto.escolher_canal(3)

print("-------------------------------------")
print(" ")

# Outra classe

class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def drive(self, vehicle: str) -> None:
        print('Driving a {}' .format(vehicle))

    def sing(self) -> None:
        print('Did I really just forget that melody?')

    def present_age(self) -> int:
        return self.age
    
#----------------------------------------------
    
class MinhaClasse:
    estatico = 'Junior' # Variavel de classe, nao e recomendado esse uso

    def __init__(self, estado):
        self.estado = estado
        #self.estatico = 'Junior'

    def print_estatico(self):
        print(self.estatico)
    
    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Pro-gramador'

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
obj3 = MinhaClasse(True)
obj4 = MinhaClasse(False)

#obj1.estatico = 'Programador' somente o objeto 1 vai mostrar programador
MinhaClasse.estatico = 'Programador'
obj1.estatico = 'Fortnite'

print(obj1.estatico)
print(obj2.estatico)
obj1.mudar_estatico()
print(obj1.print_estatico())
print(MinhaClasse.estatico)
obj3.print_estatico()
obj4.print_estatico

print("-------------------------------------")
print(" ")

class Loja:
    tarifa = 2.09

    def __init__(self, endereco) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa

loja_praia = Loja('Praia')
loja_centro = Loja('Centro')

loja_praia.apresentar_endereco()

print(loja_praia.vender()) #v1
print(loja_centro.vender()) #v1

loja_centro.alterar_tarifa(5.56)

print(loja_praia.vender()) #v2
print(loja_centro.vender()) #v2