import json

path = 'candidates.json'


def load_candidates_from_json(path):
    """ Загружает из файла"""
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json(path)
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json(path)
    for candidate in candidates:
        if candidate['name'].lower() == candidate_name.lower():
            return candidate


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json(path)
    candidate_list = [candidate for candidate in candidates if skill_name.lower() in candidate['skills'].lower()]
    return candidate_list

