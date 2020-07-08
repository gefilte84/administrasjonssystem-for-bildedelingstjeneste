# Tom Krystian Noodt 147
# Kristoffer Sørensen 140
# Najim Zaouaghi 161
# Slavko Radisevic 132

#Noen av funksjonene er tatt utgangspunkt i gruppens tidligere levering i PRG1000R oblig2
#Passer på at filene blir oppretet visst de ikke eksisterer fra før av
toppBildefil = open ('Bilde10.txt', 'a')
toppTag = open('TagForBilde10.txt','a')
toppKommentar = open ('Kommentar10.txt','a')
toppBruker = open ('Bruker10.txt', 'a')
toppLikes = open ('Likes10.txt', 'a')
toppEmne = open ('Emneknagg10.txt','a')

toppBildefil.close ()
toppTag.close ()
toppKommentar.close ()
toppBruker.close ()
toppLikes.close ()
toppEmne.close ()

### Hovedmeny ###
def main ():
    
    programkjorer=True
    while programkjorer:
        #Meny design og oversikt over eksisterende funksjoner
        print()
        print("//**Administrasjonssystem for bildedelingstjeneste**//")
        print()
        print("For valg av operasjon: skriv inn en av følgende kommandoer:")
        print("----------------")
        print("Registrere: \nBruker: 1\nBilde: 2\nKommentar: 3\nLike: 4\nEmneknagg: 5\nTagForBilde : 6")
        print("----------------")
        print("Slette: \nBruker: 7\nBilde: 8\nKommentar: 9")
        print("----------------")
        print("Vis: \nBilder og fotograf: 10\nAntall bilder per bruker: 11\nAntall likes på bilder: 12\nKommentarer på et bilde: 13")
        print("Bilde og fotograf via emneknagg: 14\nKommentarer via emneknagg: 15")
        print("----------------")
        print("Avslutt: 16")
        print("----------------")

        print('Skriv inn ønsket funksjon:')
        operasjon = input ('')

        #Meny for valg av funksjoner
        if operasjon == '1':
            registrerBruker ()
        elif operasjon == '2':
            registrerBilde ()
        elif operasjon == '3':
            registrerKommentar ()
        elif operasjon == '4':
            registrerLike ()
        elif operasjon == '5':
            registrerEmneknagg ()
        elif operasjon == '6':
            registrerTagForBilde ()
        elif operasjon == '7':
            slettBruker ()
        elif operasjon == '8':
            slettBilde ()
        elif operasjon == '9':
            slettKommentarer ()
        elif operasjon == '10':
            visBildeFotograf ()
        elif operasjon == '11':
            visBrukereBilde ()
        elif operasjon == '12':
            visLikesBilde ()
        elif operasjon == '13':
            visAlleKommentarer () #Det er mulighet for at denne skaper bugs
        elif operasjon == '14':
            visEmneknaggBildeFotograf ()
        elif operasjon == '15':
            visInfoEmneknagg ()
        elif operasjon == '16':
            programkjorer = False

    print ('Program avsluttet')

####################################################
### Registrer-funksjoner ###
def registrerBruker ():
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon registrer bruker -----')
    print ('-------------------------------------------------------\n')

    nyInndata = True
    while nyInndata == True:

        # Ber brukeren oppgi nødvendig informasjon
        brukerID = input ('Bruker: ')
        fornavn = input ('Fornavn: ')
        etternavn = input ('Etternavn: ')
        epost = input ('Epost: ')

        # Sjekker om input oppfyller krav, hvis ja skrives input til filen
        if  finnesBruker (brukerID) ==False:
            brukerfil = open ('Bruker10.txt', 'a')
            brukerfil.write (brukerID + '\n')
            brukerfil.write (fornavn + '\n')
            brukerfil.write (etternavn + '\n')
            brukerfil.write (epost + '\n')

            brukerfil.close ()

            print('Bruker registrert!\n')
        else:
            print('Bruker allerede registrert!\n')
            

        print ('Ønsker du å registrere en ny bruker? (Ja/ja)')
        svar = input ('')

        if svar == 'ja' or svar == 'Ja':
            nyInndata = True
        else:
            nyInndata = False

