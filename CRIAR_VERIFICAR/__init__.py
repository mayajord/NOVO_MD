def desconto_inscr(idade,valor_curso):
    if idade<18:
        cart = input('O inscrito de menor possui tem carteirinha de estudante? Digite: Sim ou Nao')
        if cart == 'Sim':
            print('PARABENS,  DESCONTÃO DE 50% SERÁ APLICADO')
            desconto = float(valor_curso) * 0.5
            print(f'Seu valor a pagar será de: {desconto},00')
            return desconto
        else:
            print(f'Não foi possível aplicar desconto. Valor a pagar: R${valor_curso},00')
            return valor_curso
    else:
        print(f'Não foi possível aplicar desconto. Valor a pagar: R${valor_curso},00')
        return valor_curso


def novo_evento(events):
    while True:
        idade = int(input('Digite sua idade'))
        if idade >= 18:
            curso = input('Digite o nome do seu curso: ')
            descricao = input('Faça um breve resumo do que terá no curso: ')
            data = input('Digite a data do seu evento: ')
            local = input('Onde será o local do evento: ')
            valor_curso = float(input('Digite quanto será o valor do curso: '))
            ID = int(input('Digite um ID de identificação do seu curso'))
            events.append([curso, descricao, data, local, valor_curso, ID])
            print('DEU TUDO CERTO')
            break
        else:
            print('---JOVEM DEMAIS  PARA MINISTRAR UM EVENTO, VOLTE DAQUI A UNS ANOS------')
            break


def veri_criador(events, id_evento):
    ind_rem = -1
    for evento in events:
        ind_rem += 1
        if evento[5] == id_evento:
            break
    return ind_rem
