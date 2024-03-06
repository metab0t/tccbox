# Tccbox

[![](https://img.shields.io/pypi/v/tccbox.svg?color=brightgreen)](https://pypi.org/pypi/tccbox/)

Tccbox is a simple and easy way to install the Tiny C Compiler (TCC) on your system.

It uses the `mob` branch at https://repo.or.cz/tinycc.git to build and release the latest version.

```
pip install tccbox
```

After installation, you can use `python -m tccbox` to invoke tcc.

```
>>> python -m tccbox
Tiny C Compiler 0.9.28rc - Copyright (C) 2001-2006 Fabrice Bellard
Usage: tcc [options...] [-o outfile] [-c] infile(s)...
       tcc [options...] -run infile (or --) [arguments...]
...
...
```