def registrerBilde ():
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon registrer bilde -----')
    print ('-------------------------------------------------------\n')

    # Ber brukeren oppgi nødvendig informasjon
    print('For å registere et bilde må du være en registrert bruker')
    brukerID = input ('Bruker: ')
    bildeID = input ('Bilde: ')
    beskrivelse = input ('Beskriv bildet: ')
    opplastetDato = input ('Skriv inn dato for bildet: ')

    # Kjører tester for å sjekke om bilde og bruker eksisterer
    # for å gi tilbakemelding til bruker
    if finnesBruker (brukerID) ==False:
        print('Bruker eksisterer ikke!')
    if finnesBilde (bildeID) ==True:
        print('Bilde eksisterer allerede!')

    # Sjekker om input oppfyller krav, hvis ja skrives input til filen
    if finnesBruker (brukerID) ==True and finnesBilde (bildeID) ==False:
        bildefil = open ('Bilde10.txt', 'a')

        bildefil.write (bildeID + '\n')
        bildefil.write (beskrivelse + '\n')
        bildefil.write (opplastetDato + '\n')
        bildefil.write (brukerID + '\n')

        bildefil.close ()

        print('Bilde registrert!')

def registrerKommentar ():
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon registrer kommentar -----')
    print ('-------------------------------------------------------\n')

    print('For å registere en kommentar må du ha en bruker og ha riktig bilde')

    # Ber brukeren oppgi nødvendig informasjon
    brukerID = input ('Bruker: ')
    bildeID = input ('Bilde: ')
    kommentar = input ('Skriv inn kommentar på bildet: ')

    # Kjører tester for å sjekke om bilde og bruker eksisterer
    # for å gi tilbakemelding til bruker
    if finnesBruker (brukerID) ==False:
        print('Bruker eksisterer ikke!')
    if finnesBilde (bildeID) ==False:
        print('Bilde eksisterer ikke!')

    # Sjekker om input oppfyller krav, hvis ja skrives input til filen
    if finnesBruker (brukerID) ==True and finnesBilde (bildeID) ==True:
        kommentarfil = open ('Kommentar10.txt', 'a')

        kommentarfil.write (bildeID + '\n')
        kommentarfil.write (brukerID + '\n')
        kommentarfil.write (kommentar + '\n')

        kommentarfil.close ()

        print('Kommentar registrert!')

def registrerLike ():
    # Funksjon for registrering av likes
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon registrer like -----')
    print ('-------------------------------------------------------\n')

    print('For å registere en like må du være en registrert bruker og ha et opplastet bilde')

    # Ber brukeren oppgi nødvendig informasjon
    bildeID = input ('Bilde: ')
    brukerID = input ('Bruker: ')

    # Kjører tester for å sjekke om bilde, bruker og like eksisterer
    # for å gi tilbakemelding til bruker
    if finnesBilde (bildeID) ==False:
        print('Bilde eksisterer ikke!')
    if finnesBruker(brukerID) ==False:
        print('Bruker eksisterer ikke!')
    if finnesLikeAllerede(brukerID, bildeID) ==True:
        print('Like for bilde eksisterer allerede!')

    # Sjekker om alle kravene er oppfylt for å så skrive til filen        
    if finnesLikeAllerede(brukerID, bildeID) ==False and finnesBilde(bildeID) ==True and finnesBruker (brukerID) ==True:
        likesfil = open ('Likes10.txt', 'a')
        likesfil.write (bildeID + '\n')
        likesfil.write (brukerID + '\n')
        likesfil.close ()

        print('Like registrert!')

def registrerEmneknagg ():
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon registrer emneknagg -----')
    print ('-------------------------------------------------------\n')

    ny_emne=True
    while ny_emne==True:

        # Ber brukeren registrere ønsket emneknagg
        emneknaggID = input('Skriv inn emneknagg-id: ')
        emneknaggNavn = input ('Skriv inn emneknagg-navn: ')

        # Sjekker om kravet er oppfylt for å så skrive til filen
        if finnesEmneknagg(emneknaggID) ==False:
            emneknaggfil = open ('Emneknagg10.txt', 'a')
            emneknaggfil.write (emneknaggID + '\n')
            emneknaggfil.write (emneknaggNavn + '\n')

            emneknaggfil.close ()

            print('Emneknagg registrert!\n')

        else:
            print ('Emneknagg finnes fra før')
        print ('-------------------------------------------------------\n')
            
        svar=input('Registrere ny emneknagg? ')
        if svar=='Nei' or svar=='nei':
            ny_emne=False

