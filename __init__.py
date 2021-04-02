import check50
import check50.c


@check50.check()
def q1_compiles():
    """q1 compiles"""
    check50.c.compile("q1.c")


@check50.check()
def q2_compiles():
    """q2 compiles"""
    check50.c.compile("q2.c")


@check50.check()
def q3_compiles():
    """q3 compiles"""
    check50.c.compile("q3.c")


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