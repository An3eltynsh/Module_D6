from collections import Counter

CENS_WORDS = ['редиска', 'Редиска', 'помидорка', 'Помидорка']
text = """Посмотрите, здесь редиска Помидорка! и так далее, Редиска и помидорка"""

def wordcensor(st:str):
    if st in CENS_WORDS:
        return st[0] + '*' * (len(st) - 1)

def wordcensor_notisalpha(st: str):
    ind =0
    for s in st:
        if not s.isalpha():
            ind = st.index(s)
            break
    word = st[0:ind]
    print(word)
    print(st[ind])
    if word in CENS_WORDS:
       return wordcensor(word)+st[ind]
    else: return st

def censor(value:str):
    val = value.split()
    for i in range(len(val)):
        if not val[i].isalpha(): val[i] = wordcensor_notisalpha(val[i])
        if val[i] in CENS_WORDS:
            val[i] = wordcensor(val[i])
    return ' '.join(val)



print(type(censor(text)))