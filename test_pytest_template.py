

def setup_module(module):
    print("setup_module")


def teardown_module(module):
    print("teardown_module")


class TestClass:
    @classmethod
    def setup_class(cls):
        print("setup_class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class")

    def setup_method(self):
        pass

    def setup_method(self, method):
        if method == self.test1:
            print("setup_method-test1")
        elif method == self.test2:
            print("setup_method-test2")
        else:
            print("setup_method-unknown!")

    def teardown_method(self, method):
        if method == self.test1:
            print("teardown_method-test1")
        elif method == self.test2:
            print("teardown_method-test2")
        else:
            print("teardown_method-unknown!")

    def test1(self):
        print("test1")
        assert True

    def test2(self):
        print("test2")
        assert True
