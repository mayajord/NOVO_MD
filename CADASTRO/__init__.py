def verificar_senha(senha1, senha2):
    while senha1 != senha2:
        print('Digite senhas iguais.')
        senha1 = input('Digite sua senha novamente: ')
        senha2 = input('Digite a mesma senha novamente para confirmar: ')
    return True


def email_verdade(email):
    while True:
        if not '@' or '.com' in email:
            return True
        print('Digite um email válido.')
        email = input('Digite seu email novamente: ')


def nome_verdade(nome):
    while True:
        if len(nome) >= 2:
            return True
        print('Digite um nome válido.')
        nome = input('Digite seu nome novamente: ')


def verificar_user_existente(email,usuarios):
    for user in usuarios:
        if user[1] == email:
            print('Esse email já foi cadastrado.')
            return True
    return False


def cadastro_usuario(usuarios, indesejados):
    while True:
        print('---------VAMOS COMEÇAR---------')
        nome = input('Digite seu nome:')
        nome_verdade(nome)
        while True:
            email = input('Digite seu email:')
            email_verdade(email)
            if not verificar_user_existente(email, usuarios):
                break
        if usu_indesejado(email, indesejados):
            print('VOCÊ NÃO É BEM VINDO!!!')
            break
        analfa = input('Voce tem dificuldades com leitura ou escrita? Sim ou Nao: ')
        crime = input('Voce tem histórico penal?Sim ou Nao')
        if analfa == 'Sim' or crime == 'Sim':
            print('Infelizmente voce nao poderá participar de nenhum evento!')
            indesejados[email] = {'nome':nome}
            print(indesejados)
            return False
        senha1 = input('Digite sua senha:')
        senha2 = input('Digite sua senha novamente')
        verificar_senha(senha1, senha2)
        usuarios.append([nome, email, senha2])
        return True

def fazer_login(email, senha2, usuarios):
    for user in usuarios:
        if user[1] == email and user[2] == senha2:
            print('<<VOCE ESTA LOGADO>>!')
            return True
    print('###USUARIO OU SENHA INCORRETOS###.')
    return False

def usu_indesejado(email, indesejados):
    if email in indesejados.keys():
        return True