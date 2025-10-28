def merge_dicts(d1, d2):
    result = d1.copy()  # start with d1

    for key, value in d2.items():
        if key in result:
            # Rule 1: Numbers → add
            if isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
                result[key] += value

            # Rule 2: Strings → concatenate
            elif isinstance(result[key], str) and isinstance(value, str):
                result[key] += value

            # Rule 3: Lists/Sets → merge
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key].extend(value)
            elif isinstance(result[key], set) and isinstance(value, set):
                result[key] = result[key].union(value)

            # Rule 4: Tuples → list of tuples
            elif isinstance(result[key], tuple) and isinstance(value, tuple):
                result[key] = [result[key], value]

            # Rule 5: Dictionaries → merge recursively
            elif isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)

            else:
                # if types mismatch, keep as tuple
                result[key] = (result[key], value)
        else:
            result[key] = value

    return result


# Example
d1 = {'a': 20, 'b': 30}
d2 = {'b': 40, 'c': 50}
print(merge_dicts(d1, d2))  # {'a': 20, 'b': 70, 'c': 50}