def registrerTagForBilde ():
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon tag for bilde -----')
    print ('-------------------------------------------------------\n')

    print('For å registere en tag må du ha riktig bilde og emneknaggen må være registrert')

    # Ber brukeren oppgi nødvendig informasjon
    bildeID = input ('Bilde: ')
    emneknaggID = input ('Skriv inn emneknagg-id: ')

    # Kjører tester for å sjekke om bilde og emneknagg eksisterer
    # for å gi tilbakemelding til bruker
    if finnesBilde (bildeID) ==False:
        print('Bilde eksistrer ikke!')
    if finnesEmneknagg(emneknaggID) ==False:
        print('Emneknaggen eksisterer ikke!')

    # Sjekker om alle kravene er oppfylt for å så skrive til filen
    if finnesBilde(bildeID) ==True and finnesEmneknagg (emneknaggID) ==True:
        tagforbildefil = open ('TagForBilde10.txt', 'a')

        tagforbildefil.write (bildeID + '\n')
        tagforbildefil.write (emneknaggID + '\n')

        tagforbildefil.close ()

        print('Emneknagg lagt til på bilde!')

####################################################
### Slett-funksjoner ###
def slettBruker ():
    """Slett bruker ved bruk av temp-fil"""

    #importerer os for å kunne erstatte originalfil med tempfil
    import os
    nyInndata = True
    while nyInndata == True:
        print ('-------------------------------------------------------')
        print ('----- Kjører operasjon slett bruker -----')
        print ('-------------------------------------------------------\n')    

        brukerID = input ('BrukerID: ')

        # Sjekk om brukeren finnes, og om det er registrert aktivitet på brukerID
        if finnesLike (brukerID)==False and finnesBilde (brukerID) == False and finnesKommentar (brukerID) == False and finnesBruker (brukerID) == True:
            print ('Starter sletting av bruker...')
  
            brukerfil = open ('Bruker10.txt', 'r')
            tempfil = open ('tempfil.txt', 'w')

            linje = brukerfil.readline ()
            while linje != '':

                filFornavn = brukerfil.readline ()
                filEtternavn = brukerfil.readline ()
                filEpost = brukerfil.readline ()

                filBrukerID = linje.rstrip ('\n')
                # Skriver inn linjene, for bruker som ikke skal slettes, til temp-fil
                if filBrukerID != brukerID:

                    tempfil.write (filBrukerID + '\n')
                    tempfil.write (filFornavn)
                    tempfil.write (filEtternavn)
                    tempfil.write (filEpost)

                # Leser neste linje i fila, som da vil være neste brukerID eller blank
                linje = brukerfil.readline ()

            brukerfil.close ()
            tempfil.close ()

            # Erstatter den originale Bruker10.txt-filen med tempfilen
            os.remove ('Bruker10.txt')
            os.rename ('tempfil.txt', 'Bruker10.txt')
            print ('Bruker fjernet!')


        elif finnesBruker(brukerID) == False:

            print ('Brukeren du ønsker å slette finnes ikke')
        else:
            print ('Brukeren kan ikke slettes grunnet følgende registrert aktivitet fra denne brukeren:')
            # Her kommer det if tester for å gi info om hvilke krav som ikke er oppfyllt
            if finnesLike (brukerID) == True:
                print ('Likes')
            if finnesBilde (brukerID) == True:
                print ('Bilder')
            if finnesKommentar (brukerID) == True:
                print ('Kommentarer')
        print ('-------------------------------------------------------\n')

        # Spør om det ønskes å slette flere brukere
        print ('Ønsker du å slette flere brukere? (Ja/ja)')
        svar = input ('')

        if svar == 'ja' or svar == 'Ja':
            nyInndata = True
        else:
            nyInndata = False

