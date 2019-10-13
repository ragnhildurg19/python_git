# Lýsing á verkefni: 
#     Í þessu verkefni eigið þið að skrifa Python forrit, airline_seating.py, sem gefur notanda möguleika á að bóka sæti í flugvél.  
#     Þið megið nota efni úr fyrstu 8 köflunum í kennslubókinni við lausn á verkefninu.
#     Í upphafi er fjöldi raða og fjöldi sæta í hverri röð í flugvélinni sleginn inn af notanda
#     Númer raðar er birt í svæði sem er 2 stafir að breidd, síðan koma þrjú bil.  
#     Eitt bil er á milli sæta en gangur á milli sætanna er sýndur með þremur bilum.  
#     Gera má ráð fyrir að fjöldi sæta í hverri röð sé slétt tala >= 2 og það á alltaf að vera einungis einn gangur á milli sætanna.
#     Eftir þetta er notandanum gefinn kostur á að taka sæti frá.  Hann gefur það til kynna með því að slá inn númer raðar og sæti (með bili á milli), t.d.:
#         Input seat number (row seat): 7 B
#     og þá prentast yfirlitið aftur, nú með 'X' fyrir valið sæti:
# 1 Taka inn input frá notanda, rows og seats
# 2 prenta raðir og sæti með 2ja stafa breidd fyrir númer raða og 3 bil eftir það, 3 bil er gangurinn,
# og eitt bil á milli sæta
# Einn gangur,fjöldi sæta í röð er slétt tala >=2
# 3 fá input frá notanda með sætinr, Taka frá sæti, if input er ákveðið þá setjum við X í staðinn. 
# 4

# SEATS = [A,B,C,D,E,F,G,H,I,J]
import math
def get_number_of_rows():
    ''' returns a number of rows '''
    rows = int(input("Enter number of rows: "))

    return rows

def get_number_of_seats():
    ''' returns a number of seats '''
    seats = int(input("Enter number of seats in each row: "))

    return seats

def data_list(rows, seats):
    ''' Returns a list of rows and seats '''
    seat_list = ["A", "B", "c", "D", "E", "F", "G", "H", "I", "J"]
    seat_list = seat_list[:seats]
    airplane = [ seat_list for i in range(rows) ]
    
    return airplane

def BookSeat(book_seat):
    book_seat = book_seat.split(" ")
    pass


def main():
    rows = get_number_of_rows()
    seats = get_number_of_seats()
    plane = data_list(rows, seats)
    # á eftir að skipta röðinni í tvennt og setja línufjölda fyrir framan
    print(*plane, sep= "\n") 
    book_seat = input("Input seat number (row seat): ")



    while True:
        more_seats = input("More seats (y/n)? ")

        if more_seats == "y":
            input("Input seat number (row seat): ")
                # ef sæti er tekið
            print("That seat is taken!")
                # ef sæti er ekki til
            print("Seat number is invalid!")

        else:
            break

main()
