from funcoes import*
limparTela()
inicio()
dev()
try:
    mostraHistorico = open('historico.txt', 'r')
except FileNotFoundError:
    print(f'\n{azul}Histórico ainda não criado!!!{reset}')
        
reinicio = 'python forca.py'

while True:
    try:
        print(f'{vermelho}\nHistorico: {reset}')
        print(mostraHistorico.read())
    except:
        print(f'{verde}Jogue pela primeira vez para gerar o histórico!!!{reset}')    
    desafiante = input('Desafiante: ').upper()
    if len(desafiante) < 2:
        print(f'{vermelho}Nome Inválido!!!{reset}')
    else:
        break
while True:
    competidor = input('Competidor: ').upper()
    if len(competidor) < 2:
        print(f'{vermelho}Nome Inválido!!!{reset}')
    else:
        break

limparTela()

#INFORMANDO A PALAVRA#
while True:
    palavra = input('Informe a palavra chave: ').upper()
    if len(palavra) < 1:
        print(f'{vermelho}Palavra muito curta!!!{reset}')
    else:
        break

#INFORMANDO AS DICAS
while True:
    dica1 = input('Dica 1: ').upper()
    dica2 = input('Dica 2: ').upper()
    dica3 = input('Dica 3: ').upper()
    if len(dica1 and dica2 and dica3) < 1:
        print(f'{vermelho}Por favor insira as dicas!{reset}')
    else:
        break

os.system('pause')
limparTela()

#DESENHO DO BONECO
vazio = '''
'''
forca = '''
+----+
     |
     |'''

cabeça = '''
     O'''
tronco = '''
     O
     |'''
braço_direito = '''
     O
     |/'''
braço_esquerdo = '''
     O
    \|/'''
perna_esquerda = '''
     O
    \|/
    /  '''
perna_direita = '''
     O
    \|/
    / \ '''


boneco = [vazio,cabeça, tronco, braço_direito,braço_esquerdo, perna_esquerda, perna_direita]
acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''


while acertos != len(palavra) and erros != 6:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra} '
        else:
            mensagem += '_ '
    print(forca+boneco[erros])
    print(mensagem)

    escolha = input('\n(1)Tentar uma letra... \n(2)Solicitar uma dica... \nOpção: ')
    if escolha == '1':
        try:
            letra = input('Digite uma letra: ').upper()
        except KeyError:
            print(f'{vermelho}Caracter inválido!!!{reset}')

        limparTela()
        if letra in letras_acertadas+letras_erradas:
            print('Você ja tentou está letra!!!')
            os.system("pause")
            limparTela()
        elif letra in palavra:
            letras_acertadas += letra
            acertos += palavra.count(letra)
            if acertos == len(palavra):
                ganhou()
                print(f'{verde}A palavra era {vermelho}{palavra}{reset}')
                open('historico.txt', 'a').write(f'Vencedor: {competidor} | Perdedor: {desafiante} - Palavra secreta: {palavra} - Dica 1: {dica1} - Dica 2:  {dica2} - Dica 3: {dica3}\n')
        else:
            letras_erradas += letra
            erros += 1
            limparTela()
            if erros == 6:
                perdeu()
                print(f'{verde}A palavra era {vermelho}{palavra}{reset}')
                open('historico.txt', 'a').write(f'Vencedor: {desafiante} | Perdedor: {competidor} - Palavra secreta: {palavra} - Dica 1: {dica1} - Dica 2:  {dica2} - Dica 3: {dica3}\n')
                os.system("pause")
                limparTela()

    elif escolha == '2':
        dicas = input(f'{magenta}\nDICAS:{reset}\nDigite (1) para a primeira dica. \nDigite (2) para a segunda dica. \nDigite (3) para a terceira dica. \nOpção: ')
        if dicas == '1':
            print(f'{verde}Dica 1:{reset}', dica1)  
        elif dicas == '2':
            print(f'{verde}Dica 2:{reset}',dica2)
        elif dicas == '3':
            print(f'{verde}Dica 3:{reset}',dica3)
        else:
            print(f'{vermelho}Opção Inválida!!!{reset}')
        os.system('pause')
        limparTela()
    else:
        print(f'{vermelho}Opção Inválida!!!{reset}')
        os.system('pause')
        limparTela()   

def escolher():
    opçao = input('\nEscolha uma das opções: \n(1)Jogar Novamente: \n(2)Sair \nOpção: ')
    if opçao == '1':
        os.system(reinicio)
    elif opçao == '2':
        limparTela()
        quit()
    else:
        print(f'{vermelho}Opção Inválida!!!{reset}')
        os.system('pause')
        escolher()
escolher()