# coding: -*- utf-8 -*-

# Parte 1
# %% Introdução  ao Python

print("Olá, acústicos!")

# %% 1.1 Data types

print(type(1), type(1.1), type('oi'), type({'key': 'item'}), type((1, )), type([1]))

# %% 1.2 Loops e condicionais

mlist = [1, 2, 3, 4, 5, 6]

for num in mlist:
    if num < 3:
        print('menor que', 3)
    elif num >= 3 and num < 5:
        print('entre', 3, 'e', 5)
    else:
        print('maior que 5')

# %% 1.3 Funções

def foo(bar):
    print(bar)

foo("baz")

# %% Parte 2
# Paradigmas de programação

a = 1
b = 2
c = 2*a + b
c /= 2
print(a, b, c)

texto = 'Oi, meu nome é Python.\nSou uma linguagem muito legal.'
lstxt = texto.replace('\n',' ').split(' ')
print(texto)
print(lstxt)

# %% 2.1 Programação orientada ao objeto

class Foo:
    def bar(self):
        print('baz')
        return

fu = Foo()
fu.bar()


# %% Parte 3, mas peraê
# Exemplo básico

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        return


class Estudante(Pessoa):
    def __init__(self, nome, idade, semestre):
        super().__init__(nome, idade)
        self.semestre = semestre
        return


