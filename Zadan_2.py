i=0
v_r=0
n_r=0
kol_gl=0
gl="ЁУЕЫАОЭЯИЮёуеыаоэяию"
s=input("Введите слово: ")
while i< len(s)-1:
    if s[i].isupper() and s[i+1].isupper():
        v_r+=1
    elif s[i].islower() and s[i+1].islower():
        n_r+=1
    kol_gl+=gl.count(s[i])
    i+=1
print("Количество пар верхнего регистра в слове: ", v_r)
print("Количество пар нижнего регистра в слове: ", n_r)
print("Количество гласных в слове", kol_gl)