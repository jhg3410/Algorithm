class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        var answer = intArrayOf()
        val genresList = genres.indices.groupBy { genres[it] }.toList()

        genresList.sortedByDescending { it.second.sumOf { plays[it] } }.forEach {
            it.second.sortedByDescending { plays[it] }.take(2).forEach { 
                answer += it
            }
        }

        return answer
    }
}