

historico = []  # cada compra: [valor_original, idade, valor_final]

print("=== PDV com Descontos ===")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    
    valor = float(input("Valor da compra (R$): "))
    while valor < 0:
        print("Aviso: o valor nao pode ser negativo. Tente novamente.")
        valor = float(input("Valor da compra (R$): "))

    if valor == 0:
        break

    
    idade = int(input("Idade do cliente: "))
    while idade < 0:
        print("Aviso: a idade nao pode ser negativa. Tente novamente.")
        idade = int(input("Idade do cliente: "))

    valor_final = valor

   
    if idade >= 65:
        valor_final = valor_final * 0.8


    if valor_final > 100:
        valor_final = valor_final * 0.9

    valor_final = round(valor_final, 2)
    historico.append([valor, idade, valor_final])

    print(f"Valor final: R$ {valor_final:.2f}\n")

total_bruto = 0
total_final = 0
for compra in historico:
    total_bruto = total_bruto + compra[0]
    total_final = total_final + compra[2]
total_descontos = total_bruto - total_final

print("\n=== Resumo do dia ===")
print(f"Compras registradas: {len(historico)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
