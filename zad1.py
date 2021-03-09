x0 = 2500
alfa = 0.1

def odredi_novu_vrijednost_gradijenta(x):
    gradijent = - 2400 + 4*x
    return gradijent


def odredi_novi_x(x_stari, alfa):
    gradijent = odredi_novu_vrijednost_gradijenta(x_stari)
    x_novi = x_stari - alfa * gradijent
    return(x_novi)


##inicijalne vrijednosti
x1 = 0
x2 = x0
x_ref = 50  #koristi se za provjeru je li se broj značajnije promijenio u zanjih 50 iteracija
i = 0       #broj iteracija 0 - 49 s resetom na 49 - za provjeru je li se broj značajnije promijenio u zanjih 50 iteracija
j = 0       #broj iteracija
flag = 1    #1 - default i ako se u zadnjih 50 iteracija broj nije značajnije promijenio


##iteracije
while(flag):
    x1 = odredi_novi_x(x2,alfa)
    print(str(i)+"   "+ str(j) +"     "+str(x1) +"   "+ str(x2) +"            "+str(x_ref))
    x2 = x1
    i = i + 1
    j = j + 1
    if(i==50):
        if(abs(x_ref-x1) < 0.001):
            flag = 0
        x_ref = x1
        i = 0


y = -2 * x1 + 2400
A = x1 * y
print("Maksimalna površina je "+ str(A))