def slettBilde ():
    """Slett bilde (+likes +kommentarer) ved bruk av temp-fil"""

    # Importerer os for å kunne erstatte originalfil med tempfil
    import os
    nyInndata = True
    while nyInndata == True:
        print ('-------------------------------------------------------')
        print ('----- Kjører operasjon slett bilde -----')
        print ('-------------------------------------------------------\n')

        bildeID = input ('Bilde-ID: ')

        # Sjekk om brukeren finnes, og om det er registrert aktivitet på brukerID
        if finnesBilde (bildeID) == True:

            #Sjekk om det finnes bilder og kommentarer, hvis det gjør det, kjør funksjonene
            finnerViserKommentarer (bildeID, False)
            visAlleLikes (bildeID)        

            print ('All likes og kommentarer i listen over vil bli slettet, ønsker du fortsatt å slette bildet?(ja)')
            svar = input ('')

            if svar == "ja":

                #Sletting av bilde
                bildefil = open('Bilde10.txt', 'r')
                tempfil = open('temp.txt', 'w')

                filBildeID = bildefil.readline()

                while filBildeID != '':
                    filBeskrivelse = bildefil.readline()
                    filOpplastetDato = bildefil.readline()
                    filFotograf = bildefil.readline()

                    filBildeID = filBildeID.rstrip('\n')

                    if filBildeID != bildeID:
                        tempfil.write (filBildeID + '\n')
                        tempfil.write (filBeskrivelse)
                        tempfil.write (filOpplastetDato)
                        tempfil.write (filFotograf)
                    
                    filBildeID = bildefil.readline()

                bildefil.close()
                tempfil.close()

                os.remove('Bilde10.txt')
                os.rename('temp.txt', 'Bilde10.txt')

                ### Del for fjerning av likes ###
                slettAlleLikes (bildeID)
                ### Del for fjerning av kommentarer ###
                slettAlleKommentarer (bildeID)
        else:
            print ('Bildet finnes ikke og kan derfor ikke slettes.')
        print ('-------------------------------------------------------\n')

        # Spør om det ønskes å slette flere bilder
        print ('Ønsker du å slette et annet bilde? (Ja/ja)')
        svar = input ('')

        if svar == 'ja' or svar == 'Ja':
            nyInndata = True
        else:
            nyInndata = False

def slettKommentarer ():
    print ('-------------------------------------------------------')
    print ('---- Kjører operasjon slett kommentarer av bruker -----')
    print ('-------------------------------------------------------\n')
    
    print ('Skriv inn bruker-id for bruker som ønsker kommentarer slettet')
    brukerID = input ('')
    print ('Skriv inn bruker-id for brukers kommentarer som skal slettes')
    sBrukerID = input ('')

    import os
    
    funnet = False

    kommentarfil = open ('Kommentar10.txt', 'r')
    temp_file = open ('temp.txt', 'w')

    filBildeID = kommentarfil.readline ()
    
    while filBildeID != '':
        kommentarSkalSlettes = False

        filBrukerID = kommentarfil.readline()
        filKommentar = kommentarfil.readline()

        filBildeID = filBildeID.rstrip ('\n')
        filBrukerID = filBrukerID.rstrip('\n')

        if filBrukerID == sBrukerID:

            if erBrukerFotograf (filBildeID, brukerID) == True:
                kommentarSkalSlettes = True
                funnet = True

        #Her må kommentarene skrives inn hvis kommentaren ikke samsvarer
        if kommentarSkalSlettes == False:
            temp_file.write (filBildeID + '\n')
            temp_file.write (filBrukerID + '\n')
            temp_file.write (filKommentar)

        filBildeID = kommentarfil.readline ()
    
    kommentarfil.close ()
    temp_file.close ()
    os.remove('Kommentar10.txt')
    os.rename('temp.txt', 'Kommentar10.txt')

    if funnet == False:
        print ('Det er ingen kommentarer å slette fra denne brukeren!')
    else:
        print ('Kommentarer slettet!')



def erBrukerFotograf(bildeID, brukerID):
    """ Returnerer sant eller usant basert på om bilde finnes """
    bildefil = open ('Bilde10.txt', 'r')
    resultat = False

    bFilBildeID = bildefil.readline ()
    while bFilBildeID != '':

        bFilBeskrivelse = bildefil.readline ()
        bFilOpplastetDato = bildefil.readline ()
        bFilFotograf = bildefil.readline ()

        bFilBildeID = bFilBildeID.rstrip ('\n')
        bFilFotograf = bFilFotograf.rstrip ('\n')

        if (bildeID == bFilBildeID ) and (brukerID == bFilFotograf):
            resultat = True

        bFilBildeID = bildefil.readline ()
    bildefil.close ()

    return resultat
