import tkinter as tk
from tkinter import messagebox

# Valores fixos para agilizar o processo de precificação
DOLAR_ATUAL = 6.00  # Cotação do dólar
IMPOSTO_LUCRO_BRUTO = 0.15  # Imposto sobre o lucro bruto
TAXA_MERCADO_PAGO = 0.05  # Taxa do gateway de pagamento
MORCAP_MULTIPLICADOR = 1.5  # Margem de lucro sobre o custo do produto

# Custos gerais fixos
CUSTO_SHOPIFY = 39 * DOLAR_ATUAL  # Custo da Shopify em reais
CUSTO_INTERNET = 80.00  # Custo mensal da internet em reais
CUSTO_ENERGIA = 100.00  # Custo mensal da energia em reais
CUSTO_ANUNCIOS_META = 500.00  # Custo mensal com anúncios no Meta (em reais)
CUSTO_ANUNCIOS_TIKTOK = 300.00  # Custo mensal com anúncios no TikTok (em reais)

# Função para calcular o preço ideal
def calcular_preco_ideal(preco_fornecedor, frete_fornecedor, total_produtos):
    # Cálculo em dólar
    morcap = preco_fornecedor * MORCAP_MULTIPLICADOR
    taxa_mercado_pago = morcap * TAXA_MERCADO_PAGO
    preco_total_fornecedor = morcap + frete_fornecedor
    preco_para_venda = preco_total_fornecedor + taxa_mercado_pago
    imposto_lucro_bruto = preco_para_venda * IMPOSTO_LUCRO_BRUTO
    preco_ideal_venda = preco_para_venda + imposto_lucro_bruto

    # Distribuir custos gerais pelos produtos
    custo_geral_por_produto = (CUSTO_SHOPIFY + CUSTO_INTERNET + CUSTO_ENERGIA + CUSTO_ANUNCIOS_META + CUSTO_ANUNCIOS_TIKTOK) / total_produtos

    # Conversão para real e adição dos custos gerais
    preco_ideal_reais = (preco_ideal_venda * DOLAR_ATUAL) + custo_geral_por_produto
    return preco_ideal_reais

# Função para processar os dados do formulário
def processar_precificacao():
    try:
        nome_produto = entry_nome.get()
        preco_fornecedor = float(entry_preco.get())
        frete_fornecedor = float(entry_frete.get())
        total_produtos = int(entry_total_produtos.get())

        preco_ideal_reais = calcular_preco_ideal(preco_fornecedor, frete_fornecedor, total_produtos)

        # Exibir os resultados
        resultado = (f"Produto: {nome_produto}\n"
                    f"Preço ideal para venda no Brasil: R$ {preco_ideal_reais:.2f}\n"
                    f"(Inclui custos gerais distribuídos por {total_produtos} produtos)")
        messagebox.showinfo("Resultados", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos nos campos de preço, frete e quantidade de produtos.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Sistema de Precificação de Produtos")

# Rótulos e entradas
label_nome = tk.Label(root, text="Nome do Produto:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_preco = tk.Label(root, text="Preço do Fornecedor (em dólar):")
label_preco.grid(row=1, column=0, padx=10, pady=5)
entry_preco = tk.Entry(root, width=30)
entry_preco.grid(row=1, column=1, padx=10, pady=5)

label_frete = tk.Label(root, text="Frete do Fornecedor (em dólar):")
label_frete.grid(row=2, column=0, padx=10, pady=5)
entry_frete = tk.Entry(root, width=30)
entry_frete.grid(row=2, column=1, padx=10, pady=5)

label_total_produtos = tk.Label(root, text="Total de Produtos para Distribuir Custos:")
label_total_produtos.grid(row=3, column=0, padx=10, pady=5)
entry_total_produtos = tk.Entry(root, width=30)
entry_total_produtos.grid(row=3, column=1, padx=10, pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular Preço Ideal", command=processar_precificacao)
button_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar a interface
root.mainloop()
