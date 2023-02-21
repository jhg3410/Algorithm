package heejik.`17week`

class `트리 순회` {

    data class Node(
        val name: String,
        var leftNode: Node? = null,
        var rightNode: Node? = null,
    ) {
        fun searchAndGetChild(node: Node) {
            if (this.name == node.name) {
                this.leftNode = node.leftNode
                this.rightNode = node.rightNode
                return
            }

            leftNode?.searchAndGetChild(node)
            rightNode?.searchAndGetChild(node)
        }
    }

    data class Tree(
        val root: Node
    ) {
        fun add(node: Node) {
            root.searchAndGetChild(node)
        }

        fun preOrder(node: Node) {
            print(node.name)
            node.leftNode?.let {
                preOrder(it)
            }
            node.rightNode?.let {
                preOrder(it)
            }
        }

        fun inOrder(node: Node) {
            node.leftNode?.let {
                inOrder(it)
            }
            print(node.name)
            node.rightNode?.let {
                inOrder(it)
            }
        }

        fun postOrder(node:Node) {
            node.leftNode?.let {
                postOrder(it)
            }
            node.rightNode?.let {
                postOrder(it)
            }
            print(node.name)
        }
    }

    private val tree = Tree(root = Node(name = "A"))

    fun solve() {
        setting()
        traverse()
    }

    private fun setting() {
        repeat(readln().toInt()) {
            readln().split(' ').run {
                tree.add(
                    node = Node(
                        name = this[0],
                        leftNode = if (this[1] == ".") null else Node(this[1]),
                        rightNode = if (this[2] == ".") null else Node(this[2])
                    )
                )
            }
        }
    }

    private fun traverse() {
        tree.run {
            preOrder(root).also { println() }
            inOrder(root).also { println() }
            postOrder(root).also { println() }
        }
    }
}

fun main() {
    `트리 순회`().solve()
}