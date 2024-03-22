class Solution {    
    fun solution(n: Int, costs: Array<IntArray>): Int {
        val sortedCosts = costs.sortedBy { it[2] }
        var answer = 0

        val visited = mutableSetOf(0)
            while (visited.size != n) {
                run {
                    sortedCosts.forEach {
                        val (x, y, cost) = it
                        if (x in visited || y in visited) {
                            if (x in visited && y in visited) return@forEach
                            visited.add(x)
                            visited.add(y)
                            answer += cost
                            return@run
                        }
                    }
            }
        }
        return answer
    }
}