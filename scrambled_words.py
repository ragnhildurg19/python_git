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
#Fáum inn skrá frá notanda.
input_file = str(input("Enter name of file: "))
open_file = open(input_file, "r")

#Þessi breyta á að gera eitthvað voðalega sniðugt.. en gerir það bara ekki. 
#hún á að halda fyrsta og seinasta staf hvers orðs og ætti að geta eitthvað við middle_words.
def scramble(word):
    middle_words = word[1:-1]
    
    return word[0] + middle_words + word[-1]
#fyrir hverja línu í skjalinu á forritið að rugla orðum. 
for word in open_file:
        words = word.split()
        for word in words:
            scrambled_word=scramble(word)
        print(scrambled_word, end=" ")

open_file.close()
