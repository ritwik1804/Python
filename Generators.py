#generator function store the info so that value can be created
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))

for j in gen:
    print(j)