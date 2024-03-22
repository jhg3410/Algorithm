class Solution {    
    fun solution(n: Int, costs: Array<IntArray>): Int {
        var answer = 0
        val relations = List(size = n) { MutableList(size = n) { -1 } }
        costs.forEach {
            val (x, y, cost) = it
            relations[x][y] = cost
            relations[y][x] = cost
        }
        
        val visited = mutableListOf(0)
        while (visited.size != n) {
            var minCost = Int.MAX_VALUE
            var nextNode = -1

            visited.forEach { visit ->
                (0 until n).filter { it !in visited && relations[visit][it] != -1 }.forEach {
                    if (relations[visit][it] < minCost) {
                        minCost = relations[visit][it]
                        nextNode = it
                    }
                }
            }

            visited.add(nextNode)
            answer += minCost
        }
        
        
        return answer
    }
}
