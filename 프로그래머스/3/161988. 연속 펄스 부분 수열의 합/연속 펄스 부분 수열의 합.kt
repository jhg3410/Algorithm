import kotlin.math.*

class Solution {
    fun solution(sequence: IntArray): Long {
        val pers1 = MutableList<Int>(size = sequence.size) { 1 }
        val pers2 = MutableList<Int>(size = sequence.size) { 1 }
        
        for (i in 0 until sequence.size step 2) {
            pers1[i] *= - 1
        }
        for (i in 1 until sequence.size step 2) {
            pers2[i] *= - 1
        }
        var answer = 0L
        var sum1 = 0L
        var sum2 = 0L
        for (i in sequence.indices) {
            sum1 += sequence[i] * pers1[i]
            sum2 += sequence[i] * pers2[i]
            if (sum1 < 0) sum1 = 0
            if (sum2 < 0) sum2 = 0
            answer = max(answer, max(sum1, sum2))
        }
        
        return answer
    }
}