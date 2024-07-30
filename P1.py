def with_fallback(s, default):
    try:
        return int(s)
    except ValueError:
        return default


input_str = "123"
fallback_value = 0
result = with_fallback(input_str, fallback_value)
print(result)  

input_str = "abc"
result = with_fallback(input_str, fallback_value)
print(result)  
