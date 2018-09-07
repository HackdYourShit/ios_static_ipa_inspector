
class Thing:

    def __init__(self, key, value):
        from log_printer import snappy_console_print
        self.key = key
        self.value = value
        snappy_console_print(self)