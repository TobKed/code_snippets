# GENERATORS


def print_iteration(iter_obj):
    for num in iter_obj:
        print(num)

def square_numbers(nums):
    for i in nums:
        yield (i*i)


# generator
my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)
print_iteration(my_nums)

# list comprehension (low performance)
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)
print_iteration(my_nums)

# generator comprehension (higher peroformance)
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)
print_iteration(my_nums)
