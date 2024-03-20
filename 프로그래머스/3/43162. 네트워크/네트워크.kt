class Solution {
    private fun find(x: Int, parents: MutableList<Int>): Int {
        if (x == parents[x]) return x
        return find(parents[x], parents)
    }
    
    private fun union(x: Int, y: Int, parents: MutableList<Int>) {
        val a = find(x, parents)
        val b = find(y, parents)
        
        if (a < b) {
            parents[b] = a
        } else {
            parents[a] = b
        }
    }
    
    fun solution(n: Int, computers: Array<IntArray>): Int {
        val parents = MutableList(size = n) { it }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i != j && computers[i][j] == 1) {
                    union(i, j, parents)
                }
            }
        }
        val answers = mutableSetOf<Int>()
        for (i in 0 until n) {
            answers.add(find(i, parents))
        }
        
        return answers.size
    }
}