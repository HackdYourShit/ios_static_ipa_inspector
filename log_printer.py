from ios_static_ipa_inspector.thing_class import Thing


def snappy_console_banner(arg1: str):
    print('\n[+]' + ('*' * 10) + ' ' + arg1 + ' ' + ('*' * 20))

def snappy_console_print(thing: Thing):
    print('[+]\t{0}\t{1}'.format(thing.key, thing.value))

def snappy_console_arg_1(arg1: str):
    print('[+]\t{0}', arg1)

def snappy_console_arg_2(arg1: str, arg2: str):
    print('[+]\t{0}\t{1}'.format(arg1, arg2))