class Solution {
    val visited = BooleanArray(size = 1_000_001) { false }
    fun solution(x: Int, y: Int, n: Int): Int {
        
        val queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(x to 0)
        visited[x] = true
        while (queue.isNotEmpty()) {
            val (number, count) = queue.removeFirst()
            if (number == y) {
                return count
            }
            
            if (number + n <= y && visited[number + n].not()) {
                queue.add(number + n to count + 1)
                visited[number + n] = true
            }
            if (number * 2 <= y && visited[number *2].not()) {
                queue.add(number *2 to count + 1)
                visited[number *2] = true
            }
            if (number * 3 <= y && visited[number * 3].not()) {
                queue.add(number  * 3 to count + 1)
                visited[number * 3] = true
            }
        }
        
        return -1
    }
}