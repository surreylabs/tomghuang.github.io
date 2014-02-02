---
layout: post2
title:  "Trying Code Snippets in codepad.org"
date:   2011-03-10 11:48:04
tags: utilities best-practices
---

[codepad.org][codepad] is an online compiler/interpreter for more than a dozen programming languages, such as C/C++, PHP, Perl, etc. It is very easy to use: write a few lines of code, hit the Submit button, and the execution result will appear at the bottom of the page.

It is a great tool for trying code snippets, learning language syntax, and communicate ideas. For example, I often forget how to use wchar vectors in C++. What I can do is grabbing *The C++ Standard Library: A Tutorial and Reference* and type the following code snippet in codepad.org:

```cpp
#include <string>
#include <vector>
#include <iostream>

int main(int argc, char **argv)
{
    vector<wchar_t> wc(10);
    wc[0] = L'A';
    wc[1] = L'B';

    wc.resize(3);
    wstring ws(wc.begin(), wc.end());
    //wstring ws(L"This is a book\n");
    wcout << ws << endl;

    return 0;
}
```

After hitting the Submit button, you will see the following page:

<img src="/assets/codepad-org.png" alt="codepad.org" class="img-rounded img-responsive figure">

Compare to writing prototype code snippets in Visual Studio and GCC, you don’t need to create a lot of temp source code files in your file system and you can try your ideas on any machine without installing any compiler/interpreter. It’s really another great example showing how cloud services can simplify our lives.

[codepad]: http://codepad.org/

