import kotlin.math.absoluteValue

class Solution {
    fun solution(survey: Array<String>, choices: IntArray): String {
        val types = mutableMapOf<String, Int>()
        "RTCFJMAN".forEach {
            types[it.toString()] = 0
        }

        for ((personality, choice) in survey.zip(choices.toTypedArray())) {
            val (pre, post) = personality.chunked(1)
            val score = (choice - 4).absoluteValue
            if (choice < 4) {
                types[pre] = types[pre]!! + score
            } else {
                types[post] = types[post]!! + score
            }
        }
        
        var answer = ""

        listOf("RT", "CF", "JM", "AN").forEach {
            it.maxByOrNull { type ->
                types[type.toString()]!!
            }.run { answer += this }
        }

        return answer
    }
}
