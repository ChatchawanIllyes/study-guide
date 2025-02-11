# Commonly Used Native Python Functions for Interviews
#
# Python provides many built-in functions and methods that are useful for solving
# coding problems efficiently. Below are some commonly used ones, along with their
# time and space complexities, and manual implementations.

from collections import Counter

# ====================== List Functions ======================

# 1. **reverse()**:
# - Reverses a list in-place using a two-pointer approach.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
arr = [1, 2, 3, 4]
arr.reverse()
print(arr)  # Output: [4, 3, 2, 1]

# Manual Implementation of reverse()
def manual_reverse(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(manual_reverse([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]

# 2. **sort()**:
# - Sorts a list in-place using Timsort (a hybrid sorting algorithm).
# - Time Complexity: O(n log n)
# - Space Complexity: O(n) (due to Timsort's space requirements)
arr = [3, 1, 4, 2]
arr.sort()
print(arr)  # Output: [1, 2, 3, 4]

# Manual Implementation of sort() (using QuickSort)
def manual_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return manual_sort(left) + middle + manual_sort(right)

print(manual_sort([3, 1, 4, 2]))  # Output: [1, 2, 3, 4]

# 3. **append()**:
# - Adds an element to the end of the list.
# - Time Complexity: O(1) (amortized)
# - Space Complexity: O(1)
arr = [1, 2, 3]
arr.append(4)
print(arr)  # Output: [1, 2, 3, 4]

# Manual Implementation of append()
def manual_append(arr, element):
    arr += [element]
    return arr

print(manual_append([1, 2, 3], 4))  # Output: [1, 2, 3, 4]

# 4. **pop()**:
# - Removes and returns the last element (or a specified index).
# - Time Complexity: O(1) for the last element, O(n) for an arbitrary index
# - Space Complexity: O(1)
arr = [1, 2, 3]
arr.pop()
print(arr)  # Output: [1, 2]

# Manual Implementation of pop()
def manual_pop(arr, index=-1):
    if index < 0:
        index = len(arr) + index
    if index < 0 or index >= len(arr):
        raise IndexError("Index out of range")
    element = arr[index]
    del arr[index]
    return element

print(manual_pop([1, 2, 3]))  # Output: 3

# 5. **extend()**:
# - Adds all elements of an iterable to the end of the list.
# - Time Complexity: O(k), where k is the length of the iterable
# - Space Complexity: O(k)
arr = [1, 2, 3]
arr.extend([4, 5])
print(arr)  # Output: [1, 2, 3, 4, 5]

# Manual Implementation of extend()
def manual_extend(arr, iterable):
    for element in iterable:
        arr.append(element)
    return arr

print(manual_extend([1, 2, 3], [4, 5]))  # Output: [1, 2, 3, 4, 5]

# 6. **index()**:
# - Returns the index of the first occurrence of a value.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
arr = [1, 2, 3, 2]
print(arr.index(2))  # Output: 1

# Manual Implementation of index()
def manual_index(arr, value):
    for i, element in enumerate(arr):
        if element == value:
            return i
    raise ValueError(f"{value} is not in list")

print(manual_index([1, 2, 3, 2], 2))  # Output: 1

# 7. **count()**:
# - Returns the number of occurrences of a value in the list.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
arr = [1, 2, 3, 2]
print(arr.count(2))  # Output: 2

# Manual Implementation of count()
def manual_count(arr, value):
    count = 0
    for element in arr:
        if element == value:
            count += 1
    return count

print(manual_count([1, 2, 3, 2], 2))  # Output: 2

# 8. **insert()**:
# - Inserts an element at a specified index.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
arr = [1, 2, 3]
arr.insert(1, 4)
print(arr)  # Output: [1, 4, 2, 3]

# Manual Implementation of insert()
def manual_insert(arr, index, element):
    if index < 0:
        index = len(arr) + index
    if index < 0 or index > len(arr):
        raise IndexError("Index out of range")
    return arr[:index] + [element] + arr[index:]

print(manual_insert([1, 2, 3], 1, 4))  # Output: [1, 4, 2, 3]

# ====================== String Functions ======================

# 1. **split()**:
# - Splits a string into a list based on a delimiter (default is whitespace).
# - Time Complexity: O(n)
# - Space Complexity: O(n)
s = "Hello World"
print(s.split())  # Output: ['Hello', 'World']

# Manual Implementation of split()
def manual_split(s, delimiter=' '):
    result = []
    start = 0
    for i, char in enumerate(s):
        if char == delimiter:
            result.append(s[start:i])
            start = i + 1
    result.append(s[start:])
    return result

print(manual_split("Hello World"))  # Output: ['Hello', 'World']

# 2. **join()**:
# - Joins a list of strings into a single string with a specified separator.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
arr = ['Hello', 'World']
print(' '.join(arr))  # Output: 'Hello World'

# Manual Implementation of join()
def manual_join(iterable, separator=''):
    result = ''
    for i, element in enumerate(iterable):
        if i > 0:
            result += separator
        result += element
    return result

print(manual_join(['Hello', 'World'], ' '))  # Output: 'Hello World'

# 3. **strip()**:
# - Removes leading and trailing whitespace (or specified characters).
# - Time Complexity: O(n)
# - Space Complexity: O(n)
s = "  Hello World  "
print(s.strip())  # Output: 'Hello World'

# Manual Implementation of strip()
def manual_strip(s, chars=None):
    if chars is None:
        chars = ' \t\n\r'
    start = 0
    end = len(s) - 1
    while start <= end and s[start] in chars:
        start += 1
    while end >= start and s[end] in chars:
        end -= 1
    return s[start:end + 1]

print(manual_strip("  Hello World  "))  # Output: 'Hello World'

# 4. **replace()**:
# - Replaces all occurrences of a substring with another substring.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
s = "Hello World"
print(s.replace("World", "Python"))  # Output: 'Hello Python'

# Manual Implementation of replace()
def manual_replace(s, old, new):
    result = ''
    i = 0
    while i < len(s):
        if s[i:i + len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

print(manual_replace("Hello World", "World", "Python"))  # Output: 'Hello Python'

# 5. **find()**:
# - Returns the index of the first occurrence of a substring (or -1 if not found).
# - Time Complexity: O(n)
# - Space Complexity: O(1)
s = "Hello World"
print(s.find("World"))  # Output: 6

# Manual Implementation of find()
def manual_find(s, substring):
    n = len(substring)
    for i in range(len(s) - n + 1):
        if s[i:i + n] == substring:
            return i
    return -1

print(manual_find("Hello World", "World"))  # Output: 6

# 6. **startswith() and endswith()**:
# - Checks if a string starts or ends with a specified substring.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
s = "Hello World"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World"))    # Output: True

# Manual Implementation of startswith()
def manual_startswith(s, prefix):
    return s[:len(prefix)] == prefix

# Manual Implementation of endswith()
def manual_endswith(s, suffix):
    return s[-len(suffix):] == suffix

print(manual_startswith("Hello World", "Hello"))  # Output: True
print(manual_endswith("Hello World", "World"))    # Output: True

# ====================== Dictionary Functions ======================

# 1. **get()**:
# - Retrieves the value for a key, with a default value if the key doesn't exist.
# - Time Complexity: O(1)
# - Space Complexity: O(1)
d = {'a': 1, 'b': 2}
print(d.get('c', 0))  # Output: 0

# Manual Implementation of get()
def manual_get(d, key, default=None):
    if key in d:
        return d[key]
    return default

print(manual_get({'a': 1, 'b': 2}, 'c', 0))  # Output: 0

# 2. **items()**:
# - Returns a view of key-value pairs in the dictionary.
# - Time Complexity: O(1) to create the view
# - Space Complexity: O(1)
d = {'a': 1, 'b': 2}
print(d.items())  # Output: dict_items([('a', 1), ('b', 2)])

# Manual Implementation of items()
def manual_items(d):
    return [(k, v) for k, v in d.items()]

print(manual_items({'a': 1, 'b': 2}))  # Output: [('a', 1), ('b', 2)]

# 3. **keys() and values()**:
# - Returns a view of keys or values in the dictionary.
# - Time Complexity: O(1) to create the view
# - Space Complexity: O(1)
print(d.keys())   # Output: dict_keys(['a', 'b'])
print(d.values()) # Output: dict_values([1, 2])

# Manual Implementation of keys()
def manual_keys(d):
    return [k for k in d]

# Manual Implementation of values()
def manual_values(d):
    return [v for v in d.values()]

print(manual_keys({'a': 1, 'b': 2}))    # Output: ['a', 'b']
print(manual_values({'a': 1, 'b': 2}))  # Output: [1, 2]

# 4. **pop()**:
# - Removes and returns the value for a key (or raises KeyError if not found).
# - Time Complexity: O(1)
# - Space Complexity: O(1)
print(d.pop('a'))  # Output: 1
print(d)           # Output: {'b': 2}

# Manual Implementation of pop()
def manual_pop(d, key, default=None):
    if key in d:
        value = d[key]
        del d[key]
        return value
    if default is not None:
        return default
    raise KeyError(f"{key} not found")

print(manual_pop({'a': 1, 'b': 2}, 'a'))  # Output: 1

# ====================== Set Functions ======================

# 1. **add()**:
# - Adds an element to the set.
# - Time Complexity: O(1)
# - Space Complexity: O(1)
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# Manual Implementation of add()
def manual_add(s, element):
    s |= {element}
    return s

print(manual_add({1, 2, 3}, 4))  # Output: {1, 2, 3, 4}

# 2. **intersection()**:
# - Returns the intersection of two sets.
# - Time Complexity: O(min(len(s1), len(s2)))
# - Space Complexity: O(k), where k is the size of the intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2))  # Output: {2, 3}

# Manual Implementation of intersection()
def manual_intersection(s1, s2):
    return {x for x in s1 if x in s2}

print(manual_intersection({1, 2, 3}, {2, 3, 4}))  # Output: {2, 3}

# 3. **union()**:
# - Returns the union of two sets.
# - Time Complexity: O(len(s1) + len(s2))
# - Space Complexity: O(len(s1) + len(s2))
print(s1.union(s2))  # Output: {1, 2, 3, 4}

# Manual Implementation of union()
def manual_union(s1, s2):
    return s1 | s2

print(manual_union({1, 2, 3}, {2, 3, 4}))  # Output: {1, 2, 3, 4}

# ====================== Counter ======================

# 1. **Counter**:
# - Counts the frequency of elements in an iterable.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
arr = [1, 2, 2, 3, 3, 3]
counter = Counter(arr)
print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1})

# Manual Implementation of Counter
def manual_counter(iterable):
    counter = {}
    for element in iterable:
        counter[element] = counter.get(element, 0) + 1
    return counter

print(manual_counter([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}

# ====================== Max and Min ======================

# 1. **max()**:
# - Returns the maximum value in an iterable.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
arr = [1, 2, 3, 4]
print(max(arr))  # Output: 4

# Manual Implementation of max()
def manual_max(iterable):
    if not iterable:
        raise ValueError("max() arg is an empty sequence")
    max_val = iterable[0]
    for val in iterable:
        if val > max_val:
            max_val = val
    return max_val

print(manual_max([1, 2, 3, 4]))  # Output: 4

# 2. **min()**:
# - Returns the minimum value in an iterable.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
arr = [1, 2, 3, 4]
print(min(arr))  # Output: 1

# Manual Implementation of min()
def manual_min(iterable):
    if not iterable:
        raise ValueError("min() arg is an empty sequence")
    min_val = iterable[0]
    for val in iterable:
        if val < min_val:
            min_val = val
    return min_val

print(manual_min([1, 2, 3, 4]))  # Output: 1

# ====================== Other Useful Functions ======================

# 1. **enumerate()**:
# - Returns an iterator of tuples containing indices and values.
# - Time Complexity: O(1) to create the iterator
# - Space Complexity: O(1)
arr = ['a', 'b', 'c']
for i, val in enumerate(arr):
    print(i, val)  # Output: 0 a, 1 b, 2 c

# Manual Implementation of enumerate()
def manual_enumerate(iterable, start=0):
    return zip(range(start, start + len(iterable)), iterable)

for i, val in manual_enumerate(['a', 'b', 'c']):
    print(i, val)  # Output: 0 a, 1 b, 2 c

# 2. **zip()**:
# - Combines two or more iterables into a single iterator of tuples.
# - Time Complexity: O(1) to create the iterator
# - Space Complexity: O(1)
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Manual Implementation of zip()
def manual_zip(*iterables):
    min_length = min(len(it) for it in iterables)
    return [tuple(it[i] for it in iterables) for i in range(min_length)]

print(manual_zip([1, 2, 3], ['a', 'b', 'c']))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 3. **map()**:
# - Applies a function to all items in an iterable.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
arr = [1, 2, 3]
print(list(map(lambda x: x * 2, arr)))  # Output: [2, 4, 6]

# Manual Implementation of map()
def manual_map(func, iterable):
    return [func(x) for x in iterable]

print(manual_map(lambda x: x * 2, [1, 2, 3]))  # Output: [2, 4, 6]

# 4. **filter()**:
# - Filters elements of an iterable based on a condition.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
arr = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, arr)))  # Output: [2, 4]

# Manual Implementation of filter()
def manual_filter(func, iterable):
    return [x for x in iterable if func(x)]

print(manual_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # Output: [2, 4]
