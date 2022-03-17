alphabet = 'АКДЕМИ'
# alphabet = 'АКАДЕМИК'  <--- здесь буквы повторяются и поэтому дают одинаковые подходящие варианты
vowels = 'АЕИ'
consonants = 'КДМ'

vowels_comb = []
for v1 in vowels:
    for v2 in vowels:
        vowels_comb.append(v1 + v2)

consonants_comb = []
for v1 in consonants:
    for v2 in consonants:
        consonants_comb.append(v1 + v2)

count = 0
for ch1 in alphabet:
    print(ch1)
    for ch2 in alphabet:
        for ch3 in alphabet:
            for ch4 in alphabet:
                for ch5 in alphabet:
                    for ch6 in alphabet:
                        for ch7 in alphabet:
                            for ch8 in alphabet:
                                res = ch1 + ch2 + ch3 + ch4 + ch5 + ch6 + ch7 + ch8
                                if res.count('А') == 2 and res.count('К') == 2 and res.count('Д') == 1 and res.count(
                                        'М') == 1 and res.count('Е') == 1 and res.count('И') == 1:
                                    is_broken = False
                                    for v in vowels_comb:
                                        if v in res:
                                            is_broken = True
                                            break
                                    for c in consonants_comb:
                                        if c in res:
                                            is_broken = True
                                            break
                                    if is_broken:
                                        break
                                    print(res)
                                    count += 1
print(count)
