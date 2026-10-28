# PDV com Descontos (Nível 1)

## Enunciado

Criar em Python a lógica de um PDV (Ponto de Venda) que aplica descontos progressivos. O programa deve:

- Receber o valor da compra (número decimal) e a idade do cliente (número inteiro).
- Dar 20% de desconto se o cliente tiver 65 anos ou mais.
- Dar mais 10% se o valor, já com o desconto da idade, for maior que R$ 100.
- Mostrar o valor final formatado em reais, com duas casas decimais (ex.: R$ 144.00).
- Permitir várias compras seguidas, encerrando quando o valor digitado for 0.
- Guardar cada compra numa lista com `.append()` e, no final, mostrar um resumo com a quantidade de compras, o total bruto, o total de descontos e o total final.
- Avisar e pedir de novo quando o valor ou a idade forem negativos.
- Não usar `def` nem `try/except`.

## O que o código faz

É um caixa de loja simples. Você digita o valor da compra e a idade do cliente, e o programa calcula quanto ele vai pagar. Quem tem 65 anos ou mais ganha 20% de desconto. Se depois disso a compra ainda passar de R$ 100, ganha mais 10%. Dá para registrar várias compras seguidas e, no fim, o programa mostra um resumo do dia.

## Como ele faz

1. Pede o valor da compra. Se for negativo, avisa e pede de novo. Se for 0, encerra.
2. Pede a idade. Se for negativa, avisa e pede de novo.
3. Se a idade for 65 ou mais, tira 20%.
4. Se o valor (já com o desconto da idade) for maior que 100, tira mais 10%.
5. Mostra o valor final e guarda a compra numa lista com `.append()`.
6. Quando o usuário digita 0, soma tudo da lista e mostra o resumo.

## Como rodar

```bash
python pdv.py
```

## Testes

Rodei o programa com estes 10 casos e anotei o que apareceu no console:

| Caso | Valor  | Idade | Valor final |
|------|-------:|------:|------------:|
| 1    | 50.00  | 30    | R$ 50.00    |
| 2    | 50.00  | 65    | R$ 40.00    |
| 3    | 150.00 | 30    | R$ 135.00   |
| 4    | 150.00 | 70    | R$ 108.00   |
| 5    | 125.00 | 70    | R$ 100.00   |
| 6    | 100.00 | 30    | R$ 100.00   |
| 7    | 101.00 | 30    | R$ 90.90    |
| 8    | 130.00 | 65    | R$ 93.60    |
| 9    | 80.00  | 80    | R$ 64.00    |
| 10   | 200.00 | 64    | R$ 180.00   |

Depois de digitar 0, a saída foi:

```
=== Resumo do dia ===
Compras registradas: 10
Total bruto: R$ 1136.00
Total de descontos: R$ 174.50
Total final: R$ 961.50
```
