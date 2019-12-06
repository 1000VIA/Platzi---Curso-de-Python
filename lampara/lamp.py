class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
              '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    # Primer método que se va a llamar, self indica que un método de instancia
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on  # nace estando apagada

    def turn_on(self):  # Método público para prender la lampara
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):  # Método público para apagar la lampara
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):  # Método privado
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
