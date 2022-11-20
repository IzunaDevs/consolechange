import consolechange


def test_consoletitle():
    consolechange.consoletitle("testing...")
    # reset back to default.
    consolechange.consoletitle("")
