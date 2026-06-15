import os
import getpass
import time
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

class TelaLogin:
    def __init__(self):
        # ENCAPSULAMENTO: Dicionário privado simulando um banco de dados de usuários (login: senha)
        self.__usuarios_cadastrados = {
            "marcos.santos": "senha123",
            "adao.silva": "admin123",
            "admin": "1234"
        }

    def __limpar_tela(self):
        # Limpa o terminal dependendo do sistema operacional (Windows ou Linux/Mac)
        os.system('cls' if os.name == 'nt' else 'clear')

    def __autenticar(self, usuario: str, senha: str) -> bool:
        # Valida se a chave (usuário) existe no dicionário e se a senha corresponde
        if usuario in self.__usuarios_cadastrados and self.__usuarios_cadastrados[usuario] == senha:
            return True
        return False

    def iniciar(self) -> bool:
        self.__limpar_tela()
        print("=====================================")
        print("    ACESSO AO SISTEMA BANCÁRIO       ")
        print("=====================================\n")

        tentativas = 3

        while tentativas > 0:
            usuario = input("👤 Usuário: ")
            # getpass oculta o que o usuário digita no terminal por segurança
            senha = getpass.getpass("🔑 Senha: ") 

            if self.__autenticar(usuario, senha):
                print("\n✅ Login realizado com sucesso!")
                print("Carregando sua conta...")
                time.sleep(1.5) # Pausa dramática para simular carregamento
                self.__limpar_tela()
                return True
            else:
                tentativas -= 1
                print(f"\n❌ Usuário ou senha incorretos. Você tem {tentativas} tentativa(s) restante(s).\n")

        print("🔒 Acesso bloqueado por segurança. Procure sua agência.")
        return False

def main():
    # Instancia a tela de login
    login = TelaLogin()

    # O sistema bancário só roda se o iniciar() retornar True
    if login.iniciar():
        print("=== PAINEL BANCÁRIO ===\n")

        # CRIAÇÃO DE OBJETOS
        cc = ContaCorrente("Marcos Santos", 1001, 500.0)
        cp = ContaPoupanca("Adão Silva", 2001, 0.01)

        # --- Testando a Conta Corrente ---
        print("--- Operações: Conta Corrente ---")
        cc.depositar(1000.0)
        cc.sacar(1200.0) 
        cc.exibir_detalhes()
        print()

        # --- Testando a Conta Poupança ---
        print("--- Operações: Conta Poupança ---")
        cp.depositar(1000.0)
        cp.sacar(1200.0) 
        cp.aplicar_rendimento()
        cp.exibir_detalhes()
        print()

        print("--- Relatório Final ---")
        banco = [cc, cp]
        for conta in banco:
            conta.exibir_detalhes()

if __name__ == "__main__":
    main()
