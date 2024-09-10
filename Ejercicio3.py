class Procesador:
    def OperacionMatematica(self, Multiplicando1, Multiplicando2, Sumando1):
        Resultado = Multiplicando1 * Multiplicando2 + Sumando1
        return Resultado

    def Potencia(self, Base):
        return Base ** 2

    def main(self):
        print("\tMenu         ")
        print("1.Operacion Matematica")
        print("2.Potencia")
        op = int(input("Elije una opcion(1/2) : "))

        procesador = Procesador()

        if op == 1:
            """PRUEBA UNITARIA 1"""
            resultado = procesador.OperacionMatematica(4, 3, 2)
            print(f"4 * 3 + 2 = {resultado}")
        elif op == 2:
            """PRUEBA UNITARIA 2"""
            resultado = procesador.Potencia(5)
            print(f"La potencia de 5 es: {resultado}")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    Procesador().main()