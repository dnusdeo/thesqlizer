f = lambda x: "'"+x+"'"

def format_list(list):
    if ',' in list:
        return map(f, list.split(","))
    else:
        return map(f, list.split())

user_list = input("Gimme yo goodies: \n")

f_list = format_list(user_list)

print(*f_list, sep=", ")