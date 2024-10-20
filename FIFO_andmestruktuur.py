patients = []  # Loome tühja loendi patsientide jaoks

# Funktsioonid järjekorra haldamiseks
def add_patient(name):
    patients.append(name)  # Lisab patsiendi nime loendi lõppu

def call_patient():
    return patients.pop(0) if patients else "Järjekord on tühi."  # Eemaldab ja tagastab esimese patsiendi või teate, kui järjekord on tühi

def next_patient():
    return patients[0] if patients else "Järjekord on tühi."  # Tagastab järgmise patsiendi nime või teate, kui järjekord on tühi

def queue_size():
    return len(patients)  # Tagastab järjekorras olevate patsientide arvu

# Näide
add_patient("Eldur")  # Lisab patsiendi nimega "Eldur" järjekorda
add_patient("Pets")    # Lisab patsiendi nimega "Pets" järjekorda
add_patient("Leena")  # Lisab patsiendi nimega "Leena" järjekorda

print("Järjekord:", ', '.join(patients))  # Kuvab järjekorras olevate patsientide nimed
print("Kutsutud patsient:", call_patient())  # Kutsutud patsient ja eemaldab selle järjekorrast
print("Järgmine patsient:", next_patient())  # Kuvab järgmise patsiendi nime, ilma et seda järjekorrast eemaldataks
print("Järjekorras olevate patsientide arv:", queue_size())  # Kuvab järjekorras olevate patsientide arvu
print("Järjekord pärast patsiendi väljakutsumist:", ', '.join(patients))  # Kuvab järjekorra pärast patsiendi väljakutsumist
