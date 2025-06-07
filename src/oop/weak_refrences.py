import weakref


class Foo: ...


# ---- reference ----
foo = Foo()
weak_foo = weakref.ref(foo)

del foo

# ---- weak key dictionary ----
wk = weakref.WeakKeyDictionary()
foo = Foo()
wk[foo] = "foo"

del wk[foo]

# ---- weak value dictionary ----
wk = weakref.WeakValueDictionary()
foo = Foo()
wk["item"] = foo

del wk["item"]

# ---- weak set ----
wk = weakref.WeakSet()
foo1 = Foo()
foo2 = Foo()
foo3 = Foo()
wk.add(foo1)
wk.add(foo2)
wk.add(foo3)

# ---- finalize ----
foo = Foo()
weakref.finalize(foo, print, "Resource is deleted")

del foo

# ---- custom classes ----


class NoWeakref:
    __slots__ = ()  # breaks weakref


class SupportsWeakref:
    __slots__ = ('__weakref__',)
