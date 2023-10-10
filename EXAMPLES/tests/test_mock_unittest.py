import pytest
import spamlib
from spamlib import Spam

HAM_VALUE = 42
HAM_RESULT = HAM_VALUE * 10


def test_spam_calls_ham(mocker):
    # need to patch spamlib.ham, not hamlib.ham
    mocker.patch("spamlib.ham", return_value=HAM_VALUE * 10)
    s = Spam(HAM_VALUE)  # Create instance of Spam, which calls ham()
    assert s.value == HAM_RESULT
    assert spamlib.ham.calledoncewith(HAM_VALUE)


if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner
