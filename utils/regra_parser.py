import re
from typing import Dict, List

def processar_regra(regra: str) -> List[Dict[str, str]]:
    """Processa a string de regra e retorna a lista de atributos."""
    regra = regra.replace('\n', '').strip()
    condicoes = re.split(r'\s+(?:e|E)\s+', regra)
    atributos = []
    atributos_dict = {}

    for condicao in condicoes:
        condicao = condicao.strip()

        # Detecta sintaxe de IN / NOT IN com parênteses (ex: nome = (1, 2) ou nome != (1,2))
        match_in = re.search(r"(\w+)\s*(=|!=)\s*\(([^)]+)\)", condicao)
        if match_in:
            nome, operador, valores_str = match_in.groups()
            valores = [v.strip() for v in valores_str.split(',')]
            cond_op = 'in' if operador == '=' else 'not in'
            valores_formatados = ', '.join([f"'{v}'" for v in valores])
            atributos.append({
                "nome": nome,
                "condicao": f"{cond_op} [{valores_formatados}]"
            })
            continue

        # Detecta expressões com 'ou'
        if ' ou ' in condicao.lower():
            sub_condicoes = condicao.lower().split(' ou ')
            nomes = []
            operadores = []
            valores = []

            for sub in sub_condicoes:
                sub = sub.strip()
                for op in ['>=', '<=', '!=', '>', '<', '=']:
                    if op in sub:
                        nome, valor = sub.split(op, 1)
                        nomes.append(nome.strip())
                        operadores.append(op)
                        valores.append(valor.strip())
                        break

            if len(set(nomes)) > 1:
                raise ValueError(f"As condições 'ou' envolvem atributos diferentes: {', '.join(set(nomes))}")

            if len(set(operadores)) > 1:
                raise ValueError(f"Os operadores em uma condição 'ou' para o atributo '{nomes[0]}' são mistos: {', '.join(set(operadores))}")

            nome = nomes[0]
            operador = operadores[0]
            cond_op = 'in' if operador == '=' else 'not in'
            valores_formatados = ', '.join([f"'{v}'" for v in valores])
            atributos_dict[nome] = {
                "nome": nome,
                "condicao": f"{cond_op} [{valores_formatados}]"
            }
        else:
            nome, operador, valor = None, None, None
            operadores = ['>=', '<=', '!=', '>', '<', '=']
            for op in operadores:
                if op in condicao:
                    nome, valor = condicao.split(op, 1)
                    operador = op
                    break

            nome = nome.strip()
            valor = valor.strip() if valor else None

            if nome in atributos_dict:
                if isinstance(atributos_dict[nome]['condicao'], str):
                    atributos_dict[nome]['condicao'] = [atributos_dict[nome]['condicao'].split()[-1]]
                atributos_dict[nome]['condicao'].append(valor)
            else:
                # Correção: Substituir '=' por '=='
                operador_corrigido = '==' if operador == '=' else operador
                atributos_dict[nome] = {
                    "nome": nome,
                    "condicao": f"{operador_corrigido} {valor}" if valor else "exists"
                }

    # Pós-processamento: converte listas acumuladas em in/not in
    for nome, attr in atributos_dict.items():
        if isinstance(attr['condicao'], list):
            op = '=' if '=' in attr['condicao'][0] else '!='
            valores_formatados = ', '.join([f"'{v}'" for v in attr['condicao']])
            attr['condicao'] = f"{'in' if op == '=' else 'not in'} [{valores_formatados}]"
        atributos.append(attr)

    return atributos