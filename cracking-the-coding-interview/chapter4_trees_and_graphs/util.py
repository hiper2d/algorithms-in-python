from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.left: Optional[TreeNode[T]]
        self.right: Optional[TreeNode[T]]
