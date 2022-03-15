from tests.flow.flo import Flo


def test_one_and_done():
    Flo.test("tests/flow/one_and_done.sim.txt")