from conta import Conta

# HERANÇA: ContaCorrente herda de Conta
class ContaCorrente(Conta):
    def __init__(self, titular: str, numero: int, limite_cheque_especial: float):
        # Chama o construtor da classe pai (super)
        super().__init__(titular, numero)
        self.__limite_cheque_especial = limite_cheque_especial

    # POLIMORFISMO: Sobrescrevendo o método abstrato sacar
    def sacar(self, valor: float) -> bool:
        if valor > 0 and (self.saldo + self.__limite_cheque_especial) >= valor:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} efetuado na Conta Corrente {self.numero}.")
            return True
        
        print(f"Erro: Saldo e limite insuficientes na Conta Corrente {self.numero}.")
        return False