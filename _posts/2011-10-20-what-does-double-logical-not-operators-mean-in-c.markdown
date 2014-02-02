---
layout: post2
title:  "What does Double Logical Not Operators (!!) Mean in C"
date:   2011-10-20 13:54:04
tags: web utilities
---

Sometime you will see the following statement in C/C++ source code:

```cpp
bool isKeepGoing = !!func();
```
You may wonder, "Why the author uses double logical not (`!!`)? Convert to the opposite boolean value, and convert back? It doesn't make any sense to me..."

Well, what the author really wants to do is converting the return value of the `func` function to a boolean value: The first logical operator will convert whatever return value to the opposite boolean value, and then the second logical operator will convert the opposite value back.

To be honest, this is a horribly obscure way to do the boolean type conversion. Nearly 99.999% of C/C++ programmers won't understand what the statement really means. They can understand the syntax, but they cannot understand why. "Is there any trick behind this statement?"

Unless you want to obfuscate your source code, please, please don't use this kind of statement. Instead, you can use normal casting to clearly express what you want to do:

```cpp
bool isKeepGoing = (bool)func();
```

[yagbe]: https://chrome.google.com/extensions/detail/jdnejaepfmacfdmhkplckpfdcjgbeode

