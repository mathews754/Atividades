from automato import Automato

soma = "+"
subtracao = "-"
multiplicacao = "*"
divisao = "/"

def aceita_id(palavra):
    splitted_txt = palavra.split(None,1)
    input, palavra = splitted_txt if len(splitted_txt) > 1 else (palavra,"")
    if len(input)>1: input, palavra = input[0],input[1:]+palavra
    if input.isalpha() or input.isdigit():
        print("<identificador, {}>".format(input))
        proximo_estado = "Est2"
    else:
        proximo_estado = "Est_erro"
    return (proximo_estado, palavra)

def aceita_op(palavra):
    splitted_txt = palavra.split(None,1)
    input, palavra = splitted_txt if len(splitted_txt) > 1 else (palavra,"")
    if len(input)>1: input, palavra = input[0],input[1:]+palavra
    if (input == soma):
        print("<soma, {}>".format(input))
        proximo_estado = "Est1"
    elif (input == subtracao):
        print("<subtracao, {}>".format(input))
        proximo_estado = "Est1"
    elif (input == multiplicacao):
        print("<multiplicacao, {}>".format(input))
        proximo_estado = "Est1"
    elif (input == divisao):
        print("<divisao, {}>".format(input))
        proximo_estado = "Est1"
    elif len(input) == 0:
        proximo_estado = "err"
    else:
        proximo_estado = "Est_erro"
    return (proximo_estado, palavra)

if __name__== "__main__":
    m = Automato()
    m.add_state("Est1", aceita_id)
    m.add_state("Est2", aceita_op, end_state=1)
    m.add_state("Est_erro", None, end_state=1)
    m.add_state("err", None, end_state=1)
    m.set_start("Est1")

    inpt = input("Insira a expressão a ser analizada: ")
    m.run(inpt)
