
class Instrument:
    def play(self):
        pass

class StringInstrument(Instrument):
    def play(self):
        print("Струнний інструмент грає")

class WindInstrument(Instrument):
    def play(self):
        print("Духовий інструмент грає")

class PercussionInstrument(Instrument):
    def play(self):
        print("Ударний інструмент грає")

class Guitar(StringInstrument):
    def __init__(self, brand, strings):
        self.brand = brand
        self.strings = strings

    def play(self):
        print(f"Гітара {self.brand} грає")

    def tune(self):
        print("Гітару налаштовано")

class Flute(WindInstrument):
    def play(self):
        print("Флейта грає")

class Drum(PercussionInstrument):
    def play(self):
        print("Барабан грає")

class HybridInstrument(StringInstrument, WindInstrument, PercussionInstrument):
    def play(self):
        print("Гібридний інструмент поєднує звуки:")
        StringInstrument.play(self)
        WindInstrument.play(self)
        PercussionInstrument.play(self)


guitar = Guitar("Yamaha", 6)
flute = Flute()
drum = Drum()
guitar.play()
guitar.tune()
flute.play()
drum.play()
print("===================")
hybrid = HybridInstrument()
hybrid.play()
