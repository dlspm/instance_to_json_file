import db
from example.bar import Bar


class Foo(db.Model):
    FILE = __file__


if __name__=="__main__":
    f = Foo()
    f.a = Bar()
    f.a.b = [1, 2, 3]
    f.a.c = {"a": 1, "b": 1}
    f.b = 3

    db.write_json(f.to_dict())
    new_f = Foo.init(db.read_json())
    print("new")
