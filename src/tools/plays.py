import re


def fill_personnel(personnel, all_positions):
    positions = extract_positions(personnel)
    numbers = extract_numbers(personnel)
    out = []
    for z in zip(positions, numbers):
        out.append(' '.join(map(str, z)))
    diff = all_positions - set(positions)
    for d in diff:
        out.append(str(d) + ' 0')
    return ', '.join(sorted(out))


def extract_positions(personnel):
    m = re.findall(r'[A-Z]{2}', "".join(personnel))
    return m


def extract_numbers(personnel):
    m = re.findall(r'[0-9]+', "".join(personnel))
    return m
