

class Meta(type):
    cls_names = []
    attrs_count = 0

    def __new__(cls, name, bases, attrs):
        Meta.cls_names = Meta.cls_names + [name]
        methods = [attr for attr in attrs if callable(attrs[attr])]
        Meta.attrs_count += len(methods)
        return super().__new__(cls, name, bases, attrs)

    def show_attrs():
        print(Meta.cls_names, Meta.attrs_count)


class Class1(metaclass=Meta):
    def method1(self):
        pass


class Class2(metaclass=Meta):
    def method2(self):
        pass
    def method2_2(self):
        pass


class Class3(metaclass=Meta):
    def method3(self):
        pass

Meta.show_attrs()