class Solution {
    fun solution(n: Int, m: Int, section: IntArray): Int {
        var answer = 0
        val area = BooleanArray(n) { it + 1 !in section }

        repeat(n) { stand ->
            if (area[stand].not()) {
                repeat(m) { rise ->
                    area[(stand + rise).coerceAtMost(n - 1)] = true
                }

                answer++
            }
        }

        return answer
    }
}