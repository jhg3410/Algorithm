class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        var answer = intArrayOf()
        val genresMap = mutableMapOf<String, MutableList<Int>>()

        for ((idx, genre) in genres.withIndex()) {
            if (genre !in genresMap) genresMap[genre] = mutableListOf()
            genresMap[genre]?.add(idx)
        }
        genresMap.toList().sortedByDescending { it.second.sumOf { plays[it] } }.forEach first@ {
            var count = 0
            it.second.sortedByDescending { plays[it] }.forEach second@ {
                count++
                answer += it
                if (count == 2) return@first
            }
        }

        return answer
    }
}