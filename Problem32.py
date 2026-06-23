def link(head):
    current=head
    length=0
    while current is not None:
        length+=1
        current=current.next
        
    num=length//2
    for i in range(num):
        current=current.next
    return current