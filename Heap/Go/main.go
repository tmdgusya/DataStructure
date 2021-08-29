package main

import (
	dodo "RoachHeap/heap"
	"fmt"
)

func main() {
	heap := dodo.HeapConstructor()
	heap.UpHeapify(10)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(9)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(11)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(16)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(8)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(7)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(20)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(18)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(100)
	fmt.Println(heap.GetElements())
	heap.UpHeapify(60)
	fmt.Println(heap.GetElements())
}
