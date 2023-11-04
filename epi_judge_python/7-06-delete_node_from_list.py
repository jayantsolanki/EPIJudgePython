import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
WAP which deletes a node in a singly linked list. The input node is guaranteed not to be the tail node.
Logic:
Instead of deleting the node, you can delete its successor and still achieve the desired configuration by 
overwriting the successor's data into the given node.
Time: O(1)
"""
# Assumes node_to_delete is not tail.
def deletion_from_list(node_to_delete: ListNode) -> None:

    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next

@enable_executor_hook
def deletion_from_list_wrapper(executor, head, node_to_delete_idx):
    node_to_delete = head
    if node_to_delete is None:
        raise RuntimeError('List is empty')
    for _ in range(node_to_delete_idx):
        if node_to_delete.next is None:
            raise RuntimeError('Can\'t delete last node')
        node_to_delete = node_to_delete.next

    executor.run(functools.partial(deletion_from_list, node_to_delete))

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('7-06-delete_node_from_list.py',
                                       'delete_node_from_list.tsv',
                                       deletion_from_list_wrapper))
