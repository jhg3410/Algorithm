class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        var answer = intArrayOf()
        val genresMap = genres.indices.groupBy { genres[it] }
        
        genresMap.toList().sortedByDescending { it.second.sumOf { plays[it] } }.forEach first@{
            it.second.sortedByDescending { plays[it] }.forEachIndexed { idx, id ->
                answer += id
                if (idx == 1) return@first
            }
        }

        return answer
    }
}