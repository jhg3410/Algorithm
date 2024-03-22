package heejik.`55week`

import kotlin.math.min

class `사다리 조작` {

    var n = 0
    var m = 0
    var h = 0
//    private val lines = mutableListOf<Pair<Int, Int>>()
    private var minCount = Int.MAX_VALUE
    lateinit var visited: List<BooleanArray>

    fun solve() {
        readln().split(' ').map { it.toInt() }.run {
            n = this[0]
            m = this[1]
            h = this[2]
        }
        visited = List(size = h) { BooleanArray(size = n) }

        repeat(m) {
            val (x, y) = readln().split(' ').map { it.toInt() - 1 }
//            lines.add(x to y)
            visited[x][y] = true
        }

        drawLine(count = 0, 0, 0)
        println(with(minCount) {
            if (this == Int.MAX_VALUE) -1 else this
        })
    }

    private fun drawLine(count: Int, x: Int, y: Int) {
        if (count > 3) return
        if (search()) {
            minCount = min(minCount, count)
            return
        }

        for (i in x until h) {
            for (j in 0 until n - 1) {
                if (i == x && j <= y && (i != 0 && j != 0)) continue
                val preDraw = if (j-1 < 0) false else visited[i][j-1]
                if (visited[i][j].not() && preDraw.not() && visited[i][j+1].not()) {
                    visited[i][j] = true
                    drawLine(count = count + 1, i, j)
                    visited[i][j] = false
                }
            }
        }
    }

    private fun search(): Boolean {
        var sameCount = 0
        for (start in 0 until n) { // 기준 선
            var row = 0
            var now = start
            while (row != h) {
                val preLine = if (now -1 < 0) false else visited[row][now-1]
                if (visited[row][now]) {
                    now++
                } else if (preLine) {
                    now--
                }
                row++
            }
            if (now == start) {
                sameCount++
            }
        }
        if (sameCount == n) return true
        return false
    }
}


fun main() {
    `사다리 조작`().solve()
}