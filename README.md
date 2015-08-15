Prepend
=======

[![Current version on PyPI](http://img.shields.io/pypi/v/prepend.svg)](http://pypi.python.org/pypi/prepend/)

Prepends a list of files with text.


Motivation
----------

Maybe it's just me, but I often find myself prepending a bunch of files in a
directory with some text. Since I use this all the time, I figured I'd
share it in case it helps anyone else.


Installation
------------

To install prepend, simply:

```bash
$ pip install prepend
```


Usage
-----

To prepend a list of files in a directory with a specific extension:

```bash
$ pre 0 .png
1-screenshot.png -> 01-screenshot.png
2-screenshot.png -> 02-screenshot.png
3-screenshot.png -> 03-screenshot.png
4-screenshot.png -> 04-screenshot.png
5-screenshot.png -> 05-screenshot.png
6-screenshot.png -> 06-screenshot.png
7-screenshot.png -> 07-screenshot.png
8-screenshot.png -> 08-screenshot.png
9-screenshot.png -> 09-screenshot.png
```

You can also use the longhand name, `prepend`.


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository and make your changes
3. Send a pull request

If your PR has been waiting a while, feel free to [ping me on Twitter](http://twitter.com/joeyespo).

Use this software often? Please consider supporting me on
<a href="http://gratipay.com/joeyespo" title="Thank you!">
  <img align="center" style="margin-bottom:1px" src="http://joeyespo.com/images/gratipay-button.png" alt="Gratipay">
</a>
