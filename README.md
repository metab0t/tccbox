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

It includes a fully-featured distribution of TCC, including the `tcc` command-line tool, the `libtcc` library and the `libtcc.h` header file.

Their paths can be found using the `tccbox` module:

```python
>>> import tccbox
>>> tccbox.tcc_bin_path()
'D:\\mambaforge\\Lib\\site-packages\\tccbox\\tcc_dist\\tcc.exe'
>>> tccbox.tcc_lib_dir() 
'D:\\mambaforge\\Lib\\site-packages\\tccbox\\tcc_dist'
>>> tccbox.tcc_include_dir()    
'D:\\mambaforge\\Lib\\site-packages\\tccbox\\tcc_dist\\libtcc'
```