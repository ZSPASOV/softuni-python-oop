def vowels(s):
    for c in s:
        if c.lower() in 'aeiuyo':
            yield c


my_string = vowels('Iteratori')
for char in my_string:
    print(char)

# v judge dava samo 50 % shtoto tam se o4akva da ne polzvame generator, no tova si e vqrno reshenie
