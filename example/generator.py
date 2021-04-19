# def mygenerator():
#     print('First item')
#     yield 10

#     print('Second item')
#     yield 20

#     print('Last item')
#     yield 30


# gen=mygenerator()
# next(gen)
# next(gen)
# next(gen)
# next(gen)
# next(gen)


def get_sequence_upto(x):
    for i in range(x):
        yield i


gen = get_sequence_upto(2)
print(next(gen))