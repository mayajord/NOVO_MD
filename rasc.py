from CADASTRO import *
from LISTAR_BUSCAR import *
from CRIAR_VERIFICAR import *
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


usuarios = [['maya', 'maya@.com', '123']]

events = [['Moda', 'Roupas', '12', 'Estúdio', '200', '40'], ['Vida', 'kaka', '34', 'dsls', '900', '5050'],
          ['ADS', 'tecnologia', '8', 'escola', '2000', '07']]

inscritos= {"Bianca": {
        "email": "bianca@.com",
        "curso": "Vida",
        "valor_final": 450
    },
    "Oliveira": {
        "email": "anaoliveira@.com",
        "curso": "Vida",
        "valor_final": 900
    },
    "Pedro Santos": {
        "email": "pedrosantos@example.com",
        "curso": "Vida",
        "valor_final": 900
    }
}

indesejados = {
    "joao@.com": {"nome": "João Silva"},
    "ana@.com": {"nome": "Ana Souza"}
}


op = -1
while op != 0:
    print('------------:)OLÁ,PRAZER EM TE RECEBER!CASO NÃO SEJA UM USUÁRIO FAÇA SEU CADASTRO(:-------------')
    print('1-Cadastrar usuário')
    print('2-Login')
    print('0-Sair do programa')

    op = int(input('Digite a opção desejada: '))

    if op == 1:
        cadastro_usuario(usuarios, indesejados)

    elif op == 2:
        print('.........OLÁ USUÁRIO, BOM REVER VOCE........´´(:')
        email = input('Digite seu e-mail para login: ')
        senha = input('Digite sua senha: ')

        if fazer_login(email, senha, usuarios):
            while not fazer_login(email, senha, usuarios):
                email = input('Digite seu e-mail para login: ')
                senha = input('Digite sua senha: ')
            print('Usuário validado')

            evento = -1
            while evento != 0:
                print('==============SEJA BEM VINDO A PLATAFORMA DE EVENTOS!===========')
                print('1-Exibir eventos')
                print('2-Incrição em evento')
                print('3-Criar Evento')
                print('4-Buscar evento')
                print('5-Remover Evento')
                print('6-Listar Participantes')
                print('7-Verificar valor arrecadado')
                print('8-Certificado')
                print('9-Reclamações')
                print('10-Adicionar participantes no evento')
                print('11-Gráfico dos participantes dos eventos')
                print('0-Sair')

                evento = int(input('Digite o número referente à sua escolha: '))

                if evento == 0:
                    break

                elif evento == 1:
                    listar_eventos(events)

                elif evento == 2:
                    print('xxxx..OS EVENTOS DISPONIVEIS SÃO..xxx')
                    listar_eventos(events)
                    inscr = int(input("Escolha um evento para detalhes (digite o número do evento): "))
                    if inscr >= 1 and inscr <= len(events):
                        nome = input("Digite seu nome: ")
                        while not nome_verdade(nome):
                            nome = input('Insira seu nome novamente: ')
                        idade = int(input('Digite sua idade:'))
                        email = input("Digite seu email: ")
                        while not email_verdade(email):
                            print("Insira um email válido com '@' e '.com'")
                            email = input('Insira seu email novamente: ')
                        print(email)
                        curso = input("Digite o nome do curso escolhido: ")
                        valor_curso = events[inscr - 1][4]
                        valor_final = desconto_inscr(idade, valor_curso)

                        inscritos[nome] = {
                            'email': email,
                            'curso': curso,
                            'valor_final': valor_final
                        }

                        print("´´´´´´INSCRIÇAO REALIZADA'''''!")
                        print(inscritos)
                    else:
                        print("Opção inválida.")

                elif evento == 3:
                    print(',.,.,,.,CRIAR EVENTO.,.,.,.')
                    novo_evento(events)

                elif evento == 4:
                    even = input('----OLÁ!!---'
                                 ' QUAL O NOME DO EVENTO QUE PROCURA?:')
                    proc_eventos(even, events)

                elif evento == 5:
                    print('{[{[{[DELETAR EVENTOS}]}]}]')
                    id_evento = input("Digite o ID do seu evento: ")
                    nome_evento = input("Digite o nome do seu evento: ")
                    ind_rem = -1
                    if veri_criador(events, id_evento):
                        events.pop(ind_rem)
                        print(f'EVENTO: "{nome_evento}" FOI REMOVIDO COM SUCESSO.')
                    else:
                        print('Operação cancelada.')

                elif evento == 6:
                    print('=========PROCURAR INSCRITOS==========')
                    id_evento = input("digite o ID do seu evento:")
                    nome_evento = input("digite o nome do seu evento:")
                    ind_rem = -1
                    if veri_criador(events, id_evento):
                        print(f'participantes inscritos no evento "{nome_evento} são":')
                        for nome_chave, info in inscritos.items():
                            if info.get('curso') == nome_evento:
                                print(f'Nome: {nome_chave}, Email: {info["email"]}\n')

                        salvar_arquivo = input('Você deseja salvar a lista em forma de arquivo? Sim ou Não? ')
                        if salvar_arquivo == 'Sim':
                            with open(f'{nome_evento}_participantes.txt','a') as arquivo:
                                arquivo.write(f'Nome: {nome_chave}, Email: {info["email"]}\n')

                elif evento == 7:
                    print('$VALOR TOTAL$')
                    id_evento = input("Digite o ID do seu evento: ")
                    nome_evento = input("Digite o nome do seu evento: ")
                    ind_rem = -1
                    if veri_criador(events, id_evento):
                        qtde = 0
                        soma = 0
                        for inscrito in inscritos.values():
                            if inscrito['curso'] == nome_evento:
                                soma += inscrito['valor_final']
                                qtde += 1
                        total_arrecadado = soma
                        print(f' O total arrecadado é R${total_arrecadado},0')


                elif evento == 8:
                    print('*-*-*CERTIFICADOS*-*-*')
                    participacao = input('Voce participou de algum evento?Digite Sim ou Nao:')
                    if participacao == 'Sim':
                        listar_eventos(events)
                        qual = int(input('Qual foi o evento? Digite o número do evento:'))
                        while qual < 1 or qual > len(events):
                            print("Número inválido. Tente novamente.")
                            participacao = input('Voce participou de algum evento?Digite Sim ou Nao:')
                        else:
                            nome1 = input("Digite seu nome: ")
                            evento_escolhido = events[qual - 1]
                            inscrito_encontrado = False
                            for nome_chave, evento in inscritos.items():
                                if nome_chave == nome1 and evento.get('curso') == evento_escolhido[0]:
                                    inscrito_encontrado = True
                                print(f'''
                                -----------------------------------------------------------------
                                                         CERTIFICADO
                                          Certificamos que {nome1} participou do minicurso
                                          {evento_escolhido[0]} no dia {evento_escolhido[2]}
                                          com carga total de 20 horas.
                                -----------------------------------------------------------------

                                                       ''')
                            imagem = Image.new("RGB", (800, 400), "black")
                            draw = ImageDraw.Draw(imagem)
                            fonte = ImageFont.truetype("arial.ttf", 20)
                            texto = f'''
                                CERTIFICADO
                                Certificamos que {nome1} participou do minicurso
                                {evento_escolhido[0]} no dia {evento_escolhido[2]}, com carga total de 20 horas.
                                '''
                            draw.multiline_text((50, 100), texto, fill="pink", font=fonte, spacing=10)
                            imagem.show()
                            imagem.save(f"certificado_{nome1.replace(' ', '_')}.png")
                            print(f"Certificado salvo como certificado_{nome1.replace(' ', '_')}.png")


                    else:
                        print(',,,Infelismente nao terá certificado,,,,')

                elif evento == 9:
                    print('........RECLAMAÇOES.........')
                    ouvidoria = input('Escreva aqui suas sugestões ou feedbacks para os proximos '
                                      'cursos ou para a plataforma:')

                    with open('feedbacks.txt', 'a') as arquivo:
                            arquivo.write(f"{ouvidoria}\n")
                    expor = input('Voce gosataria de ler os feedbacks da plataforma? Sim ou Nao?')
                    if expor == 'Sim':
                        with open('feedbacks.txt', 'r') as arquivo:
                            print('-------FEEDBACKS-------')
                            for feedbacks in arquivo:
                                print(feedbacks)

                elif evento == 10:
                    print('=========ADICIONAR PARTICIPANTE EM EVENTO==========')
                    listar_eventos(events)
                    numc = int(input('Digite o numero correpondente ao seu curso:'))
                    if numc < 1 or numc > len(events):
                        print("Número inválido. Tente novamente.")
                    id_evento = input("digite o ID do seu evento para assegurar que voce realmente é o criador:")
                    ind_rem = -1
                    if veri_criador(events, id_evento):
                        nome = input('Digite o nome do seu participante:')
                        nome_verdade(nome)
                        idade = int(input('Digite a idade do seu participante:'))
                        email = input("Digite o email do seu participante: ")
                        email_verdade(email)
                        valor_curso = events[numc - 1][4]
                        valor_final = desconto_inscr(idade, valor_curso)
                        curso = events[numc - 1][0]
                        inscritos[nome] = {
                            'email': email,
                            'curso': curso,
                            'valor_final': valor_final
                        }
                        print("´´´´´´INSCRIÇAO REALIZADA'''''!")
                        print(f"inscritos\n")
                    else:
                        print("Você não é o criador deste evento. Ação não permitida.")

                elif evento == 11:
                    cont_part = {}
                    for nome_chave, info in inscritos.items():
                        evento = info.get('curso')
                        if evento in cont_part:
                            cont_part[evento] += 1
                        else:
                            cont_part[evento] = 1

                    for curso, quantidade in cont_part.items():
                        print(f"Curso: {curso}, Participantes: {quantidade}")

                    curso = list(cont_part.keys())
                    quantidade = list(cont_part.values())
                    plt.bar(curso, quantidade, color='pink')
                    plt.xlabel("Cursos")
                    plt.ylabel("Número de Participantes")
                    plt.title("Participantes por Curso")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

    elif op == 0:
        print("Encerrando o programa. Até mais!")
    else:
        print("Opção inválida. Tente novamente.")
