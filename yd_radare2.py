import r2pipe
from ios_static_ipa_inspector.yd_thing import Thing, Thing2
from ios_static_ipa_inspector.yd_console import YDConsole

def CheckBinary():
    r2 = r2pipe.open("/bin/ls")
    check_list = ['stripped', 'bits', 'canary']

    for x in check_list:
        a = "iIj~{%s}" % (x)
        b = Thing(x, r2.cmd(a))
        YDConsole.single_value(b)

    r2.quit()