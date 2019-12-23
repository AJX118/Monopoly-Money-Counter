aj = 2500
aisha = 2500
sarah = 2500
sumi = 2500

bank = 1000000
g = 1
while(g == 1):
    x = int(input("Choose option:\n1 for checking money\n2 for giving money to player\n3 for taking money from player\n4 for passing start\n"))
    if(x == 1):
        print("Ammar has: ", aj, "\nAisha has: ", aisha, "\nSarah has: ", sarah, "\nSumi has: ", sumi, "\nBank has: ", bank, "\n")
    elif (x == 2):
        mc= int(input("Choose option:\n1 for Ammar.\n2 for Aisha.\n3 for Sarah.\n4 for Summi bebiz.\n"))
        if(mc == 1):
            money = int(input("How much money???"))
            bank = bank - money
            aj += money
            print("Ammar now has:", aj, " Bank now has:", bank, "\n")
        elif(mc == 2):
            money = int(input("How much money???"))
            bank = bank - money
            aisha += money
            print("Aisha has:", aisha, "\n")
        elif(mc == 3):
            money = int(input("How much money???"))
            bank = bank - money
            sarah += money
            print("Sarah has:", sarah, "\n")
        elif(mc == 4):
            money = int(input("How much money???"))
            bank = bank - money
            sumi += money
            print("Summayah has:", sumi, "\n")

    elif (x == 3):
        mc= int(input("Who is losing the money:\n1 from Ammar.\n2 from Aisha.\n3 from Sarah.\n4 from Summi bebiz.\n"))
        p= int(input("Who is gaining the money:\n1 for Ammar.\n2 for Aisha.\n3 for Sarah.\n4 for Summi bebiz.\n5 for bank.\n"))
        money = int(input("How much money???"))
        if(mc == 1):
            aj -= money
            if(p == 2):
                aisha += money
                print("Ammar now has: ", aj, "Aisha now has: ", aisha, "\n")
            elif(p == 3):
                sarah += money
                print("Ammar now has: ", aj, "Sarah now has: ", sarah, "\n")
            elif(p == 4):
                sumi += money
                print("Ammar now has: ", aj, "Sumayyah now has: ", sumi, "\n")
            elif(p == 5):
                bank += money
                print("Ammar now has: ", aj, "Bank now has: ", bank, "\n")
        elif(mc == 2):
            aisha -= money
            if(p == 1):
                aj += money
                print("Aisha now has: ", aisha, "Ammar now has: ", aj, "\n")
            elif(p == 3):
                sarah += money
                print("Aisha now has: ", aisha, "Sarah now has: ", sarah, "\n")
            elif(p == 4):
                sumi += money
                print("Aisha now has: ", aisha, "Sumayyah now has: ", sumi, "\n")
            elif(p == 5):
                bank += money
                print("Aisha now has: ", aisha, "Bank now has: ", bank, "\n")
        elif(mc == 3):
            sarah -= money
            if(p == 1):
                aj += money
                print("Sarah now has: ", sarah, "Ammar now has: ", aj, "\n")
            elif(p == 2):
                aisha += money
                print("Sarah now has: ", sarah, "Aisha now has: ", aisha, "\n")
            elif(p == 4):
                sumi += money
                print("Sarah now has: ", sarah, "Sumayyah now has: ", sumi, "\n")
            elif(p == 5):
                bank += money
                print("Sarah now has: ", sarah, "Bank now has: ", bank, "\n")
        elif(mc == 4):
            sumi -= money
            if(p == 1):
                aj += money
                print("Sumi now has: ", sumi, "Ammar now has: ", aj, "\n")
            if(p == 2):
                aisha += money
                print("Sumi now has: ", sumi, "Aisha now has: ", aisha, "\n")
            if(p == 3):
                sumi += money
                print("Sumi now has: ", sumi, "Sarah now has: ", sarah, "\n")
            if(p == 5):
                bank += money
                print("Sumi now has: ", sumi, "Bank now has: ", bank, "\n")
    elif (x == 4):
        mc= int(input("Choose option:\n1 for Ammar.\n2 for Aisha.\n3 for Sarah.\n4 for Summi bebiz.\n"))
        if(mc == 1):
            bank = bank - 200
            aj += 200
            print("Ammar now has:", aj, "Bank now has:", bank, "\n")
        elif(mc == 2):
            bank = bank - 200
            aisha += 200
            print("Aisha has:", aisha, "Bank now has:", bank, "\n")
        elif(mc == 3):
            bank = bank - 200
            sarah += 200
            print("Sarah has:", sarah, "Bank now has:", bank, "\n")
        elif(mc == 4):
            bank = bank - 200
            sumi += 200
            print("Summayah has:", sumi, "Bank now has:", bank, "\n")
            
    


