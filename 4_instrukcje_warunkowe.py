x = 5
if x == 5:
    print("x jest równe 5")
    x = str(x)
    print("Wyświetlam wartość x: " + x)
else:
    print("x nie jest równe 5")
    x = str(x)
    print("Wyświetlam wartość x: " + x)

##########

y = True

if y:
    print("Prawda")
else:
    print("Fałsz")

#########

z = 5>6

if z:
    print("Prawda")
else:
    print("Fałsz")

#######

j = "1"

if bool(j):
    print("Prawda, j ma typ bool")
else:
    print("J nie ma typu bool")
