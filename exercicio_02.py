#
#
# 2) Quantos alunos do 1º ano foram aprovados sem exame?
#
#
from functions import ReadFile

data_students = ReadFile.load_csv()
data = data_students[0]

message = ''
count_stud_aproved = 1
for studants in data:
    median = (studants['nota_semestre_1'] + studants['nota_semestre_2']) / 2
    if studants['ano'] == 1 and median >= 7 and studants['faltas'] <= 15:
        message = f'Total de {count_stud_aproved} alunos do 1 ano foram aprovados com sucesso.'
        count_stud_aproved += 1


print(f"\n{'=':=^70}")
print(message)
print(f"{'=':=^70}\n")

# RESPOSTA DO PRINT ABAIXO
# ======================================================================
# Total de 149 alunos do 1 ano foram aprovados com sucesso.
# ======================================================================