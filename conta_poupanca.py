from conta import Conta

# HERANÇA: ContaPoupanca herda de Conta
class ContaPoupanca(Conta):
    def __init__(self, titular: str, numero: int, taxa_rendimento: float):
        super().__init__(titular, numero)
        self.__taxa_rendimento = taxa_rendimento

    # POLIMORFISMO: Sobrescrevendo com a regra específica da poupança (sem limite extra)
    def sacar(self, valor: float) -> bool:
        if valor > 0 and self.saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} efetuado na Conta Poupança {self.numero}.")
            return True
        
        print(f"Erro: Saldo insuficiente na Conta Poupança {self.numero}.")
        return False

    # Comportamento exclusivo da poupança
    def aplicar_rendimento(self):
        rendimento = self.saldo * self.__taxa_rendimento
        self.depositar(rendimento) # Reutiliza o método da superclasse
        print(f"Rendimento de R$ {rendimento:.2f} aplicado à conta {self.numero}.")