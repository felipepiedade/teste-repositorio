#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador e Otimizador de Prompts
===============================

Uma ferramenta para criar e otimizar prompts para interações com modelos de IA.
Ajuda a estruturar prompts eficazes para diferentes finalidades e casos de uso.
"""

import json
import random
import re
from typing import Dict, List, Optional, Union


class PromptOptimizer:
    """Classe principal para otimização e geração de prompts."""
    
    def __init__(self):
        self.templates = {
            "criativo": "Atue como {persona}. {contexto} Crie {output_type} sobre {tema} com {estilo}.",
            "técnico": "Você é um especialista em {área}. {contexto} Explique {conceito} com {nível_detalhe}.",
            "análise": "Como {persona}, analise {objeto_análise}. {contexto} Forneça {tipo_análise} considerando {aspectos}.",
            "instrução": "Atue como {persona}. {contexto} Forneça instruções detalhadas sobre como {tarefa}, considerando {considerações}.",
            "pesquisa": "Como pesquisador em {área}, {contexto} Investigue {tópico} e forneça {tipo_resultado} focando em {aspectos}."
        }
        
        self.persona_options = [
            "um professor universitário", "um especialista renomado", "um consultor experiente",
            "um pesquisador premiado", "um mentor dedicado", "um analista crítico",
            "um criativo inspirado", "um estrategista inovador", "um comunicador habilidoso"
        ]
        
        self.estrutura_prompt = {
            "básico": "{instrução}",
            "detalhado": "{instrução}\n\nContexto: {contexto}\nObjetivo: {objetivo}\nFormato desejado: {formato}",
            "avançado": "# TAREFA\n{instrução}\n\n# CONTEXTO\n{contexto}\n\n# OBJETIVO\n{objetivo}\n\n# FORMATO\n{formato}\n\n# RESTRIÇÕES\n{restrições}\n\n# EXEMPLOS\n{exemplos}"
        }

    def gerar_prompt_básico(self, tipo: str, **kwargs) -> str:
        """Gera um prompt básico baseado no tipo selecionado."""
        if tipo not in self.templates:
            tipos_disponíveis = ", ".join(self.templates.keys())
            return f"Tipo inválido. Tipos disponíveis: {tipos_disponíveis}"
        
        template = self.templates[tipo]
        try:
            return template.format(**kwargs)
        except KeyError as e:
            parâmetros_faltantes = re.findall(r'\{([^}]+)\}', template)
            return f"Parâmetros faltantes: {', '.join(parâmetros_faltantes)}"

    def sugerir_persona(self) -> str:
        """Sugere uma persona aleatória para o prompt."""
        return random.choice(self.persona_options)
    
    def otimizar_prompt(self, prompt_original: str) -> str:
        """Otimiza um prompt existente adicionando elementos de estruturação."""
        # Verificar tamanho do prompt
        palavras = len(prompt_original.split())
        
        # Prompts muito curtos
        if palavras < 10:
            return self._expandir_prompt(prompt_original)
        # Prompts médios
        elif palavras < 30:
            return self._estruturar_prompt(prompt_original)
        # Prompts longos
        else:
            return self._refinar_prompt(prompt_original)
    
    def _expandir_prompt(self, prompt: str) -> str:
        """Expande prompts curtos adicionando contexto e especificidade."""
        expansão = (
            f"{prompt}\n\n"
            f"Por favor, forneça uma resposta detalhada e estruturada. "
            f"Inclua exemplos relevantes e passos concretos quando aplicável. "
            f"Considere diferentes perspectivas e contextos."
        )
        return expansão
    
    def _estruturar_prompt(self, prompt: str) -> str:
        """Adiciona estrutura a prompts de tamanho médio."""
        estruturado = (
            f"# INSTRUÇÃO\n{prompt}\n\n"
            f"# FORMATO DESEJADO\n"
            f"- Comece com uma introdução concisa\n"
            f"- Organize a informação em seções claras\n"
            f"- Utilize bullets para pontos importantes\n"
            f"- Conclua com um resumo aplicável\n"
            f"- Use linguagem precisa e exemplos quando necessário"
        )
        return estruturado
    
    def _refinar_prompt(self, prompt: str) -> str:
        """Refina prompts longos para maior clareza e foco."""
        linhas = prompt.split('\n')
        
        # Identificar principais elementos
        instrução = linhas[0] if linhas else prompt
        contexto = "Entendendo o contexto completo fornecido"
        
        refinado = (
            f"# OBJETIVO PRINCIPAL\n{instrução}\n\n"
            f"# CONTEXTO\n{contexto}\n\n"
            f"# PARÂMETROS DE QUALIDADE\n"
            f"1. Precisão: Forneça informações corretas e verificáveis\n"
            f"2. Relevância: Mantenha o foco no objetivo principal\n"
            f"3. Estrutura: Organize a resposta de forma lógica\n"
            f"4. Profundidade: Equilibre detalhes suficientes sem prolixidade\n"
            f"5. Clareza: Use linguagem simples e direta\n\n"
            f"# PROMPT ORIGINAL\n{prompt}"
        )
        return refinado

    def gerar_prompt_estruturado(
            self, 
            nível: str = "básico", 
            instrução: str = "", 
            contexto: str = "", 
            objetivo: str = "",
            formato: str = "", 
            restrições: str = "", 
            exemplos: str = ""
        ) -> str:
        """Gera um prompt com a estrutura escolhida."""
        if nível not in self.estrutura_prompt:
            níveis_disponíveis = ", ".join(self.estrutura_prompt.keys())
            return f"Nível inválido. Níveis disponíveis: {níveis_disponíveis}"
        
        template = self.estrutura_prompt[nível]
        
        # Preencher valores padrão para campos vazios
        if not contexto and nível != "básico":
            contexto = "Considere o contexto atual e as melhores práticas."
        if not objetivo and nível != "básico":
            objetivo = "Fornecer informação clara, precisa e útil."
        if not formato and nível != "básico":
            formato = "Texto estruturado com parágrafos lógicos e pontos principais destacados."
        if not restrições and nível == "avançado":
            restrições = "Mantenha a resposta concisa e focada no objetivo."
        if not exemplos and nível == "avançado":
            exemplos = "Exemplo 1: [Breve exemplo relacionado]"
            
        # Formatar o prompt conforme o template
        prompt_formatado = template.format(
            instrução=instrução,
            contexto=contexto,
            objetivo=objetivo,
            formato=formato,
            restrições=restrições,
            exemplos=exemplos
        )
        
        return prompt_formatado
    
    def salvar_prompt(self, prompt: str, nome_arquivo: str) -> None:
        """Salva o prompt em um arquivo JSON."""
        dados = {
            "prompt": prompt,
            "metadata": {
                "versão": "1.0",
                "timestamp": "gerado automaticamente",
                "tipo": "prompt otimizado"
            }
        }
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
            
        print(f"Prompt salvo com sucesso em {nome_arquivo}")


def exemplo_uso():
    """Demonstração de uso da classe PromptOptimizer."""
    otimizador = PromptOptimizer()
    
    # Exemplo 1: Gerar prompt básico
    prompt1 = otimizador.gerar_prompt_básico(
        "técnico", 
        área="inteligência artificial", 
        contexto="Estou criando um tutorial introdutório.",
        conceito="como funcionam os transformers em processamento de linguagem natural",
        nível_detalhe="analogias simples e exemplos visuais"
    )
    print("Exemplo 1 - Prompt Técnico:\n", prompt1, "\n")
    
    # Exemplo 2: Otimizar um prompt existente
    prompt_original = "Me dê ideias para um aplicativo mobile."
    prompt2 = otimizador.otimizar_prompt(prompt_original)
    print("Exemplo 2 - Prompt Otimizado:\n", prompt2, "\n")
    
    # Exemplo 3: Prompt estruturado avançado
    prompt3 = otimizador.gerar_prompt_estruturado(
        nível="avançado",
        instrução="Crie um plano de aprendizado para dominar ciência de dados em 6 meses",
        contexto="Sou um profissional de TI com conhecimentos básicos de programação em Python e estatística",
        objetivo="Desenvolver habilidades suficientes para conseguir um emprego júnior na área",
        formato="Plano semanal detalhado com recursos de aprendizado específicos",
        restrições="Foco em ferramentas open-source e recursos gratuitos quando possível",
        exemplos="Semana 1: Revisão de Python com foco em pandas e numpy, exercícios incluindo..."
    )
    print("Exemplo 3 - Prompt Estruturado Avançado:\n", prompt3)


if __name__ == "__main__":
    exemplo_uso()
