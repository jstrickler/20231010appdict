import pytest  # Needed for test runner
import spamlib
from spamlib import SpamSearch   # subject under test

SEARCH_TERM = 'bug'
SEARCH_STRING = 'lightning bug'


def test_spam_search_calls_re_search(mocker):   # Unit test
    # Patch re.search (i.e., replace re.search with a Mock object that 
    # records calls to it)
    mocker.patch('spamlib.re.search')  
    
    s = SpamSearch(SEARCH_TERM, SEARCH_STRING)  # Create instance of SpamSearch
    s.findit()   # Call the method under test

    # Check that method was called just once with the expected parameters
    spamlib.re.search.assert_called_once_with(SEARCH_TERM, SEARCH_STRING)  


if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner
