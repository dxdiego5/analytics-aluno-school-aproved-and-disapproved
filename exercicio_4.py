#
#
# 4) De todos os alunos que reprovaram quantos foram por falta e quantos foram por nota, e quantos foram por ambas as causas?
#
#
from functions import ReadFile

data_students = ReadFile.load_csv()
data = data_students[0]

faults = 0
note = 0
note_and_faltas = 0

for studant in data:
    median = (studant['nota_semestre_1'] + studant['nota_semestre_2']) / 2

    if median < 7 and studant['nota_exame'] < 5:
        note += 1

    if studant['faltas'] > 15:
        faults += 1

    if (studant['faltas'] > 15) and (median < 7 and studant['nota_exame'] < 5):
        note_and_faltas += 1

print(f"\n{'=':=^70}")
print(f'--- {note} Reprovarão por nota.')
print(f'--- {faults} Reprovarão por falta.')
print(f'--- {note_and_faltas} Reprovarão por falta e nota.')
print(f"{'=':=^70}\n")

# RESPOSTA DO PRINT ABAIXO
# ======================================================================
# --- 2063 Reprovarão por nota.
# --- 2420 Reprovarão por falta.
# --- 981 Reprovarão por falta e nota.
# ======================================================================
