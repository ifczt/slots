import tomllib

data = {
    1: {3: 1, 4: 2, 5: 3},
    2: {3: 1, 4: 2, 5: 3},
}
# toml
t_str = """
[[odds]]
symbol = 1
3 = 1
4 = 1
5 = 1
[[odds]]
symbol = 2
3 = 1
4 = 1
5 = 1
[[winning_rule]]
coords = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
[[winning_rule]]
coords = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]

"""
print(tomllib.loads(t_str))
