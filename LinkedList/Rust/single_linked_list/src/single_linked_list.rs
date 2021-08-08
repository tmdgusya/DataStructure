pub struct Node<T> {
    pub data: T,
    pub next: Option<Box<Node<T>>>
}

pub struct SingleLinkedList<T> {
    pub head: Option<Node<T>>
}

impl<T> SingleLinkedList<T> {
    

}