import kotlin.math.max

data class GiftInfo(
    val sends: MutableList<String> = mutableListOf(),
    val receives: MutableList<String> = mutableListOf()
) {
    val score
        get() = sends.count() - receives.count()
}

class Solution {
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val giftHistories = mutableMapOf<String, GiftInfo>()
        var answer: Int = 0

        friends.forEach {
            giftHistories[it] = GiftInfo()
        }

        gifts.forEach {
            val (send, receive) = it.split(' ')
            giftHistories[send]!!.sends.add(receive)
            giftHistories[receive]!!.receives.add(send)
        }
        giftHistories.forEach {
            val me = it.key
            var nowReceiveCount = 0
            giftHistories.filter { it.key != me }.forEach { friend ->
                val sendCount = it.value.sends.count { it == friend.key }
                val receiveCount = it.value.receives.count { it == friend.key }
                if (sendCount > receiveCount) nowReceiveCount++
                if (receiveCount == sendCount && it.value.score > friend.value.score) nowReceiveCount++
            }
            answer = max(answer, nowReceiveCount)
        }
        return answer
    }
}