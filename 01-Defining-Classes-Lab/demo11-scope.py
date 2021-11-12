# polzva se rqdko, no vse paK:
def outer():
    dqdo = None

    def get_dqdo():
        return dqdo

    def inner():
        nonlocal dqdo
        dqdo= 42 # ako ne slojim nonlocal shte vurne None. nonlocal e scopa na predishnata funkciq, edno nivo nagore
        return get_dqdo()


    return inner


fn_inner = outer()
fn_get_dqdo = fn_inner()
print(fn_get_dqdo) # 42
print(fn_inner()) # 42