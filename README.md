# ISDD Package Usage Example

This document provides an overview of how to use encoding and decoding in the `ISDD` format, as well as how to decode and access `ISDO` file properties.

## Code Overview

### 1. Importing the Module
```python
import isdd
```
- First, you need to import the `isdd` package to use ISDD functionalities.

### 2. Accessing ISDD Methods
```python
isdd.isddfile
isdd.search
```
- The `isdd` module contains two key methods: `isddfile` for handling ISDD files and `search` for searching functionalities within those files.

### 3. Encoding and Decoding Strings


#### Encoding a String
```python
isf = isdd.isddfile
encoded = isf.ISDD.encoding("Hello ISDD!")
print(encoded)  # Print the encoded result.
```
- This line encodes the string "Hello ISDD!" using the `ISDD.encoding` method, producing an encoded output, which is printed.

#### Decoding the Encoded String
```python
decoded = isf.ISDD.decoding(encoded)
print(decoded)  # Print the decoded result.
```
- The previously encoded string is decoded back to its original form using the `ISDD.decoding` method, and the result is printed.

### 4. Decoding an ISDO Object

#### Example Encoded ISDO String
```python
encoded = "55 47 39 75 62 33 42 76 65 57 38 67 4D 54 6B 35 4F 43 42 54 55 31 4D 74 53 55 6B 67 52 32 56 75 5A 47 56 79 56 48 6C 77 5A 54 6F 7A 49 45 4E 76 64 57 35 30 63 6E 6B 36 4F 44 45 67 61 58 4E 6B 5A 43 35 72 63 6D 38 75 61 33 49 67 51 32 56 79 64 47 6C 6D 61 57 4E 68 64 47 6C 76 62 6B 35 31 62 57 4A 6C 63 6A 70 77 62 32 35 76 63 47 39 35 62 7A 42 6E 4D 32 4D 34 4D 57 45 78 4D 44 55 30 4D 67 3D 3D"
```
- An example encoded string representing an ISDO (ISDD Object) is provided for decoding.

#### Decoding the ISDO Object
```python
isf = isdd.isddfile
isdd_object_decoded = isf.ISDO(encoded)
```
- The encoded ISDO string is decoded into an ISDO object using the `ISDO` method.

### 5. Printing ISDO Object Attributes
```python
print(isdd_object_decoded.name)    
# Print the name of the object.
print(isdd_object_decoded.country) 
# Print the country associated with the object.
print(isdd_object_decoded.gender)  
# Print the gender of the object.
print(isdd_object_decoded.madeat)  
# Print the place of manufacture.
print(isdd_object_decoded.engine)  
# Print engine information of the object.
print(isdd_object_decoded.dic)     
# Print the properties in dictionary format
```
