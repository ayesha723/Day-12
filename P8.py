def exp_table(base , expo_range):
    table=[]
    for exp in range( 1 , expo_range +1):
        result = base ** exp
        table.append(f"{base}^{exp} = {result}")
    return table
base_num = 2
exp_range = 5  # Exponents from 1 to 5
result = exp_table(base_num, exp_range)
for line in result:
    print(line)

