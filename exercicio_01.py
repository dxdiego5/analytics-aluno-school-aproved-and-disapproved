#
#
# 1) Quantos alunos estudam em cada escola, e qual a escola com mais alunos?
#
#
from functions import ReadFile

data_students = ReadFile.load_csv()
data = data_students[0]
list_school = data_students[1]

for studant in data:
    list_school[studant['escola']] += 1


count_stundant = -1
print(f"{'=':=^70}")
for s, v in zip(list_school.keys(), list_school.values()):
    print(f'Total de {v} alunos estudão na escola {s}.')

    if count_stundant < v:
        count_stundant = v
        name_school = f'\nA escola que possui mais alunos é {s} com um total de {v} alunos.'

print(name_school)
print(f"{'=':=^70}\n")

# RESPOSTA DO PRINT ABAIXO
# ======================================================================
# Total de 798 alunos estudão na escola Pedro II.
# Total de 876 alunos estudão na escola Francisto Chagas.
# Total de 830 alunos estudão na escola Gabriel Gomes.
# Total de 816 alunos estudão na escola Antonio Prado.
# Total de 835 alunos estudão na escola Pedro I.
# Total de 845 alunos estudão na escola Carlos Santos.

# A escola que possui mais alunos é Francisto Chagas com um total de 876 alunos.
# ======================================================================
