class Solution {
    fun solution(orogin_scores: Array<IntArray>): Int {
        val wanhoScore = orogin_scores.first().sum()

        val scores = orogin_scores.sortedWith(compareBy( { -it.first() }, { it[1] }))
        
        var maxScore2 = 0
        var answer = 1
        for ((score1, score2) in scores) {
            if (orogin_scores[0][0] < score1 && orogin_scores[0][1] < score2) {
                return -1
            }
            if (score2 < maxScore2) continue
            if (wanhoScore < score1 + score2) {
                answer += 1
            }
            maxScore2 = score2
        }
        
        return answer
    }
}