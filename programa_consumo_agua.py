#paga 1.65 por cada litro usado
#se consumir mais que 70% da capacidade paga multa de 10%
#se consumir tudo paga multa de 15%

litros_capacidade = input("Digite a capacidade de litros da caixa d'água: ")
litros_usados = input("Digite o consumo de litros: ")

litros_capacidade = int(litros_capacidade)
litros_usados = int(litros_usados)

valor_litro_consumido = 1.65
multa = 0
valor_pagar = litros_usados * valor_litro_consumido
porcentagem_usada = (litros_usados / litros_capacidade) * 100

if litros_capacidade > litros_usados:
    if porcentagem_usada >= 70:
        cor_bandeira = "laranja"
        multa = valor_pagar * 0.1
        valor_pagar = multa + valor_pagar
    else:
        cor_bandeira = "azul"
else:
    cor_bandeira = "vermelha"
    multa = valor_pagar * 0.15
    valor_pagar = multa + valor_pagar
    
economia = "ruim" if cor_bandeira == "laranja" else "ótima"

if cor_bandeira == "vermelha":
    economia = "péssima"

mensagem_relatorio = f""" 
Multa: R${multa:.2f}
Consumo: {litros_usados} litros
Economia: {economia}
Valor à pagar: R${valor_pagar:.2f}
"""
print(mensagem_relatorio)

