class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head: ListNode) -> ListNode:
    
    # Elimina los nodos duplicados en una lista enlazada simple y devuelve la nueva lista.
    
    if not head:
        return None

    current = head
    seen = set([head.val])

    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next

    return head