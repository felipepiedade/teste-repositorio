#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Carregador de Templates de Prompts
==================================

Utilitário para carregar e utilizar os templates do arquivo JSON.
"""

import json
import os
import random


class TemplateLoader:
    """Classe para carregar e utilizar templates de prompts."""
    
    def __init__(self, templates_file='prompt_templates.json'):
        """Inicializa o carregador de templates.
        
        Args:
            templates_file (str): Caminho para o arquivo de templates.
        """
        self.templates_file = templates_file
        self.templates = self._load_templates()
        
    def _load_templates(self):
        """Carrega os templates do arquivo JSON.
        
        Returns:
            dict: Conteúdo do arquivo de templates.
        """
        try:
            with open(self.templates_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Arquivo {self.templates_file} não encontrado.")
            return {"templates": [], "dicas_otimização": []}
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo {self.templates_file}.")
            return {"templates": [], "dicas_otimização": []}
    
    def listar_templates(self):
        """Lista todos os templates disponíveis.
        
        Returns:
            list: Lista com nomes e categorias dos templates.
        """
        return [(t['nome'], t['categoria']) for t in self.templates.get('templates', [])]
    
    def obter_template(self, nome_ou_indice):
        """Obtém um template específico pelo nome ou índice.
        
        Args:
            nome_ou_indice (str or int): Nome ou índice do template.
            
        Returns:
            dict: Template solicitado ou None se não encontrado.
        """
        templates = self.templates.get('templates', [])
        
        # Se o parâmetro for um índice
        if isinstance(nome_ou_indice, int):
            if 0 <= nome_ou_indice < len(templates):
                return templates[nome_ou_indice]
            return None
        
        # Se o parâmetro for um nome
        for template in templates:
            if template['nome'].lower() == nome_ou_indice.lower():
                return template
        
        return None
    
    def obter_template_por_categoria(self, categoria):
        """Obtém todos os templates de uma categoria específica.
        
        Args:
            categoria (str): Categoria desejada.
            
        Returns:
            list: Lista de templates da categoria.
        """
        return [t for t in self.templates.get('templates', []) 
                if t['categoria'].lower() == categoria.lower()]
    
    def obter_dica_aleatória(self):
        """Retorna uma dica de otimização aleatória.
        
        Returns:
            str: Dica de otimização.
        """
        dicas = self.templates.get('dicas_otimização', [])
        if dicas:
            return random.choice(dicas)
        return "Não há dicas disponíveis."
    
    def preencher_template(self, template, valores):
        """Preenche um template com os valores fornecidos.
        
        Args:
            template (dict): Template a ser preenchido.
            valores (dict): Valores para preencher o template.
            
        Returns:
            str: Template preenchido.
        """
        if not template or 'template' not in template:
            return "Template inválido."
        
        prompt_template = template['template']
        
        # Verificar valores faltantes
        placeholders = self._extrair_placeholders(prompt_template)
        valores_faltantes = [p for p in placeholders if p not in valores]
        
        if valores_faltantes:
            missing = ", ".join(valores_faltantes)
            return f"Valores faltantes: {missing}"
        
        # Preencher o template
        prompt_preenchido = prompt_template
        for chave, valor in valores.items():
            placeholder = "{" + chave + "}"
            if placeholder in prompt_preenchido:
                prompt_preenchido = prompt_preenchido.replace(placeholder, valor)
        
        return prompt_preenchido
    
    def _extrair_placeholders(self, texto):
        """Extrai placeholders de um texto.
        
        Args:
            texto (str): Texto contendo placeholders.
            
        Returns:
            list: Lista de placeholders encontrados.
        """
        import re
        placeholders = re.findall(r'\{([^}]+)\}', texto)
        return placeholders


def exemplo_uso():
    """Exemplo de uso do carregador de templates."""
    loader = TemplateLoader()
    
    # Listar todos os templates
    print("Templates disponíveis:")
    for i, (nome, categoria) in enumerate(loader.listar_templates()):
        print(f"{i}: {nome} ({categoria})")
    print()
    
    # Obter um template específico
    template = loader.obter_template(0)  # Primeiro template
    if template:
        print(f"Template selecionado: {template['nome']}")
        print("Exemplo de valores:")
        for chave, valor in template['exemplo_preenchido'].items():
            print(f"  {chave}: {valor}")
        print()
        
        # Preencher o template com valores de exemplo
        prompt = loader.preencher_template(template, template['exemplo_preenchido'])
        print("Prompt gerado:")
        print("="*50)
        print(prompt)
        print("="*50)
    
    # Obter uma dica aleatória
    print("\nDica de otimização:")
    print(loader.obter_dica_aleatória())


if __name__ == "__main__":
    exemplo_uso()
