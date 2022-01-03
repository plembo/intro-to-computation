def print_name(first_name, last_name, reverse=False):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)


print_name('John', 'Doe', False)
print_name('John', 'Doe', reverse=False)
print_name('John', 'Doe')
print_name('John', 'Doe', True)
print_name('John', 'Doe', reverse=True)
