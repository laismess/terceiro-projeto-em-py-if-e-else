# Pede para o usuário digitar o valor da compra e guarda o valor
valor_total = float(input("Digite o valor total da sua compra: R$ "))
desconto = 0

# Verifica qual vai ser o valor do desconto recebido
if valor_total < 200:
    desconto = 0.05
    print("Recebe um desconto de 5%")

elif valor_total < 300:
    desconto = 0.10
    print("Recebe um desconto de 10%")

else:
    desconto = 0.15
    print("Recebe um desconto de 15%")

# Calcula o valor do desconto
valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto

# Exibi o desconto
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")