# python 学习笔记 - 基础知识

1. Which of the following are operators, and witch are values?

```python
*
'hello'
-88.8
-
/
+
5
```

   `*`, `-`, `/`, `+` are operators; 'hello',`-88.8`, `5` are values.

2. Which of the following is a variable, and witch is a string?

```python
spam
'spam'
```

   `spam` is a variable, `'string'` is a string.

3. Name three data types.

   Integers, Floating-pointing numbers and Strings.

4. What is an expression made up of? What do all expressions do?

   Expressions consist of *values* and *operators*, and they can always *evaluate* down to a single value.

5. This chapter introduced assignment statement, like `spam = 10`. What is the difference between an expression and a statement?

   An assignment statement consists of a variable name, an equal sign (called the *assignment operator*). and the value to be stored. 

6. What does the variable `bacon` contain after the following code runs?

```python
bacon = 20
bacon + 1
```

   21

7. What should the following two expressions evaluate to?

```python
'spam' + 'spamspam'
'spam' * 3
```

   `'spamspamspam'`

8. Why is `eggs` is a valid variable name while `100` is invalid?

   Because name of a variable can\`t begin with a number.

9. What three functions can be used to get the integer, floating-point number, or string version of a value?

```python
int()
float()
str()
```

10. Why does this expression cause an error? How can you fix it?

	```python
	'I have eaten ' + 99 + ' burritos.'
	```

	```python
	'I have eaten ' + str(99) + ' bussitos.'
	```

	**Extra credit:** Search online for the Python documentation for the `len()` function. It will be on a web page titled "Built-in Functions." Skim the list if other functions Python has, look up what the `round()`function does, and experiment with it in the interactive shell.

	`len()`

	Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list or range) or a collection (such as a dictionary, set, or frozen set.)

	`round()`

	Return *number* rounded to *ndigits* precision after the decimal point. If *ndigits* i omitted or is `None`, it returns the nearest integer to its input.

	For the built-in types supporting `round()`, values are rounded to the closed multiple of 10 to the power minus *ndigits*; if two multiples are equally closer rounding is done toward the even choice (so, for example, both `round(0.5)`  and `round(-0.5)` are `0`, and `round(1.5)` is `2`). Any integer value is valid for *ndigits* (positive, zero, or negative). The return value is an integer if *ndigits* if omitted or `None`. Otherwise the return value has the same type as *number*.

	For a general Python object `number`, `round` delegates to `number._round_`.