####################################################
### Vis-funksjoner ###

def visAlleKommentarer ():
    print ('-------------------------------------------------------')
    print ('--- Kjører operasjon vis alle kommmentarer på bilde ---')
    print ('-----------------------------------------------------\n')
    
    nyInndata = True
    while nyInndata == True:
        finnerViserKommentarer ('', True)

        print ('-----------------------------------------------------\n')
        
        # Spør om det ønkes å vise flere kommentarer
        print ('Ønsker du å vise kommentarer på et annet bilde? (Ja/ja)')
        svar = input ('')

        if svar == 'ja' or svar == 'Ja':
            nyInndata = True
        else:
            nyInndata = False

def visLikesBilde ():
    print ('-------------------------------------------------------')
    print ('----- Kjører operasjon vis antall likes per bilde -----')
    print ('-------------------------------------------------------\n')

    antallBilder = 0

    bildefil = open ('Bilde10.txt', 'r')
    linje = bildefil.readline ()

    # Teller likes for hver post funnet i fila
    while linje != '':
        antallBilder += 1

        bildeID = linje.rstrip ('\n')
        filBeskrivelse = bildefil.readline ()
        filOpplastetDato = bildefil.readline ()
        filFotograf = bildefil.readline ()

        likesfil = open ('Likes10.txt', 'r')
        linje = likesfil.readline ()

        likeTeller = 0
        while linje != '':
            filBrukerID = likesfil.readline ()

            filBildeID = linje.rstrip ('\n')
            filBrukerID = filBrukerID.rstrip ('\n')
            
            if filBildeID == bildeID:
                likeTeller +=1

            linje = likesfil.readline ()
        print ('Bilde-id:', bildeID)
        print ('Antall likes:', likeTeller, '\n')

        likesfil.close ()
        linje = bildefil.readline ()

    bildefil.close ()

    if antallBilder == 0:
        print ('Det er ingen bilder registrert i systemet!\n')

    print ('-------------------------------------------------------\n')

    # For å unngå visning av meny
    svar = input ('Trykk enter for å vise meny\n')

def visEmneknaggBildeFotograf ():
    print ('----------------------------------------------------------------')
    print ('----- Kjører operasjon vis bilde og fotograf via emneknagg -----')
    print ('--------------------------------------------------------------\n')

    #While loop som sjekker for om bruker ønsker å søke på flere emneknagger
    nyInndata = True
    while nyInndata == True:

        # Ber brukeren skrive inn emneknagg
        print ('Skriv inn emneknagg:')
        emneknaggnavn = input ('')
        print ('')

        resultat = False
        antSokeRes = 0

        emneknaggfil = open ('Emneknagg10.txt', 'r')

        linje = emneknaggfil.readline ()
        while linje != '':

            filEmneknaggnavn = emneknaggfil.readline ()

            filEmneKnaggID = linje.rstrip('\n')
            filEmneknaggnavn = filEmneknaggnavn.rstrip ('\n')

            if filEmneknaggnavn == emneknaggnavn:
                resultat = True
                emneknaggID = filEmneKnaggID

            linje = emneknaggfil.readline ()
        emneknaggfil.close ()

        if resultat == True:
            # Emneknaggnavnet finnes og emneknaggid er lagret i emneknaggID

            tagForBildefil = open ('TagForBilde10.txt', 'r')
            linje = tagForBildefil.readline ()
            while linje != '':
                
                filEmneknaggID =tagForBildefil.readline ()

                filBildeID = linje.rstrip ('\n')
                filEmneKnaggID = filEmneknaggID.rstrip ('\n')

                # Sjekk for om bildet i posten har emneknaggen vi leter etter

                if emneknaggID == filEmneKnaggID:
                    bildeID = filBildeID
                    # Finne forfatter info fra Bilde10.txt
                    
                    bildefil = open ('Bilde10.txt', 'r')
                    linje = bildefil.readline ()
                    while linje != '':

                        filBeskrivelse = bildefil.readline ()
                        filOpplastetDato = bildefil.readline ()
                        filFotograf = bildefil.readline ()

                        filBildeID = linje.rstrip ('\n')
                        if filBildeID == bildeID:
                            fotograf = filFotograf.rstrip ('\n')

                            print ('Bilde-id:', bildeID, ', Fotograf:', fotograf)
                            print ()

                        linje = bildefil.readline ()
                    bildefil.close ()

                linje = tagForBildefil.readline ()

            tagForBildefil.close ()
        else:
            print ('Emneknaggen finnes ikke\n')
        
        print ('-------------------------------------------------------')

        # Spør om det ønskes å søke i ny emneknagg
        print ('Ønsker du å søke på en annen emneknagg? (Ja/ja)')
        svar = input ('')

        if svar == 'ja' or svar == 'Ja':
            nyInndata = True
        else:
            nyInndata = False

