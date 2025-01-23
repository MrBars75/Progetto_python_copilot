import random

class Dipendente:
    def __init__(self, nome, cognome, ruolo, eta, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.eta = eta
        self.stipendio = stipendio

    def __str__(self):
        return f"{self.nome} {self.cognome}, Ruolo: {self.ruolo}, Età: {self.eta}, Stipendio: {self.stipendio}€"
    
dipendenti = []

nomi = ["Mario", "Luigi", "Giovanni", "Paolo", "Francesco", "Luca", "Marco", "Antonio", "Roberto", "Stefano"]
cognomi = ["Rossi", "Bianchi", "Verdi", "Neri", "Gialli", "Marroni", "Esposito", "Russo", "Ferrari", "Colombo"]
ruoli = ["Manager", "Developer", "Analyst", "Designer", "Tester", "Support", "HR", "Sales", "Marketing", "Finance"]

for _ in range(20):
    nome = random.choice(nomi)
    cognome = random.choice(cognomi)
    ruolo = random.choice(ruoli)
    eta = random.randint(25, 65)
    stipendio = random.randint(30000, 80000)
    dipendenti.append(Dipendente(nome, cognome, ruolo, eta, stipendio))

def restituisci_nome(dipendenti):
    return [d.nome for d in dipendenti]

def salario_minimo_massimo(dipendenti):
    stipendi = [d.stipendio for d in dipendenti]
    return min(stipendi), max(stipendi)

def salario_maggiore_di_valore(dipendenti, valore):
    return [d for d in dipendenti if d.stipendio > valore]