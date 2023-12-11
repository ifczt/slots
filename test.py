import tomllib

data = {
    1: {3: 1, 4: 2, 5: 3},
    2: {3: 1, 4: 2, 5: 3},
}
# toml
t_str = """
[[spark]]
mode = 'COUNT_SYMBOL'
symbol = 1
min = 3
max = 5
[spark.freespin]
mode = 'LIGATURE'
build_nums = 10
"""
print(tomllib.loads(t_str))