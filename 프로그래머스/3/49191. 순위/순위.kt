class Solution {
    data class Result(
        val winner: Int,
        val loser: Int
    )

    private fun IntArray.toResult() = Result(this.first() - 1, this.last() - 1)

    fun solution(n: Int, results: Array<IntArray>):Int {
        var answer = 0
        val wins = List(n) { mutableSetOf<Int>() }
        val loses = List(n) { mutableSetOf<Int>() }

        // win
        results.map { it.toResult() }.forEach { result ->
            wins[result.winner].add(result.loser)
            wins[result.winner].addAll(wins[result.loser])

            wins.filter { result.winner in it }.forEach {
                it.addAll(wins[result.winner])
            }
        }

        // lose
        results.map { it.toResult() }.forEach { result ->
            loses[result.loser].add(result.winner)
            loses[result.loser].addAll(loses[result.winner])

            loses.filter { result.loser in it }.forEach {
                it.addAll(loses[result.loser])
            }
        }

        repeat(n) { idx ->
            if (wins[idx].size + loses[idx].size == n - 1) answer++
        }

        return answer
    }
}