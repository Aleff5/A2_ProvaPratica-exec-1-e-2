import matplotlib.pyplot as plt


class Armazem:
    def __init__(self):
        self.data = []
    
    def menu_principal(self):
        while True:
            print("Menu Principal:")
            print("1. Registrar Venda")
            print("2. Calcular Faturamento")
            print("3. Exibir Percentuais de Vendas")
            print("4. Gravar Dados em Arquivo")
            print("5. Ler Dados do Arquivo")
            print("6. Gerar Gráfico das 5 Mercadorias Mais Vendidas")
            print("7. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                self.registrar_venda()
            elif escolha == '2':
                self.calcular_faturamento()
            elif escolha == '3':
                self.exibir_percentuais_vendas()
            elif escolha == '4':
                self.gravar_dados_em_arquivo()
            elif escolha == '5':
                self.ler_dados_do_arquivo()
            elif escolha == '6':
                self.gerar_grafico()
            elif escolha == '7':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def registrar_venda(self):
        mercadoria = input("Número da mercadoria (1 a 100): ")
        quantidade = int(input("Quantidade vendida: "))
        preco = float(input("Preço de venda: "))
        
        self.data.append({'Mercadoria': mercadoria, 'Quantidade': quantidade, 'Preço': preco})
        print("Venda registrada com sucesso!")
    
    def calcular_faturamento(self):
        faturamento = sum(item['Quantidade'] * item['Preço'] for item in self.data)
        print("Faturamento mensal: R$ {:.2f}".format(faturamento))
    
    def exibir_percentuais_vendas(self):
        total_vendido = sum(item['Quantidade'] for item in self.data)
        percentuais = [(item['Quantidade'] * item['Preço'] / total_vendido) for item in self.data]
        
        for i, item in enumerate(self.data):
            print(f"Mercadoria {item['Mercadoria']}: {percentuais[i] * 100:.2f}%")
    
    def gravar_dados_em_arquivo(self):
        with open('dados_vendas.txt', 'w') as file:
            for item in self.data:
                file.write(f"{item}\n")
        print("Dados gravados em arquivo.")
    
    def ler_dados_do_arquivo(self):
        try:
            with open('dados_vendas.txt', 'r') as file:
                for line in file:
                    print(*line.strip())  # Exibe os dados do arquivo na tela
            print("Dados lidos do arquivo.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
    
    def gerar_grafico(self):
        top5 = sorted(self.data, key=lambda item: item['Quantidade'], reverse=True)[:5]
        
        mercadorias = [item['Mercadoria'] for item in top5]
        quantidades = [item['Quantidade'] for item in top5]
        
        plt.bar(mercadorias, quantidades)
        plt.xlabel("Mercadoria")
        plt.ylabel("Quantidade Vendida")
        plt.title("As 5 Mercadorias Mais Vendidas")
        plt.show()

if __name__ == "__main__":
    armazem = Armazem()
    armazem.menu_principal()
