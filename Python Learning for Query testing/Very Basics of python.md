# Very Basics of python

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

# Class

#### `self`

`self` is the first parameter of python class. self is the first parameter of class method. used to access its own method and properties

#### `__init__()` 

Constructor