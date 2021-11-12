# hakerski na4in za suzdavane na klasove s type, optional e

Baba = type('Baba', (), {'say_hi': lambda self: 'Hi From Baba'})

baba = Baba()
print(baba.say_hi()) # Hi From Baba

Dqdo = type('Dqdo', (Baba,), {'say_hi_from_dqdo': lambda self: 'Hi From Dqdo'})

dqdo = Dqdo()
print(dqdo.say_hi()) # Hi From Baba
print(dqdo.say_hi_from_dqdo()) # Hi From Dqdo


# rqdko se polzva, prosto primer