def reduce_rec (op, values):
    if len(values)==1:
        return values[0]
    
    return op(values[0], reduce_rec(op, values[1:]))


print(f'{reduce_rec(lambda x,y: x + y, [1,2,3,4,5])}')
# expected output: 15

print(f'{reduce_rec(lambda x,y: x * y, [1,2,3,4,5])}')
# expected output: 120