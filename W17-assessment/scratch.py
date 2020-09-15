if({} == True):
    print(True)
elif {} == False:
    print(False)
else:
    print("what?")

def func(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

func(True, False, 1, 2, c=3)

if '':
    print('true')
elif not '':
    print('false')
else:
    print('nada')
