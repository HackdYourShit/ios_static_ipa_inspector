import r2pipe
from ios_static_ipa_inspector.thing_class import Thing

def CheckBinary():
    t = Thing()
    r2 = r2pipe.open("/bin/ls")
    t.key_name = "stripped check"
    print("stripped: " + r2.cmd("iIj~{stripped}"))  # evaluates JSONs and returns an object
    r2.quit()

    # add finding to a global List.