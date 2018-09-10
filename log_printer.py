
def snappy_console_banner(arg1: str):
    print('\n[+]' + ('*' * 10) + ' ' + arg1 + ' ' + ('*' * 10) + '[+]')

# def snappy_console_print_unzipper(thing: Unzipper):
#     print('[+]\t{0}\t{1}'.format(thing.filename, thing.user_entered_path))

def snappy_console_arg_1(arg1: str):
    print('[+]\t', arg1)

def snappy_console_arg_2(arg1: str, arg2: str):
    print('[+]\t{0}\t{1}'.format(arg1, arg2))