
class Node(
    val send: MutableList<Int> = mutableListOf(),
    val receive: MutableList<Int> = mutableListOf()
)

class Solution {
    private val relations = List(size = 1_000_001) { Node() }
    fun solution(edges: Array<IntArray>): IntArray {
        val answer = MutableList(size = 4) { 0 }

        edges.forEach {
            val (send, receive) = it
            relations[send].send.add(receive)
            relations[receive].receive.add(send)
        }
        var mainNode = -1

        // 정점 찾기
        for (number in 1..1_000_000) {
            if (relations[number].send.count() >= 2 && relations[number].receive.isEmpty()) {
                mainNode = number
            }
        }
        answer[0] = mainNode
        visited[mainNode] = true
        // 정점에서 연결한 그래프 탐색
        relations[mainNode].send.forEach { graphNode ->
            val graphType = findGraph(nodeNumber = graphNode)
            if (graphType == -1) return@forEach
            answer[graphType] += 1
        }

        answer[1] = relations[mainNode].send.count() - (answer[2] + answer[3])

        return answer.toIntArray()
    }

    private val visited = BooleanArray(size = 1_000_001)

    private fun findGraph(nodeNumber: Int): Int {
        var graphType = -1

        val queue = ArrayDeque<Int>()
        visited[nodeNumber] = true
        queue.add(nodeNumber)

        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            val sendCount = relations[node].send.count()
            val receiveCount = relations[node].receive.count()
            if (sendCount == 1 && receiveCount == 0) {
                graphType = 2
                break
            }
            if (sendCount == 0 && receiveCount == 1) {
                graphType = 2
                break
            }
            if (sendCount >= 2) {
                graphType = 3
                break
            }
            relations[node].send.forEach {
                if (visited[it]) return@forEach
                visited[it] = true
                queue.add(it)
            }
            relations[node].receive.forEach {
                if (visited[it]) return@forEach
                visited[it] = true
                queue.add(it)
            }
        }

        return graphType
    }
}

