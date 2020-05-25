from collections import Counter

texto1 = """  Ministério da Saúde divulgou nesta segunda-feira (25) o mais recente balanço de casos e mortes causadas pelo novo coronavírus. Os principais dados são:
23.473 mortes, eram 22.666 no domingo (24)
Foram 807 registros de morte incluídos no balanço em 24 horas
374.898 casos confirmados
Foram 11.687 novos casos incluídos no balanço em 24 horas
153.833 pacientes recuperados (41%)
São Paulo, Rio de Janeiro e Ceará são os três estados que mais registraram casos e mortes pela infecção causada pelo novo coronavírus Sars-Cov-2 no Brasil. Apenas os três estados são responsáveis por mais da metade (54%) das mortes por complicações da Covid-19 no país.

SP: 83.625 casos, 6.220 mortes
RJ: 39.298 casos, 4,105 mortes
CE: 36.185 casos, 2.493 mortes
Segundo o balanço desta segunda, dos mais de 23 mil óbitos, 270 aconteceram nos últimos 3 dias e ao menos 3.742 ainda estão em investigação.
"""

texto2 = """A secretária de Gestão do Trabalho e da Educação na Saúde, Mayra Pinheiro, disse que o estudo que serviu de base para a decisão da Organização Mundial da Saúde (OMS) de suspender testes com hidroxicloroquina para tratamento da Covid-19, publicado na revista "The Lancet", não tem uma metodologia "aceitável para servir de referência".

Após prever painel com taxa de UTIs ocupadas, governo diz só ter dados de menos da metade dos hospitais que atuam contra a Covid-19
Pesquisadores tiram do ar estudo que recomendava hidroxicloroquina contra Covid-19
"O estudo [da Lancet] não é um ensaio clínico, é apenas um banco de dados coletado de vários países. não entra em um estudo metodologicamente aceitável para servir de referência para outros países muito menos para o Brasil", disse Pinheiro.

A secretária disse que a pasta acompanha 216 protocolos de uso da cloroquina no tratamento da doença em países como Estados Unidos, Turquia e Índia. Segundo ela, os técnicos do Ministério da Saúde estão "tranquilos e serenos" quanto à orientação que dá autonomia para os médicos oferecerem esse tratamento a pacientes "que assim desejarem".

Suspensão de testes
Nesta segunda, a OMS pediu a suspensão de testes com o uso da hidroxicloroquina no tratamento da infecção pelo novo coronavírus após a constatação no aumento no risco de mortes.


A suspensão temporária foi tomada até que a segurança da droga seja reavaliada, já que estudos recentes mostraram que ela não é eficaz contra a Covid-19 e pode aumentar a taxa de mortalidade.

O diretor-geral da entidade, Tedros Adhanom Ghebreyesus, afirmou que a suspensão foi determinada depois da divulgação dos resultados do estudo publicado na sexta-feira (22) na revista "The Lancet".

96 mil pessoas
A pesquisa publicada na revista científica, feita com 96 mil pessoas, apontou que não houve eficácia das substâncias contra a Covid-19 e detectou risco de arritmia cardíaca nos pacientes que as utilizaram.

Dados do estudo:

96.032 pacientes internados foram observados;
Idade média de 53,8 anos com 46,3% de mulheres;
Pacientes são de 671 hospitais em 6 continentes;
14.888 pacientes receberam 4 tipos de tratamentos diferentes com a cloroquina e a hidroxicloroquina;
As hospitalizações ocorreram entre 20 de dezembro de 2019 e 14 de abril de 2020."""

def analisa_frequencia(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, freq/total_caracteres) for letra, freq in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comum = proporcoes.most_common(10)
    for carac, proporcao in mais_comum:
        print("{} --> {:.2f}%".format(carac, proporcao*100))

print(analisa_frequencia(texto1))
print(analisa_frequencia(texto2))
    

