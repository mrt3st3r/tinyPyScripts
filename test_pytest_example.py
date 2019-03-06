import random
import time
import pytest


"""
example of pytests
download plugins from http://plugincompat.herokuapp.com/
"""
import time
def timing(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print('Elapsed time: {}'.format(finish - start))
    return wrapper

@timing
@pytest.mark.parametrize("test_input, expected_output", [(5, 10), (2, 4)])
def test_method1(test_input, expected_output):
    total = test_input * 2
    assert total == expected_output



@timing
@pytest.fixture(scope="module")
def setUp():
    print("setup method is running now!")
    yield
    print("teardown at the end of last test")

def test_calc_multiply(setUp):
    result = 10 * 3
    assert result == 30

@pytest.mark.skip("dont want to execute on the current build")
def test_another_calc_Test():
    pass

a = 101
@pytest.mark.skipif(a>100, reason="blah")
def test_failure():
    assert 1==1

@pytest.mark.Smoke
def test_sm1():
    pass

@pytest.mark.full
def test_sanity1(setUp):
    pass

@pytest.mark.Sanity
def test_sanity2():
    pass

@pytest.mark.full
def test_Asserts():
    a,b=1,2
    assert(a==b, "This should fail.")
    # if a != b:
    #     raise ArithmeticError("they ara not equal!")

@pytest.mark.xfail
def test_list_assertion():
    a = [1,2,3,4]
    b = [1,2,4,3]
    assert a == b

@pytest.mark.smoke
def test_marks():
    assert 1 == 1

@pytest.mark.xfail(reason="flaky test , jira #123", strict=False)
def test_flakyTest():
    assert random.randint(1,3) == 2

