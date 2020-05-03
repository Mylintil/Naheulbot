from dices import roll

class character:


    name = "Péhainjy"
    etat = "V" #V vivant, #I inconscient, #D décédé

    EV = 20

    AT = 8
    PRD = 8

    DEG = [1,2]
    PR = 0

    COU = 10

    def prendre_un_coup(self, degats):
        degats_prot = degats-self.PR
        if(degats_prot < 0):
            degats_prot = 0

        self.EV = self.EV - degats_prot
        if(self.EV < 0):
            self.EV = 0

        if(self.EV == 0):
            print(self.name, "meurt.")
            self.etat = "D"
        elif(self.EV < 3):
            print(self.name, "tombe inconscient.")
            self.etat = "I"

    def attaquer(self, mechant):
        if(mechant.etat != "D"):
            degats = roll(self.DEG[0],"D6") + self.DEG[1]
            if(self.etat == "V"):
                mechant.prendre_un_coup(degats)# nD6+m
                print(self.name, "porte un coup à ", mechant.name, "et lui inflige", degats, "dégats!" )

            elif(self.etat == "I"):
                print("Je crois que ", self.name, "est inconscient")
            elif(self.etat == "D"):
                print("Mais enfin", self.name, "est mort!! Il ne peut pas attaquer")
        else:
            print("Pas la peine d'attaquer le cadavre de", mechant.name)
