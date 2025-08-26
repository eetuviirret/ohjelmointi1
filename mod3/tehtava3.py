sukupuoli = input("Syötä biologinen sukupuoli: ")
hemoglobiiniarvo = input("Syötä hemoglobiiniarvo: ")
int_hemoglobiiniarvo = int(hemoglobiiniarvo)

if sukupuoli == "nainen":
    if 117<=int_hemoglobiiniarvo<175:
        print("Normaali hemoglobiiniarvo")
    elif int_hemoglobiiniarvo < 117:
        print ("Alhainen hemoglobiiniarvo")
    else:
        print ("Korkea hemoglobiiniarvo")


if sukupuoli == "mies":
    if 134<=int_hemoglobiiniarvo<195:
        print("Normaali hemoglobiiniarvo")
    elif int_hemoglobiiniarvo < 134:
        print("Alhainen hemoglobiiniarvo")
    else:
        print("Korkea hemoglobiiniarvo")

