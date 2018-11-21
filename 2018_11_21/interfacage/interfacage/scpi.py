import visa

class SCPI(object):
    def __init__(self, conn):
        if isinstance(conn, str):
            conn = visa.ResourceManager().open_resource(conn)
        self._conn = conn

    def ask(self, *args):
        return self._conn.ask(*args)

    def write(self, *args):
        return self._conn.write(*args)

    def read(self, *args):
        return self._conn.read(*args)

    def scpi_ask(self, cmd):
        cmd = cmd if cmd.endswith('?') else cmd + '?'
        return self.ask(cmd)

    def scpi_write(self, cmd, *args):
        pass

    def scpi_ask_for_float(self, cmd):
        """ Lit le résultat de l'instruction cmd et la transforme en float """
        pass 

    @property
    def idn(self):
        return self.scpi_ask('*IDN')

    def reset(self):
        pass

    def __repr__(self):
        return "{self.__class__.__name__}({self.idn})".format(self=self)

