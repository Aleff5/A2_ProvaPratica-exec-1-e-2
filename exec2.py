# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# class Funcionario:
#     def __init__(self, nome, cargo, salario, horas_trabalhadas):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario
#         self.horas_trabalhadas = horas_trabalhadas

#     def calcular_desconto_ir(self):
#         if self.salario <= 1500:
#             return 0
#         elif 1500 < self.salario <= 3000:
#             return 0.15 * self.salario
#         elif 3000 < self.salario <= 5000:
#             return 0.20 * self.salario
#         else:
#             return 0.27 * self.salario

#     def calcular_salario_liquido(self):
#         desconto_ir = self.calcular_desconto_ir()
#         salario_liquido = self.salario - desconto_ir
#         return salario_liquido, desconto_ir

# def menu():
#     funcionarios = []
#     acumulado_desconto_ir = 0
#     acumulado_salario_bruto = 0
#     acumulado_salario_liquido = 0

#     while True:
#         print("\nMenu Principal:")
#         print("1. Adicionar funcionário")
#         print("2. Ler dados do arquivo")
#         print("3. Calcular imposto de renda e gerar relatório")
#         print("4. Sair")
        
#         escolha = input("Escolha uma opção: ")

#         if escolha == '1':
#             nome = input("Nome do funcionário: ")
#             cargo = input("Cargo do funcionário: ")
#             salario = float(input("Salário do funcionário: "))
#             horas_trabalhadas = int(input("Horas trabalhadas do funcionário: "))
#             funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
#             funcionarios.append(funcionario)
#             print("Funcionário adicionado com sucesso!")

#         elif escolha == '2':
#             try:
#                 df = pd.read_csv('folha_pag.csv')
#                 funcionarios = [Funcionario(row['nome'], row['cargo'], row['salario'], row['horas_trabalhadas']) for index, row in df.iterrows()]
#                 print("Dados lidos do arquivo com sucesso!")
#             except FileNotFoundError:
#                 print("Arquivo não encontrado. Certifique-se de que ele existe.")

#         elif escolha == '3':
#             if not funcionarios:
#                 print("Nenhum funcionário cadastrado.")
#             else:
#                 for funcionario in funcionarios:
#                     salario_liquido, desconto_ir = funcionario.calcular_salario_liquido()
#                     acumulado_desconto_ir += desconto_ir
#                     acumulado_salario_bruto += funcionario.salario
#                     acumulado_salario_liquido += salario_liquido
#                 gerar_relatorio(funcionarios, acumulado_desconto_ir, acumulado_salario_bruto, acumulado_salario_liquido)

#         elif escolha == '4':
#             break

#         else:
#             print("Opção inválida. Por favor, escolha uma opção válida.")

# def gravar_dados(funcionarios):
#     data = {
#         'nome': [funcionario.nome for funcionario in funcionarios],
#         'cargo': [funcionario.cargo for funcionario in funcionarios],
#         'salario': [funcionario.salario for funcionario in funcionarios],
#         'horas_trabalhadas': [funcionario.horas_trabalhadas for funcionario in funcionarios]
#     }
#     df = pd.DataFrame(data)
#     df.to_csv('folha_pag.csv', index=False)
#     print("Dados gravados no arquivo 'folha_pag.csv' com sucesso!")

# def gerar_relatorio(funcionarios, acumulado_desconto_ir, acumulado_salario_bruto, acumulado_salario_liquido):
#     data = {
#         'Nome': [funcionario.nome for funcionario in funcionarios],
#         'Cargo': [funcionario.cargo for funcionario in funcionarios],
#         'Salário Bruto': [funcionario.salario for funcionario in funcionarios],
#         'Horas Trabalhadas': [funcionario.horas_trabalhadas for funcionario in funcionarios],
#         'Desconto de IR': [funcionario.calcular_desconto_ir() for funcionario in funcionarios],
#         'Salário Líquido': [funcionario.calcular_salario_liquido()[0] for funcionario in funcionarios]
#     }
#     df = pd.DataFrame(data)
#     print("\nRelatório de Funcionários:")
#     print(df)
#     print(f"Total de Descontos de IR: R${acumulado_desconto_ir:.2f}")
#     print(f"Total de Salário Bruto: R${acumulado_salario_bruto:.2f}")
#     print(f"Total de Salário Líquido: R${acumulado_salario_liquido:.2f}")
#     gerar_grafico(df)

# def gerar_grafico(df):
#     fig, ax = plt.subplots()
#     ax.bar(df['Nome'], df['Desconto de IR'])
#     ax.set_ylabel('Desconto de IR')
#     ax.set_title('Desconto de IR por Funcionário')
#     plt.xticks(rotation=45)
#     plt.show()

# if __name__ == '__main__':
#     menu()



# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np

# # class FolhaPagamento:
# #     def __init__(self):
# #         self.funcionarios = []
# #         self.total_descontos = 0
# #         self.total_salario_bruto = 0
# #         self.total_salario_liquido = 0

# #     def menu_principal(self):
# #         while True:
# #             print("Menu Principal:")
# #             print("1. Cadastrar Funcionário")
# #             print("2. Calcular Imposto de Renda")
# #             print("3. Imprimir Relatório")
# #             print("4. Sair")
            
# #             escolha = input("Escolha uma opção: ")
            
# #             if escolha == '1':
# #                 self.cadastrar_funcionario()
# #             elif escolha == '2':
# #                 self.calcular_imposto_renda()
# #             elif escolha == '3':
# #                 self.imprimir_relatorio()
# #             elif escolha == '4':
# #                 break
# #             else:
# #                 print("Opção inválida. Tente novamente.")

# #     def cadastrar_funcionario(self):
# #         nome = input("Nome do funcionário: ")
# #         cargo = input("Cargo: ")
# #         salario = float(input("Salário: "))
# #         horas_trabalhadas = float(input("Horas trabalhadas: "))
        
# #         self.funcionarios.append({'Nome': nome, 'Cargo': cargo, 'Salário': salario, 'Horas Trabalhadas': horas_trabalhadas})
# #         print("Funcionário cadastrado com sucesso!")

# #     def calcular_imposto_renda(self):
# #         for funcionario in self.funcionarios:
# #             salario = funcionario['Salário']
# #             if salario <= 1500:
# #                 desconto = 0
# #             elif salario <= 3000:
# #                 desconto = salario * 0.15
# #             elif salario <= 5000:
# #                 desconto = salario * 0.20
# #             else:
# #                 desconto = salario * 0.27

# #             funcionario['Desconto IR'] = desconto
# #             funcionario['Salário Líquido'] = salario - desconto

# #             self.total_descontos += desconto
# #             self.total_salario_bruto += salario
# #             self.total_salario_liquido += funcionario['Salário Líquido']
    
# #     def imprimir_relatorio(self):
# #         df = pd.DataFrame(self.funcionarios)
# #         print("\nRelatório de Folha de Pagamento:")
# #         print(df)
# #         print("\nTotais:")
# #         print("Total de Descontos de IR: R$", self.total_descontos)
# #         print("Total de Salário Bruto: R$", self.total_salario_bruto)
# #         print("Total de Salário Líquido: R$", self.total_salario_liquido)

# # if __name__ == "__main__":
# #     folha_pagamento = FolhaPagamento()
# #     folha_pagamento.menu_principal()

import pandas as pd

# ALUNOS: ALEFF 22308138 E LUIZ FELIPE 22300737

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


