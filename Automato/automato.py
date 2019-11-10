class Automato:
    def __init__(self):
        self.transitions = {}	# 'transitions' é um dicionário que um nome (Estado) e uma função (Transição)
        self.startState = None	# Estado incial
        self.endStates = []	    # Estados finais

    def add_state(self, nome, transition, end_state=0):
        nome = nome.upper()
        self.transitions[nome] = transition
        if end_state:
            self.endStates.append(nome)

    def set_start(self, nome):
        self.startState = nome.upper()

    def run(self, input):

        print("==========================================")
        print("Iniciando automato...")
        print("Entrada: {}\n".format(input))
        transition = self.transitions[self.startState]

        while True:
            (proximo_estado, input) = transition(input) # 'proximo_estado' é um Estado, 'input' é a string de entrada

            if ((proximo_estado.upper() in self.endStates and len(input) == 0) or (proximo_estado.upper() == "EST_ERRO")):
                print("Alcançou ", proximo_estado)
                print("==========================================")
                break
            else:
                transition = self.transitions[proximo_estado.upper()]