def visBrukereBilde():
    print ('-----------------------------------------------------------')
    print ('--- Kjører operasjon for å vise antall bilder pr bruker ---')
    print ('---------------------------------------------------------\n')

    brukerfil=open('Bruker10.txt','r')
    brukerID = brukerfil.readline()

    while brukerID !='':
        bildeTeller = 0
        brukerID = brukerID.rstrip('\n')
        fornavn = brukerfil.readline()
        etternavn = brukerfil.readline()
        epost = brukerfil.readline()

        bildefil = open ('Bilde10.txt', 'r')
        bildeID = bildefil.readline()
        
        while bildeID !='':
            beskrivelse = bildefil.readline()
            opplastetDato = bildefil.readline()
            fotograf = bildefil.readline()

            fotograf = fotograf.rstrip ('\n')

            if brukerID == fotograf:
                bildeTeller +=1

            bildeID = bildefil.readline()
        print ('BrukerID: ',brukerID)
        print ('Antall bilder: ',bildeTeller)
        print ('')

        bildefil.close()

        brukerID = brukerfil.readline()
    brukerfil.close()

    print ('-------------------------------------------------------\n')

    # For å unngå visning av meny
    svar = input ('Trykk enter for å vise meny\n')

def visInfoEmneknagg ():
    print ('---------------------------------------------------------------')
    print ('------- Kjører operasjon vis kommentarer via emneknagg --------')
    print ('-------------------------------------------------------------\n')
    
    # While loop som sjekker for om bruker ønsker å søke på flere emneknagger
    nyInndata = True
    while nyInndata == True:
        print ('Skriv inn emneknaggnavn:')
        emneknaggnavn = input ('')
        print ('')

        emneknaggfil = open ('Emneknagg10.txt', 'r')
        resultat = False
        antSokeRes = 0

        linje = emneknaggfil.readline ()

        while linje != '':

            filEmneknaggnavn = emneknaggfil.readline ()

            filEmneKnaggID = linje.rstrip('\n')
            filEmneknaggnavn = filEmneknaggnavn.rstrip ('\n')

            if filEmneknaggnavn == emneknaggnavn:
                resultat = True
                emneKnaggID = filEmneKnaggID

            linje = emneknaggfil.readline ()
        emneknaggfil.close ()

        if resultat == True:
        # Nå er emneknaggnavnfunnet og emneknaggen finnes

            tagForBildefil = open ('TagForBilde10.txt', 'r')

            linje = tagForBildefil.readline ()
            while linje != '':

                filEmneKnaggID = tagForBildefil.readline ()

                filBildeID = linje.rstrip ('\n')
                filEmneKnaggID = filEmneKnaggID.rstrip ('\n')

                if filEmneKnaggID == emneKnaggID:
                    # Her har vi funnet et nytt bilde
                    bildeID = filBildeID

                    kommentarfil = open('Kommentar10.txt', 'r')

                    linje = kommentarfil.readline ()
                    while linje != '':
                        filBrukerID = kommentarfil.readline ()
                        filKommentar = kommentarfil.readline ()

                        filbildeID = linje.rstrip ('\n')
                        filBrukerID = filBrukerID.rstrip ('\n')
                        filKommentar = filKommentar.rstrip ('\n')

                        if filbildeID == bildeID:

                            # bildeID er funnet
                            brukerID = filBrukerID
                            kommentar = filKommentar
                            # Mangler fornavn og etternavn
                            navnFunnet=False

                            brukerfil = open ('Bruker10.txt', 'r')
                            linje = brukerfil.readline ()
                            while linje !='':

                                filFornavn = brukerfil.readline ()
                                filEtternavn = brukerfil.readline ()
                                filEpost = brukerfil.readline ()

                                filBrukerID = linje.rstrip ('\n')
                                filFornavn = filFornavn.rstrip ('\n')
                                filEtternavn = filEtternavn.rstrip ('\n')
                                
                                if filBrukerID == brukerID:
                                    fornavn = filFornavn
                                    etternavn = filEtternavn
                                    navnFunnet = True

                                linje = brukerfil.readline ()
                            brukerfil.close ()
                            # Nå er fornavn etternavn funnet og alle variablene kan printes.

                            print ('Bilde-id:', bildeID)
                            print ('Bruker-id:', brukerID, ', Fornavn:', fornavn, ', Etternavn:', etternavn)
                            print ('Kommentar:', kommentar, '\n')

                            antSokeRes +=1

                        linje = kommentarfil.readline ()
                    kommentarfil.close ()



                linje = tagForBildefil.readline ()
            tagForBildefil.close ()
        else:
            print ('Emneknaggen finnes ikke')

        print ('Antall resultater funnet i søket:', antSokeRes)
        print ('---------------------------------------------------------------\n')
        
        # Spørsmål om søk på ny emneknagg
        print ('Ønsker du å vise kommentarer på et annet bilde? (Ja/ja)')
        svar = input ('')

        if svar == 'ja' or svar == 'Ja':
            nyInndata = True
        else:
            nyInndata = False

