import kotlin.math.sqrt

class Solution {
    fun solution(n: Int, k: Int): Int {
        var answerCount = 0

        n.changeToKNumber(k).split('0').forEach {
            it.toLongOrNull()?.let {
                if (it.isPrimeNumber()) answerCount++
            }
        }

        return answerCount
    }


    private fun Int.changeToKNumber(k: Int): String {
        var tmp = this
        val sb = StringBuilder()

        while (tmp >= k) {
            sb.insert(0, tmp % k)
            tmp /= k
        }
        sb.insert(0, tmp)
        return sb.toString()
    }

    private fun Long.isPrimeNumber(): Boolean {


        if (this == 1L) return false
        if (this == 2L) return true
        if (this % 2 == 0.toLong()) return false

        for (i in 3..sqrt(this.toDouble()).toInt()) {
            if (this % i == 0.toLong()) return false
        }

        return true
    }
}