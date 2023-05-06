data class Answer(
    var start: Int,
    var end: Int
) {
    fun toMutableList(): MutableList<Int> {
        return mutableListOf(this.start,this.end)
    }
}

class Solution {
    fun solution(sequence: IntArray, k: Int): MutableList<Int> {
        var start = 0
        var end = 0
        var nowSum = sequence[end]
        val answer = Answer(0, Int.MAX_VALUE)

        while (true) {
            if (nowSum == k) {
                if (end - start < answer.end - answer.start) {
                    answer.start = start
                    answer.end = end
                } else if (end - start == answer.end - answer.start) {
                    if (start < answer.start) {
                        answer.start = start
                        answer.end = end
                    }
                }
            }

            if (nowSum <= k) {
                end += 1
                if (end == sequence.size) {
                    break
                }
                nowSum += sequence[end]
            } else {
                nowSum -= sequence[start]
                start += 1
                if (start == sequence.size) {
                    break
                }
            }
        }
        return answer.toMutableList()
    }
}