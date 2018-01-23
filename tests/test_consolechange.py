import pytest

import consolechange


def test_consoletitle():
    consolechange.consoletitle("testing...")
    # reset back to default.
    consolechange.consoletitle("")


def test_consolesize():
    # test with 15 rows and 30 cols.
    consolechange.consolesize(15, 30)
