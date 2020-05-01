# python 学习笔记 - 布尔运算

1. What are the two values of the Boolean data type? How do you write them?

   `True` and `False`.

2. What are the three Boolean operators?

   `and`, `or`, `not`. 

3. Write out of the truth tables of each Boolean operator(that is, every possible combination of Boolean values for the operator and what they evaluate to.)

```python
True and True   True
True and False  False
False and True  False
False and False False
True or True True
True or False True
False or True True
False or False False
not True False
not False True
```


4. What do the following expressions evaluate to?

```python
(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)

False
False
True
False
False
True

```

5. What are the six comparison operators?

```python
==
!=
<
>
<=
>=
```


6. What is the difference between the equal to operator and the assignment operator?

   The == operator (equal to) asks wether two values are the same as each other.

   The = operator (asignment) puts the value on the right into the variable on the left.

7. Explain what a condition is and where you should use one.

   The Boolean expressions you've seen so far aould all be considered conditions, which are the same thing as expressions; condition is just a more specific name in the context of flow control statement. Conditions always evaluate down to a Boolean value, `True` or `False`. A flow control statement decides what to do based on wether its consition is `True` or `False`, and almost every flow control statement ueses a condition.

8. Identify the three blocks in this code:

```python
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```

Block 1: 

```python
print('eggs')
if spam > 5
    print('bacon')
else:
    print('ham')
print('spam')
```

Block 2:

```python
print('bacon')
```

Block 3:

```python
print('spam')
```

9. Write code the prints `Hello` if `1` is stored in `spam`, print `Howdy` if `2` is stored in `spam`, and prints `Greetings` if anything else is stored in `spam`.

```python
if spam == 1:
    print('Helo')
elif spam == 2:
    print('Howdy')
else:
    print("Greetings")
```


10. What keys can you press if your program is stuck in an infinite loop?

11. What is the difference between `break` and `continue` ?

12. What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a `for` loop?

13. Write a short program the prints the numbers `1` to `10` using a `for` loop. Then write an equivalent program that prints the numbers `1` to `10` using a `while` loop.

14. If you had a function named `bacon()` inside a module named `spam`, how do you call it after importing `spam`?

	**Extra credit:** Look up the `round()` and `abs()` functions on the internet, and find out what they do. Experiment with them in the interactive shell.
