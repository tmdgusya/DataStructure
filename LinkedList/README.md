# Linked List

**Linked List 란 그들의 메모리 주소값으로 연결되는 선형적인 데이터 collection** 이라고 할 수 있습니다.
그러므로 모든 Node 는 next position 을 가집니다.
대부분 data 와 nextnode 의 reference 를 가집니다. Node 를 python code 로 표현하면 아래와 같습니다.

```python
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
```

LinkedList 는 여러가지 자료구조 형태가 있습니다 **SingleLinkedList, Doubly Linked List 등등 Queue 를 구현하는 자료구조로 이용**되기도 합니다.
LinkedList 는 **선형적인 구조를 지니고 있으므로, 탐색 및 추가 및 제거에 O(n) Time Complexity** 를 가집니다.

**LinkedList 의 장점은 표준 array 에 비해서 쉽게 데이터를 추가하거나 삭제할 수 있다는 것**입니다. 만약 array 의 size 를 키우려면, 아예 **데이터 구조를 다시 복사해서 더큰 배열로 복제하는 식의 형태가 이뤄져야 할 것**입니다. 왜냐하면 **Array 의 원소들이 인접한 지역에 위치하는 특성**이 있기 때문입니다. 하지만 **LinkedList 는 메모리상에서 인접한 지역에 Node 들이 존재할 필요가 없으므로, 쉽게 추가하거나 삭제**할 수 있습니다.하지만 이로 인해 얻는 단점도 있습니다. 언제나 TradeOff 가 존재하듯이.

## Linked List Basic Concept

- **Linked List 자료구조 안의 원소들은 element 혹은 Node 로 명명**합니다.
- 안의 Node 또는 element 들은 **next_node 의 link 인 next_pointer 또는 next_link 를 가져야 합니다.** 노드가 지니고 있는 **데이터 필드는 data, cargo, information, value, payload 등등 으로 명명**할 수 있습니다.
- **head 는 LinkedList 의 첫번째 노드**를 나타냅니다.
- **tail 은 LinkedList 의 종단 노드**를 나타냅니다.

### Singly Linked List

**단일 연결 리스트(Singly Linked List)**안의 Node 는 **data 와 next filed 를 가집니다.**

[Python Singly Linked List](https://github.com/tmdgusya/DataStructure/tree/master/LinkedList/Python)

**INSERT OR DELETE TIME COMPLEXITY**

![image](https://user-images.githubusercontent.com/57784077/128628593-80f32b4c-f5c6-48a6-a915-e979625491f4.png)

- INSERT 나 DELETE 를 시도할때, **결국 head 부터 시작해서 원하는 위치에 넣어야 하므로 O(N) 번 탐색이 일어난 뒤, 추가하거나 삭제**한다.
