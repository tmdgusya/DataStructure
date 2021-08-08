mod single_linked_list;
use single_linked_list::SingleLinkedList;
use single_linked_list::Node;

fn main() {

}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn create_linked_list_test() {
        let node = Node {data: 10, next: None};
        let linked_list = SingleLinkedList {head: Some(node)};
        assert_eq! (linked_list.head.unwrap().data, 10)
    }


}