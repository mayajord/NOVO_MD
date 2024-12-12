def listar_eventos(events):
    i = 1
    for evento in events:
        print(f"{i}. Nome: {evento[0]} / Descrição: {evento[1]} / Data: {evento[2]} / Local: {evento[3]} / Valor: R${evento[4]}")
        i += 1

def proc_eventos(even,events):
    for evento in events:
        if evento[0] == even:
            print(f'(f" Nome: {evento[0]} / Descrição: {evento[1]} '
                  f'/ Data: {evento[2]} / Local: {evento[3]} / Valor: R${evento[4]}')
            return
    print("Evento não encontrado.")
