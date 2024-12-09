
# module_3_3

# "Распаковка позиционных параметров" с выводом номера вызова ф-и

calls = 0
def count_calls():
    global calls
    calls += 1

def print_params(a = 1,  b = 'строка', c = True):
    count_calls()
    print(f'{calls} -', a,b,c)

print_params()
print_params(45, 90, 180)
print_params(45, 90)
print_params(45)
print_params(45, b = 666, c = 180)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1,'два', True]
values_dict = {'a' : 1.25,  'b' : 'строка', 'c' :None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.43, 'FIFA']
print_params(*values_list_2)