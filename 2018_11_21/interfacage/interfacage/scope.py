from scpi import SCPI

class Horizontal(object):
    def __init__(self, parent):
        self._parent = parent

    @property
    def offset(self):
        return self._parent._get_horizontal_offset()

    @offset.setter
    def offset(self, val):
        return selt._parent._set_horizontal_offset(val)

    # Ou en plus compact !
    # offset = property(lambda self:self._parent._get_horizontal_offset, 
    #                    lambda self, val:self._set_horizontal_offset(val) )

class Channel(object):
    def __init__(self, parent, index):
        self._parent = parent
        self._index = index

    @property
    def scale(self):
        return self._parent._get_channel_scale(self._index)

class Scope(SCPI):
    @property
    def trigger(self):
        return Trigger(self)

    @property
    def channel1(self):
        return Channel(self, i)


class Keysight(Scope):
    def _get_channel_scale(self, channel):
        pass

    def _set_data_source(self, channel):
        self.write(':WAVeform:SOURce CHANnel{}'.format(channel))

    def _get_preamble(self):
        # Format, Type, Points, Count, XIncrement, XOrigin, XReference, YIncrement, YOrigin, YReference
        out = self.ask(':WAV:PRE?')
        return list(map(eval, out.strip().split(',')))

    def ask_array(self, cmd):
        self.write(cmd)
        first = self._inst.read(1)
        header_size = eval(self._inst.read(1))
        size_str = self._inst.read(header_size)
        while size_str[0]==b'0': # remove leading 0
            size_str = size_str[1:]
        size = int(size_str)
        output = self._inst.read(size)
        self._inst.read(1) # \n
        return output

    def _get_channel_waveform(self, channel=1, **kwd):
        self._set_data_source(channel)
        self.write(':WAV:FORMAT BYTE')
        (Format, Type, Points, Count, 
            XIncrement, XOrigin, XReference, 
            YIncrement, YOrigin, YReference) = self._get_preamble()

        buff = self.ask_array(':WAV:DATA?')
        res = np.array(np.frombuffer(buff, dtype = np.dtype('uint8')), dtype=int)
        data = (res - YReference)*YIncrement
        t0 = XOrigin
        dt = XIncrement
        return data, t0, dt


