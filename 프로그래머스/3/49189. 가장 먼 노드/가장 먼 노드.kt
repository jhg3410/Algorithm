import kotlin.math.max

class Solution {
    val distances = MutableList<Int>(size = 20001) { -1 }
    var maxDistance = 0
    val relations = MutableList(20001) { BooleanArray(20001) }
    fun solution(n: Int, edge: Array<IntArray>): Int {
        edge.forEach {
            val (x, y) = it
            relations[x][y] = true
            relations[y][x] = true
        }
        bfs()

        return distances.count { it == maxDistance }
    }
    
    private fun bfs() {
        val queue = ArrayDeque<Int>()
        queue.add(1)
        distances[1] = 0
        
        while(queue.isNotEmpty()) {
            val now = queue.removeFirst()
            relations[now].forEachIndexed { idx, b ->
                if (b && distances[idx] == -1) {
                    distances[idx] = distances[now] + 1
                    queue.add(idx)
                    maxDistance = max(maxDistance, distances[idx])
                }
            }
        }
    }
}





