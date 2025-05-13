import unittest
from tkinter import Tk
from main import Tela

class TestCalculadora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.app = Tela()
        cls.root.withdraw()  # Esconde a janela principal para os testes

    def test_adicao_simples(self):
        self.app.limpar()
        self.app.atualizar("2+2")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "4")

    def test_subtracao_simples(self):
        self.app.limpar()
        self.app.atualizar("5-3")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "2")

    def test_multiplicacao_simples(self):
        self.app.limpar()
        self.app.atualizar("3x4")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "12")

    def test_divisao_simples(self):
        self.app.limpar()
        self.app.atualizar("10/2")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "5")

    def test_potenciacao_simples(self):
        self.app.limpar()
        self.app.atualizar("2^3")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "8")

    def test_operacoes_mistas(self):
        self.app.limpar()
        self.app.atualizar("2+3x4")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "14")

    def test_divisao_por_zero(self):
        self.app.limpar()
        self.app.atualizar("5/0")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "Erro")

    def test_numero_decimal(self):
        self.app.limpar()
        self.app.atualizar("0.5+0.5")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "1")

    def test_limpar_tela(self):
        self.app.atualizar("123")
        self.app.limpar()
        self.assertEqual(self.app.auxResultado.get(), "...")
        self.assertEqual(self.app.Res, "")

    def test_expressao_invalida(self):
        self.app.limpar()
        self.app.atualizar("2++2")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "Erro")

    def test_expressao_vazia(self):
        self.app.limpar()
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "Erro")

    def test_expressao_com_espacos(self):
        self.app.limpar()
        self.app.atualizar(" 2 + 2 ")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "4")

    def test_operacao_longa(self):
        self.app.limpar()
        self.app.atualizar("2+3x4-10/2+3^2")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "21")

    def test_numero_grande(self):
        self.app.limpar()
        self.app.atualizar("999999999x999999999")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "999999998000000000")

    def test_resultado_decimal(self):
        self.app.limpar()
        self.app.atualizar("10/3")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "3.33333")

    def test_expressao_com_parenteses(self):
        self.app.limpar()
        self.app.atualizar("(2+3)x4")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "20")

    def test_atualizacao_visor(self):
        self.app.limpar()
        self.app.atualizar("1")
        self.app.atualizar("+")
        self.app.atualizar("2")
        self.assertEqual(self.app.auxResultado.get(), "1+2")

    def test_botao_igual_repetido(self):
        self.app.limpar()
        self.app.atualizar("2+2")
        self.app.calcular()
        self.app.calcular()  # Chamar igual novamente
        self.assertEqual(self.app.auxResultado.get(), "4")

    def test_alternancia_operadores(self):
        self.app.limpar()
        self.app.atualizar("2++")
        self.app.atualizar("-")
        self.app.atualizar("3")
        self.app.calcular()
        self.assertEqual(self.app.auxResultado.get(), "-1")

    def test_visor_inicial(self):
        self.app.limpar()
        self.assertEqual(self.app.auxResultado.get(), "...")

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

if __name__ == "__main__":
    unittest.main()