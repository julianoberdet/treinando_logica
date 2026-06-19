exp = str(input('Digite sua expressão: '))
pilha = []

for simb in exp:

    #SE o usuario começa digitado '(' len(pilha) = 1
    if simb == '(':
        pilha.append('(')

    #Se o usuario começar digitando ')' Não vai apagar com pop, vai só dar append ')'
    #por que len(pilha) não é maior que 0
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

#Se o usuario digitar '(' , vai dar append '(' ,
# ou seja usuario digitou '(' -> len(pilha) = 1 -> if len(pilha) > 0 -> pilha.pop() -> len(pilha) = 0 TRUE
# Se o usuario digitar ')' Não vai dar pilha.pop() por que "if len(pilha) não é maior que 0",
# por que nao tem nada na lista ainda, dai o else da append(')') len(pilha) = 1 -> FALSE

if len(pilha) == 0:
    print('Sua expressão está CORRETA')
else:
    print('Sua expressão está ERRADA')

