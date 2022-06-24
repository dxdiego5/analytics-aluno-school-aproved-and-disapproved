#
#
# 5) Qual a média de todas as notas (do 1º e 2º semestre) dos alunos do 2º ano?
#
#
from functions import ReadFile

data_students = ReadFile.load_csv()
data = data_students[0]

msg = ''
for studants in data:
    if studants['ano'] == 2:
        median = (studants['nota_semestre_1'] + studants['nota_semestre_2']) / 2

        if median >= 7 and studants['faltas'] <= 15:
            msg+= f'--- {studants["nome"]}, MEIDA: {median:.2f}.\n'

        elif median < 7:
            msg+= f'--- {studants["nome"]}, MEDIA: {median:.2f}, e no EXAME: {studants["nota_exame"]}.\n'
    
print(msg)

# RESPOSTA DO PRINT ABAIXO: so alguns para exemlo.....
# --- Bernardo Alves, MEDIA: 6.05, e no EXAME: 5.82.
# --- Theo Soares, MEDIA: 4.51, e no EXAME: 2.0.
# --- Bernardo Santos, MEDIA: 3.35, e no EXAME: 1.37.
# --- Gabriel Silva, MEDIA: 3.50, e no EXAME: 5.08.
# --- Maria Rodrigues, MEDIA: 4.94, e no EXAME: 1.98.
# --- Valentina Gomes, MEDIA: 5.32, e no EXAME: 8.02.
# --- Helena Alves, MEDIA: 4.30, e no EXAME: 9.33.
# --- Valentina Ribeiro, MEDIA: 6.46, e no EXAME: 2.39.
# --- Bernardo Silva, MEDIA: 5.04, e no EXAME: 2.75.
# --- Heitor Alves, MEIDA: 9.58.
# --- Maria Martins, MEDIA: 6.18, e no EXAME: 9.08.
# --- Sophia Pereira, MEDIA: 4.67, e no EXAME: 3.38.
# --- Maria Ferreira, MEDIA: 1.48, e no EXAME: 7.22.
# --- Laura Silva, MEDIA: 4.42, e no EXAME: 6.52.
# ............ tem muito mais.