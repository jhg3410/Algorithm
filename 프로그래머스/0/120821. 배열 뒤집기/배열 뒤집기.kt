class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in 0 until num_list.size) {
            answer += num_list[num_list.size - 1 - i]
        }
        return answer
    }
}