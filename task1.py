a = int(input("Enter your name :"))
a = a.lower()
vowel = []
consunant = []
for i in a:
    if i in ["a","e","i","o","u"] :
        vowel.append(i)
    else :
        consunant.append(i)
print(vowel)
print(consunant)