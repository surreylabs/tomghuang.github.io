---
layout: post2
title:  "Using Github Pages to Write Blogs"
date:   2015-07-13 10:34:04
tags: github blog jekyll markdown
---

I haven't updated my blog for a long time. One of the reasons is that I always think using git commands to update my blog is a tedious job, and I already forgot how I did it long time ago. However, when I recently found that I can use Github web interface to add a blog post, things changed. Here is a step-by-step procedure of creating a blog post, so I won't forget how to do it again.

Since I use Jekyll, the built-in blog system of Github Pages, all the blog posts are under the `<PROJ_ROOT>/_posts` directory. To add a blog post, go to the `_posts` directory and click the `+` sign to add a new file. The file name convention is `YYYY-MM-DD-blog-post-title.markdown`.

Then use the source code of this blog post as the template and submit the new blog post. To make writing blog posts as easy as possible, I don't write any comment for the commit. I believe minimalism can encourage myself writing more useful stuffs.

#### Code Snippet

Code snippet is appropriate for showing commands and one-liner.

```
$> ilmerge /target:winexe /out:..\crvw.exe crvw.exe crvcore.dll dotnetzip.dll
```
#### Code Listing

If you want to show a complete function or code file, you can use code listing and add syntax highlighting.

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

#### Styled Text

Here is *italics* and here is **bold**. You can also *mix __bold__ and italics together*. If you want to emphasize ~~removed text~~, you can use strikethrough.

#### Unordered List

* Item 1
* Item 2
* Item 3

#### Ordered List

1. Item 1
2. Item 2
3. Item 3

#### Nested List

* Item 1
  1. Step 1
  2. Step 2
  3. Step 3
* Item 2
  * Subitem 1
  * Subitem 2
  * Subitem 3

#### Link

For more markdown syntax reference, you can visit [Markdown Basics](https://help.github.com/articles/markdown-basics/) and [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/).

#### Image and Illustration

<img src="/assets/launchy.png" alt="Launchy" class="img-rounded img-responsive figure">

#### Table

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -------------:|
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |
