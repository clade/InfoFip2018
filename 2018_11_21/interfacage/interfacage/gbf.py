from scpi import SCPI

class Agilent33200(SCPI):
    def _get_frequency(self):
        pass

    def _set_frequency(self, value):
        pass

    frequency = property(_get_frequency, _set_frequency)

