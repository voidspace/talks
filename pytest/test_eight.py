

class TestClassOne:

    def test_one(self, class_fixture, module_fixture, session_fixture):
        print(f"{self.__class__.__name__}: Test one")
        assert True

    def test_two(self, class_fixture, module_fixture, session_fixture):
        print(f"{self.__class__.__name__}: Test two")
        assert True

    def test_three(self, class_fixture, module_fixture, session_fixture):
        print(f"{self.__class__.__name__}: Test three")
        assert True


class TestClassTwo:

    def test_one(self, class_fixture, module_fixture, session_fixture):
        print(f"{self.__class__.__name__}: Test one")
        assert True

    def test_two(self, class_fixture, module_fixture, session_fixture):
        print(f"{self.__class__.__name__}: Test two")
        assert True

    def test_three(self, class_fixture, module_fixture, session_fixture):
        print(f"{self.__class__.__name__}: Test three")
        assert True


def test_function_one(function_fixture, module_fixture, session_fixture):
    print("test_function_one")


def test_function_two(function_fixture, module_fixture, session_fixture):
    print("test_function_two")
