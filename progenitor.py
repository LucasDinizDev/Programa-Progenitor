from pyswip import Prolog

class Genealogia:
    def __init__(self):
        self.prolog = Prolog()
        self._assert_fatos()

    def _assert_fatos(self):
        fatos = [
            "progenitor(sara,isaque)",
            "progenitor(abraao,isaque)",
            "progenitor(abraao,ismael)",
            "progenitor(isaque,esau)",
            "progenitor(isaque,jaco)",
            "progenitor(jaco,jose)",
            "mulher(sara)",
            "homem(abraao)",
            "homem(isaque)",
            "homem(ismael)",
            "homem(esau)",
            "homem(jaco)",
            "homem(jose)"
        ]
        for fato in fatos:
            self.prolog.assertz(fato)

    def consulta_pai(self, filho):
        consulta = f"progenitor(X, {filho}), homem(X)"
        return self._consultar(consulta)

    def consulta_mae(self, filho):
        consulta = f"progenitor(X, {filho}), mulher(X)"
        return self._consultar(consulta)

    def consulta_irmao(self, pessoa):
        consulta = f"progenitor(Z, {pessoa}), progenitor(Z, Y), homem(Y), Y \\= {pessoa}"
        return self._consultar(consulta)

    def consulta_tio_tia(self, sobrinho):
        consulta = f"progenitor(X, Y), progenitor(Y, {sobrinho}), homem(X), X \\= Y"
        return self._consultar(consulta)

    def adicionar_progenitor_filho_sexo(self):
        novo_progenitor = input("Digite o nome do novo progenitor: ")
        novo_filho = input(f"Digite o nome do filho de {novo_progenitor}: ")
        novo_sexo = input(f"Digite o sexo de {novo_progenitor} (homem/mulher): ")

        self.prolog.assertz(f"progenitor({novo_progenitor},{novo_filho})")
        self.prolog.assertz(f"{novo_sexo}({novo_progenitor})")

        print(f"Progenitor {novo_progenitor} e filho {novo_filho} adicionados com sucesso!")

    def _consultar(self, consulta):
        return list(self.prolog.query(consulta))

    def main(self):
        while True:
            print("Escolha uma opção:")
            print("1. Consultar pai de uma pessoa")
            print("2. Consultar mãe de uma pessoa")
            print("3. Consultar irmãos de uma pessoa")
            print("4. Consultar tios/tias de uma pessoa")
            print("5. Adicionar novo progenitor, filho e sexo")
            print("6. Sair")

            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                pessoa = input("Digite o nome da pessoa: ")
                resultado = self.consulta_pai(pessoa)
                print(f"Pai de {pessoa}: {resultado}")
            elif escolha == "2":
                pessoa = input("Digite o nome da pessoa: ")
                resultado = self.consulta_mae(pessoa)
                print(f"Mãe de {pessoa}: {resultado}")
            elif escolha == "3":
                pessoa = input("Digite o nome da pessoa: ")
                resultado = self.consulta_irmao(pessoa)
                print(f"Irmãos de {pessoa}: {resultado}")
            elif escolha == "4":
                pessoa = input("Digite o nome da pessoa: ")
                resultado = self.consulta_tio_tia(pessoa)
                print(f"Tios/tias de {pessoa}: {resultado}")
            elif escolha == "5":
                self.adicionar_progenitor_filho_sexo()
            elif escolha == "6":
                print("Saindo.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    genealogia = Genealogia()
    genealogia.main()
