def get_chunk(transmission, chunk_size):
    for x in range(0, len(transmission)+1):
        yield (transmission[x:x+chunk_size], (x+chunk_size))

def get_answer(input, size):
    return ([x for x in get_chunk(input, size) if len(set(x[0])) == len(x[0])][0][1])

with open('input.txt', 'r') as input:
    # part 1
    print(get_answer(input.read(), 4))
    input.seek(0, 0)

    # part 2
    print(get_answer(input.read(), 14))
