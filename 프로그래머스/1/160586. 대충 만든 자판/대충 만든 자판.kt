import kotlin.math.min

class Solution {
    fun solution(keymap: Array<String>, targets: Array<String>): IntArray {
        val answer = mutableListOf<Int>()
        val pressCounts = ('A'..'Z').associateWith { Int.MAX_VALUE }.toMutableMap()

        keymap.forEach {
            for ((idx, alpha) in it.withIndex()) {
                pressCounts[alpha] = min(pressCounts[alpha]!!, idx + 1)
            }
        }

        targets.forEach first@{ target ->
            var count = 0
            target.forEach second@{ alpha ->
                count += pressCounts[alpha]!!.also {
                    if (it == Int.MAX_VALUE) {
                        answer.add(-1)
                        return@first
                    }
                }
            }
            answer.add(count)
        }


        return answer.toIntArray()
    }
}