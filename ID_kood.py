from OmaMoodul import *
ikood=""
while True:
    ikood=input("Sisesta isikukood: ")
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        s=sugukontroll(ikood)
        if s=="viga":
            print("Esineme täht ei ole õige")
        else:
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                lause(ikood)
                