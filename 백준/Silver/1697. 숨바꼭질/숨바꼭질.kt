package heejik.`19week`

import kotlin.properties.Delegates

class 숨바꼭질 {

    var n by Delegates.notNull<Int>()
    var k by Delegates.notNull<Int>()
    val queue = ArrayDeque<Int>()
    private val timesByDistance = MutableList(100001) { Int.MAX_VALUE }
    fun solve() {
        readln().split(' ').map { it.toInt() }.run {
            n = first()
            k = last()
        }

        timesByDistance[n] = 0
        queue.addFirst(n)
        bfs()
        println(timesByDistance[k])
    }

    private fun bfs() {
        while (queue.isNotEmpty()) {
            val distance = queue.removeFirst()
            val preTime = timesByDistance[distance]
            if (distance > k && timesByDistance[distance - 1] == Int.MAX_VALUE) {
                queue.add(distance - 1)    // 후진
                timesByDistance[distance - 1] = preTime + 1
            } else {
                if (distance - 1 in 0 until timesByDistance.size && timesByDistance[distance - 1] == Int.MAX_VALUE) {
                    queue.add(distance - 1)    // 후진
                    timesByDistance[distance - 1] = preTime + 1
                }
                if (distance + 1 in 0 until timesByDistance.size && timesByDistance[distance + 1] == Int.MAX_VALUE) {
                    queue.add(distance + 1)    // 전진
                    timesByDistance[distance + 1] = preTime + 1
                }
                if (distance * 2 in 0 until timesByDistance.size && timesByDistance[distance * 2] == Int.MAX_VALUE) {
                    queue.add(distance * 2)    // 텔포
                    timesByDistance[distance * 2] = preTime + 1
                }
            }
        }
    }
}

fun main() {
    숨바꼭질().solve()
}