import java.util.PriorityQueue

class Solution {
    fun solution(operations: Array<String>): IntArray {
        val maxPQ = PriorityQueue<Int> { a, b -> b - a}
        val minPQ = PriorityQueue<Int> { a, b -> a - b}
        val remain = mutableMapOf<Int, Int>()
        for (operation in operations) {
            when (operation) {
                "D -1" -> {
                    while (minPQ.isNotEmpty()) {
                        val minNumber = minPQ.poll()
                        if (minNumber in remain.keys) {
                            val count = remain[minNumber]!!
                            if (count > 1) {
                                remain[minNumber] = remain[minNumber]!! - 1
                            } else {
                                remain.remove(minNumber)
                            }
                            break
                        }
                    }
                }
                "D 1" -> {
                    while (maxPQ.isNotEmpty()) {
                        val maxNumber = maxPQ.poll()
                        if (maxNumber in remain.keys) {
                            val count = remain[maxNumber]!!
                            if (count > 1) {
                                remain[maxNumber] = remain[maxNumber]!! - 1
                            } else {
                                remain.remove(maxNumber)
                            }
                            break
                        }
                    }
                }
                else -> {
                    val number = operation.removePrefix("I ").toInt()
                    if (number in remain.keys) {
                        remain[number] = remain[number]!! + 1
                    } else {
                        remain[number] = 0
                    }
                    maxPQ.add(number)
                    minPQ.add(number)
                }
            }
        }

        var answerMax = 0
        var answerMin = 0

        while (maxPQ.isNotEmpty()) {
            val maxNumber = maxPQ.poll()
            if (maxNumber in remain.keys) {
                answerMax = maxNumber
                break
            }
        }

        while (minPQ.isNotEmpty()) {
            val minNumber = minPQ.poll()
            if (minNumber in remain.keys) {
                answerMin = minNumber
                break
            }
        }
        return intArrayOf(answerMax, answerMin)
    }
}
