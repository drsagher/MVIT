# Data Structures (using the collections module)
from collections import deque, defaultdict, namedtuple, Counter

# Deque (Double-ended queue)
my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
print("\nDeque:", my_deque)

# Defaultdict (Dictionary with a default value for missing keys)
my_defaultdict = defaultdict(int)
my_defaultdict["a"] = 1
print("Defaultdict:", my_defaultdict["a"], my_defaultdict["b"]) #my_defaultdict["b"] returns 0 as the default value

# Namedtuple (Tuple with named fields)
Point = namedtuple("Point", ["x", "y"])
point = Point(1, 2)
print("Namedtuple:", point.x, point.y)


# Counter (Counts the frequency of elements in a sequence)
my_counter = Counter([1, 1, 2, 3, 3, 3, 4])
print("Counter:", my_counter) #prints the frequency of elements, example 3:3 means element 3 is present 3 times

# None
none_variable = None
print("None:", none_variable)