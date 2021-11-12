# da googlena , tova sa funkcionalni patterns

# primer

def adder():
    n = 0

    def incrementer(): # closure funkciq (definirana v obhvata na druga funkciq)
        nonlocal n
        n += 1

    def getter(): # # closure funkciq (definirana v obhvata na druga funkciq)
        return n

    return incrementer, getter # higher order funkcii

fn_inc_1, fn_get_1 = adder()
fn_inc_2, fn_get_2 = adder()
fn_inc_3, fn_get_3 = adder()

fn_inc_1()
fn_inc_1()
fn_inc_1()
print(fn_get_1()) # 3
print(fn_get_2()) # 0
print(fn_get_3()) # 0

# tozi primer e podobno na obekt ama bez da se polzvat klasove