def list_change(str):
    integer=[]
    error_log=[]

    for s in str:
        try:
            integer.append(int(s))
        except ValueError:
            error_log.append("error in converting string to integer")
    return integer , error_log

input_list = ["1" , "ab" , "45"]
integers, errors = list_change(input_list)

print(integers) 
print(errors)
