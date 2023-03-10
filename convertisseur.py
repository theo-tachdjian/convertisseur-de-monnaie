from tkinter import *

def add_to_history(text):
    historique_list.insert(END, text)

convertisseur = Tk()
convertisseur.title("convertisseur de devise")
screen_x = int(convertisseur.winfo_screenwidth())
screen_y = int(convertisseur.winfo_screenheight())
convertisseur_x = 500
convertisseur_y = 600

posX = (screen_x // 2) - (convertisseur_x // 2)
posY = (screen_y // 2) - (convertisseur_y // 2)

geo = "{}x{}+{}+{}".format(convertisseur_x, convertisseur_y, posX, posY)
convertisseur.geometry(geo)

convertisseur.resizable(width=False, height=False)

convertisseur.config(background='#E7E7E7')

class Interface(Frame):

    def __init__(self, convertisseur, **kwargs):
        Frame.__init__(self, convertisseur, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0


        self.label_choix_monnaie = Label(self, text="Choisissez le sens de conversion", fg='red')
        self.label_choix_monnaie.pack()

        self.sens = StringVar()

        self.s1 = Radiobutton(self, text='Euros -> Autre monnaie', variable=self.sens, value='s1')
        self.s1.pack()

        self.s2 = Radiobutton(self, text='Autre monnaie -> Euros', variable=self.sens, value='s2')
        self.s2.pack()

        self.label_choix_monnaie = Label(self, text="Choisissez l'autre monnaie", fg='blue')
        self.label_choix_monnaie.pack()

        self.monnaie = StringVar()

        self.m1 = Radiobutton(self, text='Dollars US', variable=self.monnaie, value='Dollars US')
        self.m1.pack()

        self.m2 = Radiobutton(self, text='Livres Sterling', variable=self.monnaie, value='Livres Sterling')
        self.m2.pack()

        self.m3 = Radiobutton(self, text='Yen', variable=self.monnaie, value='Yen')
        self.m3.pack()

        self.m4 = Radiobutton(self, text='Pesos mexicains', variable=self.monnaie, value='Pesos mexicains')
        self.m4.pack()

        self.m5 = Radiobutton(self, text='Francs CFA', variable=self.monnaie, value='Francs CFA')
        self.m5.pack()

        self.m6 = Radiobutton(self, text='Dinars algeriens', variable=self.monnaie, value='Dinars algeriens')
        self.m6.pack()

        self.m7 = Radiobutton(self, text='Roubles russes', variable=self.monnaie, value='Roubles russes')
        self.m7.pack()

        self.m8 = Radiobutton(self, text='Yuan', variable=self.monnaie, value='Yuan')
        self.m8.pack()

        self.m9 = Radiobutton(self, text='Roupies indiens', variable=self.monnaie, value='Roupies indiens')
        self.m9.pack()

        self.m10 = Radiobutton(self, text='Reals bresiliens', variable=self.monnaie, value='Reals bresiliens')
        self.m10.pack()

        self.labelentry = Label(self, text="Entrez la somme de depart", fg='blue')
        self.labelentry.pack()

        self.entry = Entry(self)
        self.entry.pack()

        self.bouton = Button(self, text="CONVERTIR", command=self.convert, fg='red')
        self.bouton.pack()

        self.output = StringVar()
        self.out = Label(self, textvariable=self.output, fg='green')
        self.out.pack()

        self.error = StringVar()
        self.err = Label(self, textvariable=self.error, fg='red')
        self.err.pack()

    def convert(self):
        ent = self.entry.get()
        if ent == '':
            ent = 0
        else:
            ent = float(ent)
        a = 1.24
        b = 0.79
        c = 146.04
        d = 17.04
        e = 655.62
        f = 106.81
        g = 58.22
        h = 7.64
        i = 77.04
        j = 3.16
        if self.sens.get() == 's1':
            if self.monnaie.get() == 'Dollars US':
                o = ent * a
                self.error.set('')
            elif self.monnaie.get() == 'Livres Sterling':
                o = ent * b
                self.error.set('')
            elif self.monnaie.get() == 'Yen':
                o = ent * c
                self.error.set('')
            elif self.monnaie.get() == 'Pesos mexicains':
                o = ent * d
                self.error.set('')
            elif self.monnaie.get() == 'Francs CFA':
                o = ent * e
                self.error.set('')
            elif self.monnaie.get() == 'Dinars algeriens':
                o = ent * f
                self.error.set('')
            elif self.monnaie.get() == 'Roubles russes':
                o = ent * g
                self.error.set('')
            elif self.monnaie.get() == 'Yuan':
                o = ent * h
                self.error.set('')
            elif self.monnaie.get() == 'Roupies indiens':
                o = ent * i
                self.error.set('')
            elif self.monnaie.get() == 'Reals bresiliens':
                o = ent * j
                self.error.set('')
            else:
                self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
                print('Probleme')
            monnaie_arrivee = self.monnaie.get()
        elif self.sens.get() == 's2':
            if self.monnaie.get() == 'Dollars US':
                o = ent / (a + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Livres Sterling':
                o = ent / (b + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Yen':
                o = ent / (c + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Pesos mexicains':
                o = ent / (d + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Francs CFA':
                o = ent / (e + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Dinars algeriens':
                o = ent / (f + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Roubles russes':
                o = ent / (g + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Yuan':
                o = ent / (h + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Roupies indiens':
                o = ent / (i + 0.0)
                self.error.set('')
            elif self.monnaie.get() == 'Reals bresiliens':
                o = ent / (j + 0.0)
                self.error.set('')
            else:
                print('probleme')
                self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
            monnaie_arrivee = 'Euros'
        else:
            self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
            print('pb')
        self.output.set('Vous avez ' + str(o) + ' ' + monnaie_arrivee)
        historique_list.insert(END, str(o))


historique = Frame(convertisseur, pady=8)
historique_list = Listbox(historique, width=50, height=6)
historique_list.grid(column=0, row=0, sticky=(N, W, E, S))
scrollbar = Scrollbar(historique, orient=VERTICAL, command=historique_list.yview)
scrollbar.grid(column=1, row=0, sticky=(N, S))
historique_list['yscrollcommand'] = scrollbar.set
historique.grid_columnconfigure(0, weight=1)
historique.grid_rowconfigure(0, weight=1)

interface = Interface(convertisseur)

bouton = Button(convertisseur, text="Quitter", command=convertisseur.destroy, fg="red")
bouton.pack()

historique.pack()
interface.mainloop()
interface.destroy()