def my_while_filter(iterable):
    return [iterable[i] for i in range(len(iterable)) if iterable[i] % 2 == 0]


def my_for_filter(strIter, suffix):
    return [strIter[i] for i in range(len(strIter)) if strIter[i].endswith(suffix)]


def my_comprehension(iterInts):
    return [iterInts[i]**2 for i in range(len(iterInts))]


def good_or_bad(string):
    if string in ['Coffee', 'Ice Cream']:
        return 'Good'
    elif string in ['Phone in Toilet', 'Sleeping through alarm']:
        return 'Bad'
    elif string == '6 Pieces of plain bread':
        return 'Okay?'
    elif string == 'Doe':
        return 'A dear, a female dear'
    else:
        return None


class ChestOfDrawers:
    def __init__(self, location, numDrawers):
        self._location = location
        self._numDrawers = numDrawers
        self._fullDrawers = 0

    def fill_drawer(self):
        if self._fullDrawers < self._numDrawers:
            self._fullDrawers += 1

    def empty_drawer(self):
        if self._fullDrawers > 0:
            self._fullDrawers -= 1

    def __repr__(self):
        # return f'{self._location} ({self._fullDrawers})'
        return '{0} ({1})'.format(self._location, self._fullDrawers)


class Rabbit:
    def asdf(self):
        print('floppy ears')
        print('dumb face')
        return


class Jackalope(Rabbit):
    def tell_us_about_yourself(self):
        super().asdf()
        print('and antlers')


def my_filter(dic):
    return {key: value * 3 for key, value in dic.items()}


def filter_s_words(iterable):
    return list(filter(lambda string: 's' in string, iterable))


class GetItSetIt:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newValue):
        self._value = newValue

    def forget(self):
        self.value = None


def comparison(func):
    def anotherFunc(arg1, arg2):
        val1, val2 = func(arg1), func(arg2)
        if val1 > val2:
            return 1
        elif val1 < val2:
            return -1
        else:
            return 0
    return anotherFunc
