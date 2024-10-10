data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum (*args, **kwargs):
    s = 0
    for i in args:
        if isinstance(i,(tuple,list, set)):
            s += calculate_structure_sum (*i)
        elif isinstance(i, dict):
            s += calculate_structure_sum (*i.items())
        elif isinstance(i, str):
            s += len(i)
        elif isinstance(i, (int, float)):
            s += i
        elif i is None:
            pass
    return s
result = calculate_structure_sum(data_structure)
print(result)

