class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        var answer = ""
        val filteredAlpha = ('a'..'z').filter { it !in skip }

        s.forEach {
            val idx = (filteredAlpha.indexOf(it) + index) % filteredAlpha.size
            answer += filteredAlpha[idx]
        }

        return answer
    }
}