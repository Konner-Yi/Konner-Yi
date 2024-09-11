class NoSuchCategoryError(Exception):
    pass

def get_average_classic_rating(filename):
    temp=[]
    names=[]
    list_of_books = []
    counter = 0
    average = 0
    file = open(filename, 'r')
    names=next(file).split(',')
    for line in file:
        temp=line.split(',')
        book = {names[0]: temp[0], names[1]: temp[1], names[2]: temp[2], names[3]: temp[3], names[4]: temp[4], names[5]: float(temp[5]), names[6]: temp[6]}

        list_of_books.append(book)

    for x in list_of_books:
        if x[names[4]] == "Classic":
            counter+=1
            average += x[names[5]]
        

    average = average/counter

    if counter == 0:
        raise NoSuchCategoryError("No books in that category found!")

    return average

        
print(f'{get_average_classic_rating("data.csv"):0.1f}')
# expected output: get_average_classic_rating("data.csv") = 4.6