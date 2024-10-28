import kotlin.math.*

class Solution {
    fun solution(coin: Int, cards: IntArray): Int {
        val n = cards.size
        var totalRound = 1
        val maxRound = ((n - n/3) / 2) + 1
        val goal = n + 1
        val needRounds = mutableMapOf<Int, MutableSet<Int>>()
        val defaultCards = cards.toList().subList(0, n / 3).toSet()


        for ((idx, card) in cards.withIndex()) {
            val needRound = max(getRound(n = n, idx = idx), getRound(n = n, idx = cards.indexOf(goal - card)))
            if (needRound in needRounds.keys) {
                needRounds[needRound]?.add(card)
                needRounds[needRound]?.add(goal - card)
            } else {
                needRounds[needRound] = mutableSetOf(card, goal - card)
            }
        }
        var remainCoin = coin
        while (true) {
            var minNeedCoin = Int.MAX_VALUE
            var selectCard = -1
            var selectRound = -1
            for (round in 0..totalRound) {
                if (round !in needRounds.keys) continue
                for (card in needRounds[round]!!.toList()) {
                    val needCoin = listOf(card, goal - card).count { it !in defaultCards }
                    if (needCoin < minNeedCoin) {
                        minNeedCoin = needCoin
                        selectCard = card
                        selectRound = round
                    }
                }
            }

            if (remainCoin < minNeedCoin) {
                break
            } else {
                needRounds[selectRound]?.remove(selectCard)
                needRounds[selectRound]?.remove(goal - selectCard)
                remainCoin -= minNeedCoin
            }

            totalRound += 1
        }

        return min(totalRound, maxRound)
    }

    private fun getRound(n: Int, idx: Int): Int {
        if (idx < n / 3) return 0
        return ((idx - (n / 3)) / 2) + 1
    }
}

fun main() {
    Solution().solution(coin = 4, cards = intArrayOf(3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4)).also {
        println(it)
    }
}