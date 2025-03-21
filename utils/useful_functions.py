from itertools import product

def generate_combinations(tupla):
    # Genera todas las combinaciones posibles dentro del rango de cada índice
    combinations = product(*(range(0, x + 1) for x in tupla))

    # Filtra las combinaciones eliminando las que sean puramente (0, 0, 0, ...)
    return [c for c in combinations if any(c)]  # `any(c)` verifica que haya al menos un número distinto de 0

def subtract_dict(tupla, dict_list):

    new_dict_list = []

    for i,s in zip(tupla, dict_list):
        new_dict_list.append({
            "num_agents": s['num_agents'] - i,  # Es entero
            "op1": s['op1'],
            "op2": s['op2'],
            "rigidity": s['rigidity'],
        })

    return new_dict_list