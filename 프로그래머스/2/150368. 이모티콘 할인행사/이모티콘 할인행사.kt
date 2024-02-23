class Solution {
    private lateinit var emoticons: IntArray
    private lateinit var users: Array<IntArray>
    var answer = 0 to 0

    fun solution(users: Array<IntArray>, emoticons: IntArray): IntArray {
        this.users = users
        this.emoticons = emoticons

        findDiscounts(discounts = mutableListOf(), counts = emoticons.size)
        return answer.run { intArrayOf(first, second) }
    }


    private fun findDiscounts(discounts: MutableList<Int>, counts: Int) {
        if (discounts.size == counts) {
            getResult(discounts).run {
                if (first > answer.first) answer = this
                else if (first == answer.first && second > answer.second) answer = this
            }
            return
        }

        for (discountRate in 10..40 step 10) {
            discounts.add(discountRate)
            findDiscounts(discounts = discounts, counts = counts)
            discounts.removeLast()
        }
    }

    private fun getResult(discounts: List<Int>): Pair<Int, Int> {
        var plusUserCount = 0
        var sellMoney = 0

        users.forEach {
            var buyMoney = 0
            val (discount, money) = it
            for ((idx, value) in emoticons.withIndex()) {
                if (discounts[idx] >= discount) {
                    val discountedValue = (value / 100) * (100 - discounts[idx])
                    buyMoney += discountedValue
                }
            }
            if (buyMoney >= money) plusUserCount++
            else sellMoney += buyMoney
        }

        return plusUserCount to sellMoney
    }
}