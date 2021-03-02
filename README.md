# classic-computer-science-problems-in-python
Codding parts for Classic Computer Science Problems in Python book

Code examples for the book *Classic Computer Science Problems in Python* by David Kopec

![Classic Computer Science Problems in Python Cover](cover.jpg)

# Python Tips

### Classes

Generics, static fields and methods, properties
```python
from typing import Generic, TypeVar, List

T = TypeVar('T')

class AwesomeClassWithGenerics(Generic[T]):
    static_field = 'ABC'
    # AwesomeClassWithGenerics.static_field and AwesomeClassWithGenerics().static_field are different
    # It's not possible to access static field via class instance variable
    
    def __init__(self, arg: T) -> None:
        self._property: T = arg 

    @staticmethod
    def some_static_method(arg: List[T]):
        ...

    @property
    def property(self) -> bool:
        return not self._property
```


