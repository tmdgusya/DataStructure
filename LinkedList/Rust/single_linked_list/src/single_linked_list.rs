pub struct Node<T> {
    pub data: T,
    pub next: Option<NonNull<Node<T>>>
}

impl<T> Node<T> {
    pub fn new(data: T) -> Node<T> {
        Node { data: data, next: None }
    }
}

pub struct SingleLinkedList<T> {
    pub head: Option<Node<T>>
}

impl<T> SingleLinkedList<T> {
    

}