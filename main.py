import tkinter as tk #importando a biblioteca tkinter para a interface

class Tela: #janela pincipal da calculadora
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("Calculadora de operações básicas") #Adicionando o titulo da janela principal
        self.tela.resizable(width=False, height=False) #impede o redimensionamento da tela

        self.Res = "" #armazena o digito
        self.WIDTH = 8 #largura do botão
        self.HEIGHT = 2 #altura 
        self.Fonte = "Arial 12 bold" #Tipo da fonte do texto

        self.auxResultado = tk.StringVar() #armazena o resultado
        self.auxResultado.set("...") #inicio no visor (ex: calcule...)
        self.lbResultado = tk.Label(self.tela, textvariable=self.auxResultado, font="Verdana 12 bold", borderwidth=5)
        self.lbResultado.grid(row=0, columnspan=4)

        self.criar_botoes()

        self.tela.mainloop() #loop principal

    def atualizar(self, valor): #Atualiza o visor de acordo com os digitos
        self.Res += valor
        self.auxResultado.set(self.Res)

    def calcular(self):
        try:
            expressao = self.Res.replace('x', '*').replace('^', '**') #substitui as operações
            resultado = self.avaliar_expressao(expressao)
            if resultado is None:
                self.auxResultado.set("Erro") #Caso tenha algum erro na digitação
                self.Res = ""
            else:
                self.auxResultado.set(str(round(resultado, 5))) #arredonda 5 casas
                self.Res = str(resultado) #armazena o resultado
        except Exception:
            self.auxResultado.set("Erro")
            self.Res = ""

    def avaliar_expressao(self, expr):
        try:
            #Checa se a expressão é válida e segura de avaliar
            resultado = eval(expr, {"__builtins__": None}, {})
            return resultado
        except:
            return None

    def criar_botoes(self): #lista de definição dos botões
        botoes = [
            ('0', 1, 0), ('1', 1, 1), ('2', 1, 2),
            ('3', 2, 0), ('4', 2, 1), ('5', 2, 2),
            ('6', 3, 0), ('7', 3, 1), ('8', 3, 2),
            ('9', 4, 0), ('+', 4, 1), ('-', 4, 2),
            ('/', 5, 0), ('x', 5, 1), ('^', 5, 2),
            ('=', 5, 3), ('.', 6, 0), ('C', 6, 1), ('-', 6, 2)
        ]

            #condições deo botão
        for (texto, linha, coluna) in botoes:
            if texto == "=": 
                comando = self.calcular
                cor = "gray"
            elif texto == "C":
                comando = self.limpar
                cor = "red"
            else: #atualiza com o valor do botão
                comando = lambda val=texto: self.atualizar(val)
                cor = "light blue" if texto in "+-x/^" else None

            tk.Button(self.tela, text=texto, width=self.WIDTH, height=self.HEIGHT,
                      font=self.Fonte, command=comando, bg=cor).grid(row=linha, column=coluna, padx=2, pady=2)
    
    #limpa quando é digitado o c
    def limpar(self):
        self.Res = ""
        self.auxResultado.set("...") #atualiza o visor

Tela() #inicialização da calculadora