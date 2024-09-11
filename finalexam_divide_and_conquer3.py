def product_dc (values):

    if len(values) == 0:
        return 1
    elif len(values) == 1:
        return values[0]

    middle = len(values) // 2
    left_side = product_dc(values[:middle])
    right_side = product_dc(values[middle:])

    return left_side*right_side













