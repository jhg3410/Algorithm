class Solution {
    val answer = mutableListOf<IntArray>()


    fun solution(n: Int): Array<IntArray> {
        moveHanoi(count = n, start = 1, tmp = 2, end = 3)
        return answer.toTypedArray()
    }


    private fun moveHanoi(count: Int, start: Int, tmp: Int, end: Int) {
        if (count == 1) {
            answer.add(intArrayOf(start, end))
            return
        }
        moveHanoi(count - 1, start, end, tmp)
        moveHanoi(1, start, tmp, end)
        moveHanoi(count - 1, tmp, start, end)
    }
}