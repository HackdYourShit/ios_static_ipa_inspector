import r2pipe
from ios_static_ipa_inspector.thing_class import Thing, Thing2
from ios_static_ipa_inspector.log_printer import snappy_console_arg_1

def CheckBinary():
    r2 = r2pipe.open("/bin/ls")
    check_list = ['stripped', 'bits', 'canary']

    for x in check_list:
        a = "iIj~{%s}" % (x)
        b = Thing(x, r2.cmd(a))
        snappy_console_arg_1(b)

    r2.quit()
    c = Thing2("warcraft","world","hello")
    snappy_console_arg_1(c)
