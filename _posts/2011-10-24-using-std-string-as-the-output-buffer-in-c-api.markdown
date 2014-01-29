---
layout: post2
title:  "Using std::string as the Output Buffer in C API"
date:   2011-10-24 16:26:04
tags: cpp api
---

In the traditional C programming style, when we want to get a string value, we need to allocate a character buffer that is big enough to hold the entire string from the function. For example, when we want to get the title of a console window in Windows, we need to call the `GetConsoleTitle function`. Here is how we do it in the traditional C style:

```cpp
#include <windows>

#define BUF_SIZE 1024

int main(int argc, char *argv[])
{
    char buf[BUF_SIZE] = {0};
    if (GetConsoleTitle(buf, BUF_SIZE) == 0)
    {
        return EXIT_FAILURE;
    }

    printf("%s\n", buf);
    return EXIT_SUCCESS;
}
```

However, we all know that traditional C string buffer is vulnerable because many standard string API functions don’t check boundaries appropriately, which can cause buffer overflow security flaws. To write more robust and secure software, we must learn some other ways to manipulate strings. One of the popular solutions is using `std::string`. Because `std::string` is part of the standard C++ library, it is portable. Because it can automatically adjust its internal buffer, it can avoid a lot of buffer overflow issues. Finally, because it has a complete set of methods and overloaded operators, it is easier to write readable program.

But how to use `std::string` in traditional C functions, such as Win32 API? The `c_str` method returns `const char *`, which can be the input of C functions but cannot be the buffer for the output parameters. To be the output buffer, we need to get the pointer to the contiguous memory that `std::string` uses to store the value. Here is the C++ way to use the `GetConsoleTitle` function:

```cpp
#include <windows.h>
#include <string>
#include <iostream>

#define BUF_SIZE 1024

int main(int argc, char *argv[])
{
    std::string buf(BUF_SIZE, '\0');
    if (GetConsoleTitleA(&buf[0], buf.capacity()) == 0)
    {
        return EXIT_FAILURE;
    }

    buf.resize(strlen(buf.c_str()));
    std::cout << buf << std::endl;
    return EXIT_SUCCESS;
}
```
In line 9, we delcare a `std::string` variable, initialize its length, and set its content to be all `NULL` (`'\0'`) characters. We need to set the length, so that `std::string` will pre-allocate memory; we need to specify the content, because it is a good habit to set the buffer to a known state.

In line 10, we use `&buf[0]` to get the pointer to the contiguous buffer, and use the capacity method to get the buffer size. The `&buf[0]` expression is the key. It is the only way that I know to get the pointer to the storage buffer in `std::string`. You may think this is a trick and is not portable across compilers. In fact, using `&buf[0]` to get the writable and contiguous buffer that is compatible with C API, is not only guaranteed by all STL implementations in the market, but also guaranteed by the latest C++ standard, C++11. So, you can safely use this technique in the future.

You may ask, "Why we need to resize `std::string` in line 15?" Well, that’s because `std::string` is not a `NULL` terminated string. When we initialize buf to have 1024 `NULL` characters, it does become a string that contains 1024 `NULL` characters. If you call `std::string.size()`, it will return 1024 as the string length. This is not what we want after calling the `GetConsoleTitle` function, so we call the resize method to make buf shrink and ignore the remaining `NULL`s.

That’s all you need to know about making `std::string` to be an output buffer in C functions. By using the above technique and the `c_str` method, you can use `std::string` with C functions and write wrappers around them, so that you can use `std::string` in other parts of you program.

