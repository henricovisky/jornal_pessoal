from hermes_tools import cronjob

p1 = """Crie um relatório diário sobre o mundo open-source com foco em casos de uso aplicáveis a negócios ou que facilitem a vida das pessoas. O relatório deve incluir notícias atualizadas e confiáveis de fontes como GitHub Trending, Hacker News e Linux Foundation. Formate o conteúdo como Markdown. Inclua tanto tópicos do dia quanto tendências recentes (últimos 7 dias).

IMPORTANTE: Antes de dar a sua resposta final, você DEVE enviar o conteúdo gerado para o jornal pessoal do usuário.
Para isso, formate sua postagem usando tags HTML (ex: <p>, <h3>, <ul>, <li>, <strong>) sem quebras de linha soltas (use uma string de linha única/escapada) e use a ferramenta 'terminal' para executar:
python3 /home/ubuntu/jornal_pessoal/add_post.py "Relatório Diário Open Source" "<seu conteudo html>" """

r1 = cronjob(
    action="update",
    job_id="867b22d394a7",
    prompt=p1,
    enabled_toolsets=["terminal", "web"]
)


p2 = """Você é o responsável pelo job diário “48 Leis do Poder - Corporativo Diario”.

Use o arquivo de estado como única fonte da verdade:
`~/.hermes/48laws_state.json`

Instruções:
1. Leia o arquivo de estado apontado.
2. Calcule a próxima lei: `(last_law % 48) + 1`.
3. Entregue em português a lei com número, título, explicação breve e 1-2 aplicações práticas para negócios ou vida corporativa.
4. Atualize o arquivo de estado em modo atômico.
5. Se o arquivo não existir, trate last_law = 2.
6. Não repita uma lei.
7. IMPORTANTE: Antes de dar sua resposta final, VOCÊ DEVE pegar o texto que gerou, converter para tags HTML (ex: <p>, <strong>, <ul>) em uma linha só e utilizar a ferramenta 'terminal' para incluir a publicação no Jornal Pessoal rodando:
python3 /home/ubuntu/jornal_pessoal/add_post.py "Lei X: Titulo" "<html aqui>"

Responda (na sua saída final para ser entregue) apenas com o conteúdo da lei em Markdown puro."""

r2 = cronjob(
    action="update",
    job_id="3f5a477eb164",
    prompt=p2,
    enabled_toolsets=["terminal", "read_file", "write_file"]
)


p3 = """Busque as notícias de hoje focadas no Brasil nas fontes: 'Brasil de Fato' e 'Rede Brasil Atual'.

Papel e Objetivo:
Você é um jornalista analítico e editor da seção "Brasil" do jornal "Henricovisky".

Instruções:
1. Selecione os 3 a 5 eventos.
2. Formate um HTML puro (use <h3>, <p>, <ul>).

IMPORTANTE: Antes de dar a sua resposta final, você DEVE enviar o conteúdo para o jornal usando a tool terminal.
Execute:
python3 /home/ubuntu/jornal_pessoal/add_post.py "Resumo do Brasil" "<seu conteudo html em linha única sem quebras de linha reais para não quebrar o bash>" """

r3 = cronjob(
    action="update",
    job_id="7bf9750f70b2",
    prompt=p3,
    enabled_toolsets=["web", "terminal"]
)


p4 = """Busque as notícias de hoje focadas no MUNDO nas fontes: 'BBC News Brasil' e 'DW Brasil'.

Papel e Objetivo:
Você é um jornalista analítico e editor da seção "Mundo" do jornal "Henricovisky".

Instruções:
1. Selecione os 3 a 5 eventos globais.
2. Formate um HTML puro (use <h3>, <p>, <ul>).

IMPORTANTE: Antes de dar a sua resposta final, você DEVE enviar o conteúdo para o jornal usando a tool terminal.
Execute:
python3 /home/ubuntu/jornal_pessoal/add_post.py "Resumo Mundial" "<seu conteudo html em linha única sem quebras de linha reais para não quebrar o bash>" """

r4 = cronjob(
    action="update",
    job_id="5e58ccc2ece0",
    prompt=p4,
    enabled_toolsets=["web", "terminal"]
)

print("Jobs updated:", r1, r2, r3, r4)
