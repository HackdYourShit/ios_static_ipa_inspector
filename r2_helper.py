import r2pipe
from ios_static_ipa_inspector.thing_class import Thing

def CheckBinary():
    r2 = r2pipe.open("/bin/ls")
    check_list = ['stripped', 'bits', 'canary']

    for x in check_list:
        b = Thing(x, r2.cmd('iI~{}'.format(x)))

    r2.quit()

    # add finding to a global List.