from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, titular: str, numero: int):
        # ENCAPSULAMENTO:
        # __ (duplo underline) indica "privado"
        # _ (underline simples) indica "protegido" (subclasses podem acessar)
        self.__titular = titular
        self.__numero = numero
        self._saldo = 0.0

    # Getters usando o decorador @property (forma "pythônica" de acessar dados protegidos)
    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def saldo(self) -> float:
        return self._saldo

    # Método comum a todas as contas
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {self.__numero}.")
        else:
            print("Erro: Valor de depósito inválido.")

    # POLIMORFISMO: Método abstrato que força as subclasses a implementarem sua própria lógica
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    def exibir_detalhes(self):
        print(f"Conta: {self.__numero} | Titular: {self.__titular} | Saldo Atual: R$ {self._saldo:.2f}")