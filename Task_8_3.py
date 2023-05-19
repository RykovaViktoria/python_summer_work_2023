list = ['asdda','rtywew', 'dfagy']
def sort(x):
    return -len(set(x))
print(sorted(list, key=sort))