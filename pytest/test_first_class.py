
class TestClass:

    def test_function(self):
        result = 1 + 2
        assert result == 3


    def test_not_equals(self):
        bad_result = 'not this'
        assert 'actual result' != bad_result


    def test_comparisons(self):
        result = 6
        assert result > 5
        assert result < 9
        assert result >= 6
        assert result <= 6


    def test_is_not_operator(self):
        expected = object()
        actual = object()

        assert actual is not expected


    def test_is_operator(self):
        expected = object()
        actual = expected

        assert actual is expected
