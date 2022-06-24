#
#
# 3) Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria?
#
#
from functions import ReadFile

data_students = ReadFile.load_csv()
data = data_students[0]
# list_school = data_students[1]

monitoring = 0
disapproved = 0
for studant in data:
    if studant['ano'] == 3:

        median = (studant['nota_semestre_1'] + studant['nota_semestre_2']) / 2
        if (median < 7 and studant['nota_exame'] < 5) or studant['faltas'] > 15:
            disapproved += 1

            if studant['monitoria'] == 'True':
                monitoring += 1
print(f"\n{'=':=^70}")
print(f'--- {disapproved} alunos do 3 ano reprovaram e apenas {monitoring} procuraram monitoria.')
print(f"{'=':=^70}\n")

# RESPOSTA DO PRINT ABAIXO
# ======================================================================
# --- 1166 alunos do 3 ano reprovaram e apenas 592 procuraram monitoria.
# ======================================================================