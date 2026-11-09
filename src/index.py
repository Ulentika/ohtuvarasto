
from varasto import Varasto


class Main:
    def tulosta_varastot(self, mehua, olutta):
        print("Luonnin jälkeen:")
        print(f"Mehuvarasto: {mehua}")
        print(f"Olutvarasto: {olutta}")

        print("Olut getterit:")
        print(f"saldo = {olutta.saldo}")
        print(f"tilavuus = {olutta.tilavuus}")
        print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    def testaa_mehua(self, mehua):
        print("Mehu setterit:")
        print("Lisätään 50.7")
        mehua.lisaa_varastoon(50.7)
        print(f"Mehuvarasto: {mehua}")
        print("Otetaan 3.14")
        mehua.ota_varastosta(3.14)
        print(f"Mehuvarasto: {mehua}")

    def testaa_virhetilanteet(self):
        print("Virhetilanteita:")
        print("Varasto(-100.0);")
        huono = Varasto(-100.0)
        print(huono)

        print("Varasto(100.0, -50.7)")
        huono = Varasto(100.0, -50.7)
        print(huono)

    def testaa_lisaaminen(self, mehua, olutta):
        print(f"Olutvarasto: {olutta}")
        print("olutta.lisaa_varastoon(1000.0)")
        olutta.lisaa_varastoon(1000.0)
        print(f"Olutvarasto: {olutta}")

        print(f"Mehuvarasto: {mehua}")
        print("mehua.lisaa_varastoon(-666.0)")
        mehua.lisaa_varastoon(-666.0)
        print(f"Mehuvarasto: {mehua}")

    def testaa_ottaminen(self, mehua, olutta):
        print(f"Olutvarasto: {olutta}")
        print("olutta.ota_varastosta(1000.0)")
        saatiin = olutta.ota_varastosta(1000.0)
        print(f"saatiin {saatiin}")
        print(f"Olutvarasto: {olutta}")

        print(f"Mehuvarasto: {mehua}")
        print("mehua.otaVarastosta(-32.9)")
        saatiin = mehua.ota_varastosta(-32.9)
        print(f"saatiin {saatiin}")
        print(f"Mehuvarasto: {mehua}")

    def main(self):
        mehua = Varasto(100.0)
        olutta = Varasto(100.0, 20.2)

        self.tulosta_varastot(mehua, olutta)
        self.testaa_mehua(mehua)
        self.testaa_virhetilanteet()
        self.testaa_lisaaminen(mehua, olutta)
        self.testaa_ottaminen(mehua, olutta)


if __name__ == "__main__":
    Main().main()
