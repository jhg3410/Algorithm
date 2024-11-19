import java.util.*
class Solution {
    fun solution(operations: Array<String>): IntArray {

        var minHeap = PriorityQueue<Int>(compareBy { it })
        var maxHeap = PriorityQueue<Int>(compareByDescending { it })

        for ((index, value) in operations.withIndex()) {

            var curCmd = value

            var trans = curCmd.split(" ")

            if (trans[0] == "I") {
                //값 삽입
                minHeap.add(trans[1].toInt())
                maxHeap.add(trans[1].toInt())
            } else {
                when {
                    trans[1].equals("1") -> {
                        //최댓값 삭제
                        if (!maxHeap.isEmpty()) {

                            minHeap.remove(maxHeap.peek())

                            maxHeap.poll()


                        }
                    }
                    trans[1].equals("-1") -> {
                        //최솟값 삭제
                        if (!minHeap.isEmpty()) {
                            maxHeap.remove(minHeap.peek())

                            minHeap.poll()
                        }
                    }
                }
            }


        }

        if (minHeap.isEmpty() || maxHeap.isEmpty())
            return intArrayOf(0, 0)


        return intArrayOf(maxHeap.poll(), minHeap.poll())
    }
}