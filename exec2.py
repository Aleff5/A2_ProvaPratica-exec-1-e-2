
import pandas as pd


class FolhaPagamento:
    def __init__(self):
        self.funcionarios = []
        self.total_descontos = 0
        self.total_salario_bruto = 0
        self.total_salario_liquido = 0

    def menu_principal(self):
        while True:
            print("Menu Principal:")
            print("1. Cadastrar Funcionário")
            print("2. Calcular Imposto de Renda")
            print("3. Imprimir Relatório")
            print("4. Sair")

            escolha = input("Escolha uma opção:")

            if escolha == '1':
                self.cadastrar_funcionario()
            elif escolha == '2':
                self.calcular_imposto_renda()
            elif escolha == '3':
                self.imprimir_relatorio()
            elif escolha == '4':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_funcionario(self):
        nome = input("Nome do funcionário: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        horas_trabalhadas = float(input("Horas trabalhadas: "))

        self.funcionarios.append({'Nome': nome, 'Cargo': cargo, 'Salário': salario, 'Horas Trabalhadas': horas_trabalhadas})
        print("\nFuncionário cadastrado com sucesso!\n")

    def calcular_imposto_renda(self):
        for funcionario in self.funcionarios:
            salario = funcionario['Salário']
            if salario <= 1500:
                desconto = 0
            elif salario <= 3000:
                desconto = salario * 0.15
            elif salario <= 5000:
                desconto = salario * 0.20
            else:
                desconto = salario * 0.27

            funcionario['Desconto IR'] = desconto
            funcionario['Salário Líquido'] = salario - desconto

            self.total_descontos += desconto
            self.total_salario_bruto += salario
            self.total_salario_liquido += funcionario['Salário Líquido']
        print('\nimposta calculado com sucesso. RECEITA FEDERAL AGRADECE, OTARIO!!!\n')

    def imprimir_relatorio(self):
        df = pd.DataFrame(self.funcionarios)
        print("\nRelatório de Folha de Pagamento:")
        print(df)
        print("\nTotais:")
        print("Total de Descontos de IR: R$", self.total_descontos)
        print("Total de Salário Bruto: R$", self.total_salario_bruto)
        print("Total de Salário Líquido: R$", self.total_salario_liquido)

       
        with open("folha_pag.txt", "w") as file:
            file.write("Relatório de Folha de Pagamento:\n")
            file.write(df.to_string() + "\n\n")
            file.write("Totais:\n")
            file.write("Total de Descontos de IR: R$ " + str(self.total_descontos) + "\n")
            file.write("Total de Salário Bruto: R$ " + str(self.total_salario_bruto) + "\n")
            file.write("Total de Salário Líquido: R$ " + str(self.total_salario_liquido) + "\n")

        print("Relatório salvo em 'folha_pag.txt'.\n")

if __name__ == "__main__":
    folha_pagamento = FolhaPagamento()
    folha_pagamento.menu_principal()


