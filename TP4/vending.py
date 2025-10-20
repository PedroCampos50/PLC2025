import json
import lexer as lex
import sys

f=open("stock.json", "r")
stock = json.load(f)

saldo = 0
running = True


def get_saldo(valor):
    e = valor // 100
    c = valor % 100
    if e > 0:
        return f"{int(e)}e{int(c)}c"
    else:
        return f"{int(c)}c"

def troco(valor):
    moedas = [200,100,50,20,10,5,2,1]
    resultado = []
    for moeda in moedas:
        qtd = valor // moeda
        if qtd > 0:
            valor -= qtd * moeda
            if moeda >= 100:
                resultado.append(f"{qtd} x {moeda//100}e")
            else:
                resultado.append(f"{qtd} x {moeda}c")
    return "Pode retirar o troco: " + ", ".join(resultado) + "."

# START MAQUINA

print("maq: Bom dia. Estou disponível para atender o seu pedido.")

for linha in sys.stdin:

    lex.lexer.input(linha)

    for tok in lex.lexer:
        if tok.type == 'LISTAR':
            saida = "maq:\n"
            saida += f"{'cod':<5} | {'nome':<15} | {'quantidade':<10} | {'preco':<5}\n"
            for p in stock["stock"]:
                saida += f"{p['cod']:<5} | {p['nome']:<15} | {p['quant']:<10} | {p['preco']:<5.2f}€\n"
            saida += "\nSaldo = " + get_saldo(saldo) + "\n"
            print (saida)

        elif tok.type == 'EURO':
            saldo += int(tok.value[:-1]) * 100

        elif tok.type == 'CENT':
            saldo += int(tok.value[:-1])

        elif tok.type == 'FIM_MOEDA':
            print("maq: Saldo = " + get_saldo(saldo))
        
        elif tok.type == 'CODIGO':
            produto = None
            for p in stock["stock"]:
                if p['cod'] == tok.value:
                    produto = p
                    break
            
            if not produto or produto['quant'] <= 0:
                print ("maq: Produto inexistente ou esgotado.")
            
            elif produto['preco'] * 100 <= saldo:
                saldo -= int(produto['preco'] * 100)
                produto['quant'] -= 1
                print (f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                print ("maq: Saldo = " + get_saldo(saldo))
            
            else:   #saldo insuficiente
                x = int(produto['preco'] * 100) #saldo em falta
                print("maq: Saldo insuficiente para satisfazer o seu pedido.")
                print(f"maq: Saldo = {get_saldo(saldo)}; Pedido = {get_saldo(x)}")
        
        elif tok.type == 'SAIR':
            print(troco(saldo))
            print ("maq: Até à próxima")
            f = open("stock.json", "w")
            json.dump(stock,f, indent=4)
            f.close()
            running = False

    if not running:
        break            