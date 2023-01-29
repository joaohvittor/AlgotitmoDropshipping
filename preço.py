nome_produto = str(input('Qual é o nome do produto? \n'))
preco_fornecedor = float(input(f'Qual é o preço do produto {nome_produto}  no fornecedor? \n'))
frete_fornecedor = float(input(f'Qual é o preço do frete do produto {nome_produto} no fornecedor? \n'))
print (f'==================================================================')
primeiracondicao = str(input(f'O PREÇO DO PRODUTO {nome_produto} É {preco_fornecedor} E O FRETE {frete_fornecedor} ? ')) 
if primeiracondicao == 's':
    morcap = preco_fornecedor * 2.5
    print(f'Preço Ideal para o produto {morcap} ')
    taxa_mercado_pago = (morcap*5)/100
    print(f'Preço do produto com a taxa do mercado pago que é o gateway de pagamento : {taxa_mercado_pago}')   
    preco_total_fornecedor = morcap + frete_fornecedor
    print(f'Preço total com o frete : {preco_total_fornecedor}')
    preco_para_venda = preco_total_fornecedor + taxa_mercado_pago
    dolar_atual = 6.00
    preco_dolar = preco_para_venda*dolar_atual   
    imposto_lucro_bruto = (preco_para_venda*15)/100
    preco_ideal_venda = imposto_lucro_bruto + preco_para_venda
    preco_ideal_dolar = preco_ideal_venda * 6
    print(f'Preço ideal para venda : R$ {preco_ideal_venda}, porém,caso o produto tenha sido calculado em dolar, o preço ideal se torna {preco_ideal_dolar}') 
elif primeiracondicao == 'n':
    segundacondicional = str(input('Voce deseja corrigir os valores? \n '))
    if segundacondicional == 's':
        terceiracondicional = str(input('Qual valor voce quer corrigir? Para corrigir o frete digite "frete" e para corrigir o valor do produto digite "produto" \n '))
        if terceiracondicional == 'frete':
            novo_valor_frete = float(input(f'Digite o novo valor para o frete do produto {nome_produto} \n '))
            novo_valor_frete == frete_fornecedor
            morcap = preco_fornecedor * 2.5
            print(f'Preço Ideal para o produto {morcap} ')
            taxa_mercado_pago = (morcap*5)/100
            print(f'Preço do produto com a taxa do mercado pago que é o gateway de pagamento : {taxa_mercado_pago}')   
            preco_total_fornecedor = morcap + frete_fornecedor
            print(f'Preço total com o frete : {preco_total_fornecedor}')
            preco_para_venda = preco_total_fornecedor + taxa_mercado_pago
            dolar_atual = 6.00
            preco_dolar = preco_para_venda*dolar_atual   
            imposto_lucro_bruto = (preco_para_venda*15)/100
            preco_ideal_venda = imposto_lucro_bruto + preco_para_venda
            preco_ideal_dolar = preco_ideal_venda * 6
            print(f'Preço ideal para venda : R$ {preco_ideal_venda}, porém,caso o produto tenha sido calculado em dolar, o preço ideal se torna {preco_ideal_dolar}')
        elif terceiracondicional == 'produto':
            novo_valor_produto = float(input(f'Digite o novo valor para o valor do produto {nome_produto} \n '))
            novo_valor_produto == preco_fornecedor
            morcap = preco_fornecedor * 2.5
            print(f'Preço Ideal para o produto {morcap} ')
            taxa_mercado_pago = (morcap*5)/100
            print(f'Preço do produto com a taxa do mercado pago que é o gateway de pagamento : {taxa_mercado_pago}')   
            preco_total_fornecedor = morcap + frete_fornecedor
            print(f'Preço total com o frete : {preco_total_fornecedor}')
            preco_para_venda = preco_total_fornecedor + taxa_mercado_pago
            dolar_atual = 6.00
            preco_dolar = preco_para_venda*dolar_atual   
            imposto_lucro_bruto = (preco_para_venda*15)/100
            preco_ideal_venda = imposto_lucro_bruto + preco_para_venda
            preco_ideal_dolar = preco_ideal_venda * 6
            print(f'Preço ideal para venda : R$ {preco_ideal_venda}, porém,caso o produto tenha sido calculado em dolar, o preço ideal se torna {preco_ideal_dolar}')
        else:
                print (f'==================================================================')
                print('OPÇÃO INVALIDA, REINICIE O ALGORITMO POR FAVOR !!!')    
                print (f'==================================================================')
    elif segundacondicional == 'n':
          morcap = preco_fornecedor * 2.5
          print(f'Preço Ideal para o produto {morcap} ')
          taxa_mercado_pago = (morcap*5)/100
          print(f'Preço do produto com a taxa do mercado pago que é o gateway de pagamento : {taxa_mercado_pago}')   
          preco_total_fornecedor = morcap + frete_fornecedor
          print(f'Preço total com o frete : {preco_total_fornecedor}')
          preco_para_venda = preco_total_fornecedor + taxa_mercado_pago
          dolar_atual = 6.00
          preco_dolar = preco_para_venda*dolar_atual   
          imposto_lucro_bruto = (preco_para_venda*15)/100
          preco_ideal_venda = imposto_lucro_bruto + preco_para_venda
          preco_ideal_dolar = preco_ideal_venda * 6
          print(f'Preço ideal para venda : R$ {preco_ideal_venda}, porém,caso o produto tenha sido calculado em dolar, o preço ideal se torna {preco_ideal_dolar}')
    else:
               print (f'==================================================================')
               print('OPÇÃO INVALIDA, REINICIE O ALGORITMO POR FAVOR !!!')    
               print (f'==================================================================')
else:
    print (f'==================================================================')
    print('OPÇÃO INVALIDA, REINICIE O ALGORITMO POR FAVOR !!!')    
    print (f'==================================================================')
#projeções
qntd_vendas = int(input('Quantas vendas deseja usar nesta projeção? \n'))
lucro_diario = (qntd_vendas*1) * preco_ideal_venda
lucro_semanal = (qntd_vendas*7) * preco_ideal_venda
lucro_mensal = (qntd_vendas*30) * preco_ideal_venda
lucro_bimestrallucro_ = (qntd_vendas*60) * preco_ideal_venda
print (f'==================================================================')
print(f'PROJEÇÃO DE LUCRO  || DIARIO ||  R$ {lucro_diario}        || EM 01 DIA   || COM {qntd_vendas} VENDAS ')   
print(f'PROJEÇÃO DE LUCRO  || SEMANAL||  R$ {lucro_semanal}        || EM 07 DIAS   || COM {qntd_vendas} VENDAS ')   
print(f'PROJEÇÃO DE LUCRO  || MENSAL ||  R$ {lucro_mensal}        || EM 30 DIAS   || COM {qntd_vendas} VENDAS ')   
print(f'PROJEÇÃO DE LUCRO  || B-MES  ||  R$ {lucro_bimestrallucro_}  || EM 60 DIAS   || COM {qntd_vendas} VENDAS ')   
 
print (f'==================================================================')