def visBildeFotograf():
    print ('----------------------------------------------------------------------')
    print ('----- Kjører operasjon å vise bilder med informasjon om fotograf -----')
    print ('--------------------------------------------------------------------\n')

    bildefil = open ('Bilde10.txt', 'r')
    bildeID = bildefil.readline()

    while bildeID !='':
        filbeskrivelse = bildefil.readline ()
        filOpplastetDato = bildefil.readline ()
        filFotograf = bildefil.readline ()

        bildeID = bildeID.rstrip('\n')
        
       
        print('BildeID: ',bildeID)
        print('Fotograf: ',filFotograf)

        bildeID = bildefil.readline()

    bildefil.close()

    print ('-------------------------------------------------------\n')
    # For å unngå visning av meny
    svar = input ('Trykk enter for å vise meny\n')

####################################################
### Finnes-funksjoner ###

def finnesBilde (bildeID):
    """ Returnerer sant eller usant basert på om bilde finnes """

    bildefil = open ('Bilde10.txt', 'r')
    resultat = False

    linje = bildefil.readline ()

    while linje != '':
        linje = linje.rstrip('\n')

        if linje == bildeID:
            resultat = True

        linje = bildefil.readline ()
    bildefil.close ()

    return resultat

def finnesBruker (brukerID):
    """ Returnerer sant eller usant basert på om bruker finnes """
    
    brukerfil = open ('Bruker10.txt', 'r')
    resultat = False

    linje = brukerfil.readline ()
    
    while linje != '':
        linje = linje.rstrip('\n')

        if linje == brukerID:
            resultat = True

        linje = brukerfil.readline ()
    brukerfil.close ()

    return resultat

def finnesKommentar (brukerID):
    """ Returnerer sant eller usant basert på om kommentar finnes """

    kommentarfil = open ('Kommentar10.txt', 'r')
    resultat = False

    linje = kommentarfil.readline ()
    
    while linje != '':
        linje = linje.rstrip('\n')

        if linje == brukerID:
            resultat = True

        linje = kommentarfil.readline ()
    kommentarfil.close ()

    return resultat

def finnesLike (brukerID):
    """ Returnerer sant eller usant basert på om like finnes """

    likefil = open ('Likes10.txt', 'r')
    resultat = False

    linje = likefil.readline ()
    
    while linje != '':
        linje = linje.rstrip('\n')

        if linje == brukerID:
            resultat = True

        linje = likefil.readline ()
    likefil.close ()

    return resultat

def finnesLikeAllerede (brukerID, bildeID):
    """ Sjekker om like på bilde eksisterer allerede og returnerer resultat """

    likefil = open ('Likes10.txt', 'r')
    resultat = False

    linje = likefil.readline ()  
    while linje != '':
        filBrukerID = likefil.readline ()
        
        filBildeID = linje.rstrip('\n')
        filBrukerID = filBrukerID.rstrip('\n')

        if filBrukerID == brukerID and filBildeID == bildeID:
            resultat = True
            
        linje = likefil.readline ()

    likefil.close ()

    return resultat
              
