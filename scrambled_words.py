# DESCRIPTION
# Skrifið Python forrit sem byggir á verkefninu Scrambled Words á bls. 340 í kennslubókinni.
# Skilið forritsskrá með nafninu scrambled_words.py.
# Inntakið í forritið er nafn á skrá sem inniheldur eitt orð (hugsanlega með greinarmerki í enda orðsins) 
# í hverri línu. Úttakið (á skjá) er runa af brengluðum orðum (eitt bil á milli orða) 
# með einu "newline" að lokum.
# Notið eftirfarandi reglur til að brengla orð:
# Fyrsta og síðasta staf sérhvers orðs á ekki að brengla. 
# Ef greinarmerki er í enda orðs (t.d. problem.), þá skal ekki eiga við greinarmerkið 
# og það telur jafnframt ekki sem síðasti óbrenglaði stafurinn 
# (í rununni problem. er m þá síðasti stafurinn sem ekki á að brengla). 
# Þegar athugað er hvort safur sé greinarmerki þá ber að nota string.punctuation 
# (sjá bls. 253 í kennslubókinni).
# Annars á að brengla stafina á milli fyrsta og síðasta stafs sérhvers orðs 
# með því að skipta (víxla) á aðliggjandi stöfum (byrja vinstra megin).
# Í lausninni ykkar eigið það aðeins að nota efni úr köflum 0-6 í kennslubókinni.  
# Þetta þýðir, t.d., að ekki má nota lista.
# Það þarf varla að taka það fram að læsileiki forritsins er mjög mikilvægur.

import string

input_file = str(input("Enter name of file: "))
open_file = open(input_file, "r")

def scramble(word):
    middle_words = word[1:-1]
    
    return word[0] + middle_words + word[-1]

for line in open_file:
        words = line.split()
        for word in words:
            scrambled_word=scramble(word)
            middle_words = word[1:-1]
print(middle_words) #Er með þetta inni til að sjá hvort miðjustafirnir ruglist. SEM ÞEIR GERA EKKI. 
print(scrambled_word, end="")

open_file.close()