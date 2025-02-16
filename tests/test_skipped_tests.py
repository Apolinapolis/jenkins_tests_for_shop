import pytest


class TestSkipping:

    @pytest.mark.skip
    def test_skip(self):
        pass


    @pytest.mark.skip
    def test_skip2(self):
        pass


    @pytest.mark.skip
    def test_skip3(self):
        pass