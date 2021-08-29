package dodo

const DEFAULT_SIZE int = 10

type Heap struct {
	arr   []int
	size  int
	count int
}

func HeapConstructor() Heap {
	return Heap{arr: []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, size: DEFAULT_SIZE, count: 0}
}

func (h *Heap) GetElements() []int {
	return h.arr[:]
}
func (h *Heap) UpHeapify(data int) {
	if h.isFull() {
		h.grow()
	}

	h.upCount()
	insertIndex := h.count

	for insertIndex != 1 && h.isBiggerThanParent(insertIndex, data) {
		h.arr[insertIndex] = h.arr[getParentIndex(insertIndex)]
		insertIndex = getParentIndex(insertIndex)
	}
	h.arr[insertIndex] = data
}

func (h *Heap) grow() {
	growSize := DEFAULT_SIZE + h.size
	newHeap := make([]int, growSize)
	for index, value := range h.arr {
		newHeap[index] = value
	}
	h.arr = newHeap
	h.size = growSize
}

func (h *Heap) isBiggerThanParent(index int, data int) bool {
	return data > h.arr[getParentIndex(index)]
}

func (h *Heap) upCount() {
	h.count++
}

func (h *Heap) minusCount() {
	h.count--
}

func (h *Heap) isEmpty() bool {
	return h.count <= 0
}

func (h *Heap) isFull() bool {
	return h.count >= h.size-1
}

func getParentIndex(index int) int {
	return index / 2
}

func getLeftChildFrom(parentIndex int) int {
	return parentIndex * 2
}

func getRightChildFrom(parentIndex int) int {
	return (parentIndex * 2) + 1
}
