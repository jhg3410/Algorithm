import kotlin.math.sqrt


class Solution {
    fun solution(n: Int, k: Int): Int {

        return changeToNumber(number = n, k = k).split('0').count {
            (it.isNotEmpty() && isPrime(it.toLong()))
        }
    }

    private fun changeToNumber(number: Int, k: Int): String {
        return number.toString(k)
    }

    private fun isPrime(number: Long): Boolean {
        if (number == 1L) return false
        if (number == 2L) return true
        for (i in 2..sqrt(number.toDouble()).toInt() + 1) {
            if (number % i == 0L) return false
        }
        return true
    }
}