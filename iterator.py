'''http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/'''

"""Implementation of the iterator pattern with a generator"""
def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    # The zip keeps from counting over the limit
    for number, pos in zip(numbers, list(range(count))):
        yield number

# Test the generator
count_to_two = lambda : count_to(2)
count_to_five = lambda : count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number, end=' ')

print()

print('Counting to five...')
for number in count_to_five():
    print(number, end=' ')

print()
