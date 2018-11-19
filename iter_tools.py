# The zip() function, takes any number of iterables as it's function and returns tuples of it's 
# iterable elements

arg1 = list(zip([1,2,3,4], ['a','b','c','d'], ['nyef', 24, 'bb', 'a'], [1,'q', 'op'], [1]))
print(arg1)

arg2 = list(zip([1,2,3,4], ['a','b','c','d'], ['nyef', 24, 'bb', 'a']))
print(arg2)
# NB returns the iterator with the next function hence the number of elements in the out put will always be equal the 
# next iterator meaning the last iterator

# The map function works by calling the iter function on it's second argument advancing it's iterator with next until
# the iterator is exhausted, and applying the function passed to its first argument to the value returned by next() 
# at each step
arg3 = list(map(len, ['cat', 'doggy', 'kaleodoscope']))
print(arg3)

"""
Since iterators are iterable, you can compose zip() and map() to produce an iterator over combinations of elements 
in more than one iterable. For example, the following sums corresponding elements of two lists:
"""
arg4 = list(map(sum,zip([1,3,5,7],[3,4,6,7])))
print(arg4)