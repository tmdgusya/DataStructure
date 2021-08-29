package dodo

type node struct {
	data int
}

func CreateNode(data int) node {
	return node{data: data}
}
