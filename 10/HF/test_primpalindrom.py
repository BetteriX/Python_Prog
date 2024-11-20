from prim_utils import palindrom_prim


def test_palindrom_prim():
    assert palindrom_prim(31) == 101
    assert palindrom_prim(130) == 131
    assert palindrom_prim(131) == 131
    assert palindrom_prim(1977) == 10301