class Trabalhador(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
        return


mae = Pessoa('Maria', 53)
eu = Estudante('João', 25, 12)
ele = Trabalhador('Matheus', 28, 'God da porra toda')

print("As pessoas criadas foram:", mae.nome,',',eu.nome,'e',ele.nome)
print("As idades são:", mae.idade,',', eu.idade, 'e', ele.idade)


# %% 3.1 Classes
"""
    São caracterizadores, definem novos tipos de dados, guardam uma série de atributos e métodos
    que caracterizam seu uso. Podemos pensar como definições de conceitos. Como Carro, Moto, Cadeira
    Bicicleta, Computador. Quando usamos essas palavras, sabemos que definem um TIPO específico de
    coisa, mas não define características particulares. As particularidades são pertencentes ao OBJETO.
"""

# %% 3.1.1 Objetos, ou Instâncias
"""
    Existem diversos OBJETOS que são parte de cada uma das classes citadas anteriormente.
    Vamos pegar o exemplo das CADEIRAS. Existe essa cadeira, aquela cadeira, a tua cadeira.
    Todas são CADEIRAS, mas nenhuma é a MESMA CADEIRA, cada uma é um OBJETO diferente,
    mas todos esses objetos podem ser chamados de CADEIRA. Em OOP chamamos um objeto de uma
    determinada classe de INSTÂNCIA da classe, do inglês INSTANCE.
"""

# %% 3.2 Atributos
"""
    São valores, ou conjuntos de valores (equivalente a variáveis) que pertêncem ao objeto e definem
    particularidades. Vamos usar o exemplo de uma instancia da classe COMPUTADOR:

        O MeuPC é um Computador da marca DELL, com processador i5 e 6 GB de memória RAM.

    MeuPC acabou de ser definido com determinados atributos (marca, processador e memória RAM) com valores
    particulares (DELL, i5 e 6 GB). Podemos definir outra instância de COMPUTADOR como sendo:

        O PCdoMts é um Computador da marca Apple, com processador i5 e 8 GB de memória RAM.

    PCdoMts foi definido com os mesmos atributos que o MeuPC (marca, processador e memória RAM), mas seus
    valores são distintos, tornando as duas INSTANCIAS da classe COMPUTADOR diferentes.

    Note que ambas as instâncias possuem processador i5, ou seja, embora CADA OBJETO tenha seu atributo
    processador como algo individual, os VALORES que eles carregam não são exclusivos. O fato de o atributo
    ser particular implica que o mesmo NOME de atributo está presente nos diferentes objetos e pode guardar
    diferentes valores.
"""

# %% 3.3 Métodos
"""
    Métodos são o equivalente as ações que podem ser realizadas com um objeto. Vamos pensar num objeto da
    classe COMPUTADOR, digamos MeuPC, vamos pensar agora em ações que posso realizar com MeuPC:

        * Programar;
        * Navegar na internet;
        * Jogar;
        * Ler;
        * Ouvir música;
        * Fazer medições acústicas.

    Todas essas ações (notem que são definidas por verbos) representam uma série de atividades que necessitam
    ser realizadas. Por exemplo, para ouvir música é preciso:

        * Abrir um software de reprodução de música;
        * Escolher uma música;
        * Apertar o play;
        * Ajustar o volume para não machucar meus ouvidos.


    Podemos, então, pensar em métodos como FUNÇÕES intrínsecas ao OBJETO. Isso mostra que OOP não abandona
    completamente a programação estruturada, mas é essencialmente diferente no sentido de criar diversas
    sub estruturas de código que realizam pequenas tarefas e podem, ou não, ser interdependentes.
"""


# %% Parte 4 - HERANÇA, COMPOSIÇÃO, POLIMORFISMO E ENCAPSULAMENTO

"""
    Existem algumas práticas que definem a programação orientada ao objeto, que são Herança, Composição,
    Polimorfismo e Encapsulamento.
"""

# %% HERANÇA
"""
    Como o próprio nome diz, é a habilidade que uma classe tem de HERDAR atributos e métodos de uma outra
    classe, chamada classe superior, ou superclasse.

    Como no exemplo da Pessoa, Estudante, Trabalhador, a Estudante e a Trabalhador HERDARAM os atributos
    .nome e .idade da Pessoa. Isso define que a classe HERDEIRA, ou subclasse é TAMBÉM uma Instancia da
    superclasse.

"""

class Foo:
    pass

class Bar(Foo):
    pass

mybar = Bar()
print(isinstance(mybar, Foo))


# %% COMPOSIÇÃO
"""
    Muitas vezes uma classe depende de outras classes, ou de objetos de outras classes, para se constituir.
    Pensemos num Carro, este possui:

        * Rodas e Pneus;
        * Chassi;
        * Motor;
        * Tanque de combustível;
        * Cor;
        * Marca.

    Podemos então pensar que estes são atributos de um Carro. Mas se distrincharmos mais a fundo cada um destes,
    chegaremos a pelo menos mais duas classes, o Motor e o Tanque de combustível:

        Motor:
            * Potência;
            * Marca;
            * Tipo de combustível.

        Tanque:
            * Capacidade;
            * Tipo;
            * Marca.

    Com isso, qualquer objeto da classe CARRO será COMPOSTO por outros objetos das classes MOTOR e TANQUE.
    De fato, toda classe CARRO possuirá atributos pertencentes a essas outras duas classes.

    Mais ainda, podemos generalizar que TODAS AS CLASSES EM PYTHON são COMPOSIÇÕES. Isso tem a ver com
    a forma que o interpretador Python foi implementado e como ele lida com cada nome definido no espaço
    de trabalho.
"""


# %% POLIMORFISMO
"""
    Polimorfismo refere-se a habilidade de um mesmo NOME de atributo, ou método, existir dentro de diferentes
    objetos da mesma classe, ou ainda de objetos de classes diferentes, e representarem VALORES ou AÇÕES
    diferentes dentro de cada objeto. Por exemplo:
"""

class Brinquedo:
    def brincar(self):
        pass


class Carrinho(Brinquedo):
    def brincar(self):
        print('VRRUM! VRRUUUMM!!!')


class Dinossauro(Brinquedo):
    def brincar(self):
        print('GRRAUR!! ROARR!!')


car = Carrinho()
dino = Dinossauro()

car.brincar()
dino.brincar()

# %%
class NaoBrinquedo:
    def __init__(self, nome):
        self.nome = nome

    def brincar(self):
        print(self.nome,"não é brinquedo!")

class Bebe(Pessoa):
    def __init__(self, nome, idade, brinquedo):
        super().__init__(nome, idade)
        self.brinquedo = brinquedo

    def brincar(self):
        print(self.nome,"está brincando!")
        return

    def brincar_com(self):
        self.brincar()
        print("com a", self.brinquedo.nome)
        self.brinquedo.brincar()
        return


chaveFenda = NaoBrinquedo("Chave de fenda")
nene = Bebe('Ceci', 1, chaveFenda)

nene.brincar()
nene.brincar_com()


# %% ENCAPSULAMENTO
"""
    Esta é uma prática da OOP para proteger, ou esconder, os atributos do objeto do acesso direto pelo usuário.
    Isso geralmente é feito através de métodos chamados "getters" e "setters", ou coletores e definidores,
    respectivamente.

    O encapsulamento é uma forma de garantir que um determinado dado seja alterado sempre e somente da mesma
    forma, passando pelos mesmos processos e, assim, garantir que esteja sempre coerente com sua função.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):
        if type(novoNome) is not str:
            print("Meu nome precisa ser um texto!")
        else:
            self._nome = novoNome
        return

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, novaIdade):
        if type(novaIdade) not in [int, float]:
            print("Minha idade precisa ser um número!")
        else:
            self._idade = int(novaIdade)
        return


pess = Pessoa("Guto", 22)
pess.nome = 2
print(pess.nome)

pess.nome = 'Au'
print(pess.nome)
# %% PARTE 5

# Um exemplo prático! Vamos CODAR???