def finnesEmneknagg (emneknaggID):
    """ Returnerer sant eller usant basert på om emneknagg finnes """

    emneknaggfil = open ('Emneknagg10.txt', 'r')
    resultat = False

    linje = emneknaggfil.readline ()

    while linje != '':
        filEmneknagg = emneknaggfil.readline ()

        linje = linje.rstrip('\n')
        filEmneknagg = filEmneknagg.rstrip ('\n')

        if linje == emneknaggID:
            resultat = True

        linje = emneknaggfil.readline ()
    emneknaggfil.close ()

    return resultat

####################################################
### Delfunksjoner av meny-funksjoner ###

def finnerViserKommentarer (bildeID, trengerID):
    # Denne delen er her for å kunne bruke funksjonen i både slettBilde og menyfunksjonen for visning av kommentarer for et gitt bilde.
    if trengerID == True:
        print ('Skriv inn bilde-ID: ')
        bildeID = input ('')
        print ('')
        if finnesBilde (bildeID) == False:
            print ('Bildet finnes ikke!')
    
    # Her starter funksjonen
    antKommentarer = 0
    kommentarFil = open ('Kommentar10.txt', 'r')
    
    linje = kommentarFil.readline ()
    while linje != '':
        filBildeID = linje.rstrip ()
        filBrukerID = kommentarFil.readline ()
        filKommentar = kommentarFil.readline ()

        filBrukerID = filBrukerID.rstrip ('\n')
        filKommentar = filKommentar.rstrip ('\n')

        # Hvis bildeID'en samsvarer med gitt bildeID, print kommentaren
        if filBildeID == bildeID:
            print ('Bruker:', filBrukerID)
            print (filKommentar, '\n')

            antKommentarer += 1
        linje = kommentarFil.readline ()
        
    kommentarFil.close ()

    if trengerID == False:
        print ('\nAntall Kommentarer registrert på bildet:', antKommentarer, '\n')

def visAlleLikes (bildeID):
    '''Brukes til å vise alle kommentarer for slettBilde () '''
    tempVariabel = 'temp'
    antKommentarer = 0
    likesfil = open ('Likes10.txt', 'r')
    
    linje = likesfil.readline ()
    while linje != '':
        filBildeID = linje.rstrip ()
        filBrukerID = likesfil.readline ()

        # Hvis bildeID'en samsvarer med gitt bildeID, print kommentaren
        if filBildeID == bildeID:
            print ('Bruker:', filBrukerID, '\n')

            antKommentarer += 1
        linje = likesfil.readline ()
        
    likesfil.close ()

    print ('\nAntall likes registrert på bildet:', antKommentarer, '\n')

def slettAlleKommentarer (bildeID):
    """ Funksjon som sletter alle kommentarer og likes på et gitt bilde """
    import os

    ### Del for å slette kommentarer ###
    kommentarfil = open('Kommentar10.txt', 'r')
    tempfil = open('temp.txt', 'w')

    filBildeID = kommentarfil.readline()

    while filBildeID != '':
        brukerid = kommentarfil.readline()
        kommentar = kommentarfil.readline()

        filBildeID = filBildeID.rstrip('\n')

        if filBildeID != bildeID:
            tempfil.write(filBildeID + '\n')
            tempfil.write(brukerid)
            tempfil.write(kommentar)
        
        filBildeID = kommentarfil.readline()

    kommentarfil.close()
    tempfil.close()

    os.remove('Kommentar10.txt')
    os.rename('temp.txt', 'Kommentar10.txt')

def slettAlleLikes (bildeID):
    """ Funksjon som sletter alle kommentarer og likes på et gitt bilde """
    import os

    likesfil = open('Likes10.txt', 'r')
    tempfil = open('temp.txt', 'w')

    filBildeID = likesfil.readline()

    while filBildeID != '':
        filBrukerID = likesfil.readline()

        filBildeID = filBildeID.rstrip('\n')

        if filBildeID != bildeID:
            tempfil.write(filBildeID + '\n')
            tempfil.write(filBrukerID)
        
        filBildeID = likesfil.readline()

    likesfil.close()
    tempfil.close()

    os.remove('Likes10.txt')
    os.rename('temp.txt', 'Likes10.txt')    

main ()
