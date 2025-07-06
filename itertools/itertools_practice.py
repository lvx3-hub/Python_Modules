# ----------------------------
# Welcome Message
# ----------------------------
print("-" * 5, "Hello, Welcome to Python itertools practice!", "-" * 5)
print("Let's explore and practice various methods and properties of Python's itertools module\n")

import itertools as itt

# ==========================================================
# 1. INFINITE ITERATORS
# ==========================================================
# These iterators generate infinite sequences. Use them carefully with break or slicing.

print("\n🔁 1. Infinite Iterators\n")

# 1.1 count(start=0, step=1): returns an iterator that counts indefinitely
for i in itt.count(10):  # start from 10, step by 1
    if i > 15:
        break
    print(f"count: {i}")

# 1.2 cycle(iterable): cycles through elements endlessly
cycle_iter = itt.cycle(["A", "B", "C"])
for i in range(6):
    print(f"cycle: {next(cycle_iter)}")

# 1.3 repeat(object, times=None): repeats the object (infinitely or a fixed number of times)
for i in itt.repeat("Repeat Me", 3):
    print(f"repeat: {i}")


# ==========================================================
# 2. COMBINATORIC ITERATORS
# ==========================================================
# Used to create combinations, permutations, and cartesian products.

print("\n🔢 2. Combinatoric Iterators\n")

data = [1, 2, 3]

# 2.1 product(*iterables, repeat=1): Cartesian product
for item in itt.product(data, repeat=2):
    print(f"product: {item}")

# 2.2 permutations(iterable, r): All ordered arrangements of length r
for item in itt.permutations(data, 2):
    print(f"permutation: {item}")

# 2.3 combinations(iterable, r): All unique unordered combinations
for item in itt.combinations(data, 2):
    print(f"combination: {item}")

# 2.4 combinations_with_replacement(iterable, r): Like combinations, but allows duplicates
for item in itt.combinations_with_replacement(data, 2):
    print(f"comb_with_replacement: {item}")


# ==========================================================
# 3. TERMINATING ITERATORS
# ==========================================================
# These iterators return finite results. Let's divide them further by purpose.

print("\n🧪 3. Terminating Iterators\n")


# 3A. FILTERING ITERATORS
print("\n🔍 3A. Filtering Iterators\n")

# 3A.1 compress(data, selectors): select items where selector is True
data = ['a', 'b', 'c', 'd']
selectors = [1, 0, 1, 0]
for item in itt.compress(data, selectors):
    print(f"compress: {item}")

# 3A.2 dropwhile(predicate, iterable): drop items while condition is True
for item in itt.dropwhile(lambda x: x < 5, [1, 4, 6, 7, 2]):
    print(f"dropwhile: {item}")

# 3A.3 takewhile(predicate, iterable): take items while condition is True
for item in itt.takewhile(lambda x: x < 5, [1, 4, 6, 7, 2]):
    print(f"takewhile: {item}")

# 3A.4 filterfalse(predicate, iterable): keep items where condition is False
for item in itt.filterfalse(lambda x: x % 2 == 0, range(10)):
    print(f"filterfalse (odd): {item}")


# 3B. TRANSFORMING ITERATORS
print("\n🔧 3B. Transforming Iterators\n")

# 3B.1 starmap(function, iterable): apply function with unpacked arguments
from math import pow
pairs = [(2, 3), (3, 2), (10, 2)]
for result in itt.starmap(pow, pairs):
    print(f"starmap (pow): {result}")

# 3B.2 islice(iterable, start, stop[, step]): slice iterator like a list
for item in itt.islice(range(10), 2, 8, 2):
    print(f"islice: {item}")


# 3C. COMBINING / GROUPING ITERATORS
print("\n🔗 3C. Combining / Grouping Iterators\n")

# 3C.1 chain(iter1, iter2, ...): join multiple iterables
for item in itt.chain("AB", [1, 2]):
    print(f"chain: {item}")

# 3C.2 chain.from_iterable(iterable_of_iterables)
nested = [[1, 2], [3, 4]]
for item in itt.chain.from_iterable(nested):
    print(f"chain.from_iterable: {item}")

# 3C.3 zip_longest(*iterables, fillvalue): zip but fill shorter sequences
for item in itt.zip_longest("AB", [1], fillvalue='-'):
    print(f"zip_longest: {item}")


# 3D. DUPLICATING OR GROUPING ITERATORS
print("\n📚 3D. Duplicating / Grouping Iterators\n")

# 3D.1 tee(iterable, n): create n independent iterators
original = iter([10, 20, 30])
it1, it2 = itt.tee(original, 2)
print(f"tee it1: {[x for x in it1]}")
print(f"tee it2: {[x for x in it2]}")

# 3D.2 groupby(iterable, key): group consecutive items by a key function
# Note: Input must be sorted on the same key for grouping to work properly.
data = sorted(['apple', 'apricot', 'banana', 'avocado'], key=lambda x: x[0])
for key, group in itt.groupby(data, key=lambda x: x[0]):
    print(f"groupby {key}: {list(group)}")
