from typing import Generic, TypeVar, List
T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self):
        self._container: List[T] = []

    def push(self, val: T):
        self._container.append(val)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


if __name__ == "__main__":
    stack_a: Stack[int] = Stack()
    stack_b: Stack[int] = Stack()
    stack_c: Stack[int] = Stack()
    stack_a.push(3)
    stack_a.push(2)
    stack_a.push(1)
    print(stack_a)
    hanoi(stack_a, stack_c, stack_b, 3)
    print(stack_a)
    print(stack_b)
    print(stack_c)
