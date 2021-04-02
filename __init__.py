import check50
import check50.c
import os.path
from os import path


@check50.check()
def q1_compiles():
    """q1 compiles"""
    if path.exists("794901.c"):
        check50.c.compile("794901.c")
    elif path.exists("794904.c"):
        check50.c.compile("794904.c")
    else:
        raise FileNotFoundError


@check50.check()
def q2_compiles():
    """q2 compiles"""
    if path.exists("794902.c"):
        check50.c.compile("794902.c")
    elif path.exists("794907.c"):
        check50.c.compile("794907.c")
    else:
        raise FileNotFoundError


@check50.check()
def q3_compiles():
    """q3 compiles"""
    check50.c.compile("788765.c")


@check50.check(q1_compiles)
def q1_io():
    """prints "hello, world\\n" """
    check50.run("./hello").stdout("[Hh]ello, world!?\n", regex=True).exit(0)


@check50.check(q2_compiles)
def q2_io():
    """prints "hello, world\\n" """
    check50.run("./hello").stdout("[Hh]ello, world!?\n", regex=True).exit(0)


@check50.check(q3_compiles)
def q3_io():
    """prints "hello, world\\n" """
    check50.run("./hello").stdout("[Hh]ello, world!?\n", regex=True).exit(0)