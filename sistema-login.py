def registrar():
    bd = ("credenciais.txt", "r")
    nome = input('Digite o seu nome: ')
    senha = input('Digite a sua senha: ')
    conf_senha = input('Digite sua senha novamente: ')
    nome_mae = input('[Pergunta de segurança] Digite o nome da sua mãe: ')
    if senha != conf_senha:
        print("Senha não confere, tente novamente")
        registrar()
    else:
        if len(senha)<=6:
            print('senha muito curta, tente novamente')
            registrar()
        elif nome in db:
            print('Nome já cadastrado! ')
            registrar()
        elif nome_mae != nome_mae:
            print('Pergunta de seguraça errada!')
            registrar()
        else:
            bd = open ("credenciais.txt", "a")

def logar():
    pass
