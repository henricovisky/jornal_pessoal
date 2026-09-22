# Jornal Pessoal (Henricovisky)

Este é um projeto de jornal pessoal estático projetado para ser alimentado 100% por Agentes de IA Autônomos (como o Hermes Agent). O site exibe notícias e resumos agendados hospedados via GitHub Pages.

## Como funciona a Arquitetura?

1. **Estrutura Estática:** O front-end carrega os artigos de um arquivo `historico.json` padrão.
2. **Script de Postagem Automática:** O repositório inclui um arquivo utilitário `add_post.py`. Ele registra as matérias no histórico, faz o commit com mensagem automática e envia (`git push`) para a branch principal, desencadeando o deploy via GH Pages.

## Como automatizar a IA (Guia de Reprodução)

Se você tem um agente como o Hermes (capaz de executar rotinas cronjobs invisíveis e usar ferramentas interativas de CLI), basta apontar um job diário informando como rodar o script.

### Padrão de System Prompt (O "Segredo")

Ao descrever as regras do agente, defina sua rotina editorial de busca e *exija* no fim do prompt que ele utilize o formato de quebra em linha única para o shell, desta forma exata:

```text
1. Formate sua notícia apenas com HTML estrutural nativo (<h3>, <p>, <ul>).
2. IMPORTANTE: Antes de dar a sua resposta final, você DEVE enviar o conteúdo para o site usando a ferramenta de terminal (CLI).

Execute o seguinte comando:

python3 /caminho/absoluto/jornal_pessoal/add_post.py "O Título Adequado Para a Edição" "<seu conteudo html todo em linha única sem quebras de linha reais para não quebrar o bash>"
```

### Configurações no Agente
- **Ferramentas (`toolsets`)**: Habilite, além das ferramentas de navegação web (para ler notícias), ferramentas de `terminal`.
- **Prevenções / Segurança**: O agente irá invocar um `git push` silenciosamente. A máquina onde ele trafega precisa ter autenticação SSH do git configurada com o Github.
- **Entrega / Delivery**: Configure a saída do cron para ser `local` caso você queira que ele atualize e trabalhe em plano de fundo de madrugada, sem spam no chat principal.

## Estrutura Base
- `add_post.py`
- `historico.json`
- `index.html` (com lógica de parse JSON do JS embarcada).