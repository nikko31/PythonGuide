#!/usr/bin/env python
"""
script che legge dei file aventi estensione .data, per ciascun file calcola *val min *val max *val medio
e salva su file 'nome_input'.dataout. Lo script prende in input un argomento opzionale 'out_dir_name',che indica
la directory nella quale salvare i file di output. Se viene omesso i file di output vengono salvati
 in una directory di nome 'out' che se non esiste viene creata
"""
import os
import sys

out_dir_name = sys.argv[1] if sys.argv[1:] else 'out'
try:
    os.mkdir(out_dir_name)
except FileExistsError:
    print("cartella esistente")
for file in os.listdir():
    if file.endswith('.data'):
        # apro il file da cui leggo i numeri
        rd = open(file, 'r')
        # apro il file in cui scrivo i valori
        wr = open(os.path.join(out_dir_name,file+'out'), 'w')
        for line in rd:
            numbers = [float(number) for number in line.split()]
            wr.write("valore max= %.2f valore minimo= %.2f valore medio= %.2f\n"
                  % (max(numbers), min(numbers), sum(numbers) / len(numbers)))
