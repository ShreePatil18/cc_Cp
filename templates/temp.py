
try:
    # 👇️ using Python 3.10+
    from collections.abc import Mapping
except ImportError:
    # 👇️ using Python 3.10-
    from collections import Mapping


# 👇️ <class 'collections.abc.Mapping'>
print(Mapping)