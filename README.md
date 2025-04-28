# Otimizador e Gerador de Prompts

Uma ferramenta poderosa para criar, estruturar e otimizar prompts para interações com modelos de IA.

## Funcionalidades

- **Geração de prompts** baseados em templates por categoria
- **Otimização de prompts existentes** para maior eficácia
- **Estruturação automática** com diferentes níveis de complexidade
- **Sugestão de personas** para prompts com maior impacto
- **Salvamento de prompts** em formato JSON para referência futura

## Como Usar

### Instalação

Não requer instalação especial além do Python 3.6+. Baixe o arquivo `prompt_optimizer.py` e você estará pronto para começar.

```bash
python prompt_optimizer.py
```

### Exemplos Básicos

#### 1. Gerar um prompt técnico

```python
from prompt_optimizer import PromptOptimizer

otimizador = PromptOptimizer()

prompt = otimizador.gerar_prompt_básico(
    "técnico", 
    área="inteligência artificial", 
    contexto="Estou criando um tutorial introdutório.",
    conceito="como funcionam os transformers em processamento de linguagem natural",
    nível_detalhe="analogias simples e exemplos visuais"
)

print(prompt)
```

#### 2. Otimizar um prompt existente

```python
from prompt_optimizer import PromptOptimizer

otimizador = PromptOptimizer()

prompt_original = "Me dê ideias para um aplicativo mobile."
prompt_otimizado = otimizador.otimizar_prompt(prompt_original)

print(prompt_otimizado)
```

#### 3. Criar um prompt estruturado avançado

```python
from prompt_optimizer import PromptOptimizer

otimizador = PromptOptimizer()

prompt = otimizador.gerar_prompt_estruturado(
    nível="avançado",
    instrução="Crie um plano de aprendizado para dominar ciência de dados",
    contexto="Tenho conhecimentos básicos de programação",
    objetivo="Conseguir um emprego júnior na área em 6 meses",
    formato="Plano semanal com recursos específicos",
    restrições="Apenas recursos gratuitos",
    exemplos="Semana 1: Revisão de Python focada em análise de dados"
)

print(prompt)
```

## Tipos de Prompts Disponíveis

1. **Criativo** - Para gerar conteúdo criativo, histórias, etc.
2. **Técnico** - Para explicações técnicas e tutoriais
3. **Análise** - Para análise crítica de conteúdo ou conceitos
4. **Instrução** - Para obter instruções detalhadas sobre uma tarefa
5. **Pesquisa** - Para investigação de tópicos específicos

## Níveis de Estruturação

1. **Básico** - Instrução simples e direta
2. **Detalhado** - Inclui contexto, objetivo e formato desejado
3. **Avançado** - Estrutura completa com restrições e exemplos

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias para melhorar esta ferramenta, fique à vontade para criar um pull request ou abrir uma issue.

## Licença

Este projeto está licenciado sob a licença MIT.
