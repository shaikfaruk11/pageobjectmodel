import pytest

from Testcases.Basetest import Basetest
from page.SearchPage import SearchPage
from utilities import ConfigReader
from utilities.ConfigReader import readConfig


class Test_signup(Basetest):
    @pytest.mark.usefixtures("log_on_failure")
    def test_signups(self):
        search = SearchPage()
        search.search_in_google()


