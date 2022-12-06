def get_chunk(transmission, chunk_size):
    for x in range(0, len(transmission)+1):
        chunk = transmission[x:x+chunk_size]
        x += 1
        yield (chunk, (x+chunk_size-1))

# part 1
with open('input.txt', 'r') as input:
    transmission = input.read()
    chunk = get_chunk(transmission, 4)
    while x := next(chunk):
        data, count = x
        if(len(set(data)) == len(data)):
            print(data, count)
            break

# part 2
with open('input.txt', 'r') as input:
    transmission = input.read()
    chunk = get_chunk(transmission, 14)
    while x := next(chunk):
        data, count = x
        if(len(set(data)) == len(data)):
            print(data, count)
            break