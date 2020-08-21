# Notes on python

## Variable Types

**integer: ** Stores integer values

**float:** Stores float values

**boolean: ** Boolean values either `True` or `False`

**string: ** Stores strings



## Casting data types

```python
intVariable = 3;
print("She is  " + str(int));
```



## String

Strings are immutable in python. we cannot change string character by index

### Multiplication of string in python: 

expression `"hello" * 3` will return "hellohellohello"

### Concatenation of string:

```python
firstName = "Prince";
lastName = "Billy"
fullName = firstname + ' ' + lastname # "Prince Billy"
```

### Index in string

We can access characters of string using index

``` python
python = "Python"
python = python[0] #returns 'P'
```

negative index will start counting from last. index -1 will return the last element

```python
python[-1] /returns 'n'
```

### String slicing

**syntax**:

```python
str[start:end] # items start through end-1
str[start:]    # items start through the rest of the array
str[:end]      # items from the beginning through end-1
str[:] 		 #returns full string
```

### Check weather a string contain in another string

```python
type here"billy" in "prince in billy graham karmoker" #returns true
"meow" in "prince in billy" #returns false
```

### Define multi line string

We can define multi-line string using three """ double quotation mark.

```python
"""
This is 
a multi-lin
string """
```

### Get string length

```python
len(str)
```

### String Formating

```python
"This is a string %s." % "prince"
"This is a number %d." % 34
"This is a float %f" % 34.3
```



## List

### List can be indexed and sliced like string

```python
myvar = [34, 2, 3, 53, 15];
myvar[0] #34
myvar[-2] #53
myvar[2:] #[3, 53, 15]

//clearing a range of list using slice
myvar[2:4] = []
```

### Append to list

```python
myvar.append(34) #appends an item to list
```

### Copying a list:

```diff
my_foods = ['Potato mash', 'Pizza', 'Bakon', 'Banana']
- friend_foods = my_foods #makes a alias to to my_foods
+ friend_foods = my_foods[:] #use slice operator to make a real copy
```



## Tuples

Same as list but we cannot add, change or delete in tuples. 

```python
binarydigits = (0, 1);
```

A tuples with single item must have trailing (,) comma:

```python
oneValue = ("me",)
```



## Dictonary

Similar to List but we access it using key rather than index

```python
dct = {'key1' : "value1", 'key2' : "value2"}
```

Return all keys & values dictonary:

```python
dct.key(); #return keys
dct.values(); #return values	
```



### In Keyword with List, Tupple and Values

Check weather a value is in list or tupple

```python
values = [43, 5, 2]
43 in values #True
tup = (34,3,2);
35 in tup #False
```

Check weather a key exists in tuples

```python
person = {
	'firstname' : 'Prince Billy Graham', 
	'lastname' : 'Karmoker'
	'age' : 22
}
'lastname' in person #True
```

### IS and NOT Operator

```python
name = 'John'
name is 'John'
name is not 'Tom'
```



## Function

#### Keyword argument:

We can explicitly specify the argument in any order without remembering their position

```python
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print("I have a " + animal_type +  ".");
    print("My " + animal_type + "'s name is " + pet_name.title() + ".");

describe_pet("bird", "Cute Pie");

#explicitly specifing the argement in any order
describe_pet(pet_name = "Meo", animal_type="Cat")		
```

#### Arbitrary number of argument

```python
def make_pizza(size, *topings):
    "This function allows arbitrary number of arguments"
    print ("Creating a pizza of size " + str(size))
    if topings:
        for item in topings:
            print("- " + item);
    
make_pizza(12, 'cheese', 'sause', 'meoneese');
make_pizza(5)

```

#### Arbitrary number of keyword argument

```python
def build_profile (first, last, **user_info):
    profile = {
            'firstname' : first,
            'lastname' : last
            }

    for k, v in user_info.items():
        profile[k] = v

    return profile;

user_profile = build_profile("prince billy graham", "karmoker")
user_profile = build_profile("winy", "chicham", age=17, gender= "female", hobbies=['art', 'game'])
print (user_profile)

```

**When we include both kind of Arbitrary arguments we have to keep the non keyword argument first**.

Example

```python
def myfunc(positional_arg1, positional_arg2, *arb, **key_arb):
    ...
```

## Import

```python
import package_or_module_name
import package_or_module name as x

from package_or_module import yfunction
from package_or_module import yfunction as x

from package_or_module import pfunction, qfunction, sfunction as x, zfunction
```



## Class

#### `self`

`self` is the first parameter of python class. self is the first parameter of class method. used to access its own method and properties

#### `__init__()` 

Constructor



## Some important functions and different uses:

### string

```python
#case
str.upper() #converts string to uppercase
str.title() #capitalizes only first letter and makes lower case all other letters
str.lower() #converts string to lowercase

#strip
str.strip() #removes whitespaces arround the string
str.lstrip() #removes whitespaces only from left sides
str.rstrip() #removes whitespaces only from right side
```

### list

```python
##add item
ls.append(item); #adds an item to the end of list 
ls.insert(0, item); #inserts an item at any position of the string


##remove an item 
del ls[2] #removes the item at index 2
last_item = ls.pop() #removes and returns the last item from list
last_item.remove('value') #remove an item using its value

##sorting
#permenent sorting
ls.sort() #permenent sort in ascending order
ls.sort(reverse = True) #permenent sort in ddscending order
#temporary sort
sorted_ls = sorted(carsp)
sorted_ls = sorted(cars, reverse = true)

##looping throw a list 
for magician in magicians:
    print (magician) #prints all magician in magicians

    
##statistical functions
min(ls) #prints the minmum in a list of same catagory items
max(ls) #prints the maximum in a list of same catagory items
sum(ls) #prints the sum from a number list


##list comprehension using range
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
"We can simplify this in one line"
cubes = [i ** 3 for i in range(1, 11)]

```



### Range

```python
a_range_of_4_items = range(4) #returns a range of 4 items
myrange = range(i, j) #contains i to j-1 element
myrange = range(2, 100, 2) #contains all even number range(start, end-1, step)


```

