#
#
# 6) As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?. Crie um gráfico para mostrar isso
#
#
import matplotlib.pyplot as plt
from functions import ReadFile

data_students = ReadFile.load_csv()
data = data_students[0]

_1_year = 0
_2_year = 0
_3_year = 0
for studants in data:

    median = (studants['nota_semestre_1'] + studants['nota_semestre_2']) / 2
    if (median < 7 and studants['nota_exame'] < 5) or (studants['faltas'] > 15):
        if studants['ano'] == 1:
            _1_year += 1
        elif studants['ano'] == 2:
            _2_year += 1
        elif studants['ano'] == 3:
            _3_year += 1


labels = '1 Ano', '2 Ano', '3 Ano'
sizes = [_1_year, _2_year, _3_year]

if _1_year > _2_year and _1_year > _3_year:
    explode = [0.1,0,0]

elif _2_year > _1_year and _2_year > _3_year:
    explode = [0,0.1,0]

elif _3_year > _1_year and _3_year > _2_year:
    explode = [0,0,0.1]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',explode=explode,
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.title(f'As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?', fontsize=12)
plt.show()