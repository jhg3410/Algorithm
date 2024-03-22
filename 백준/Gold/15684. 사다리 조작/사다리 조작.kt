package heejik.`55week`

class `사다리 조작` {

    var n = 0
    var m = 0
    var h = 0
    private var minCount = -1
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
            visited[x][y] = true
        }

        for (i in 0..3) {
            drawLine(count = 0, 0, 0, max = i)
            if (minCount == i) {
                println(i)
                return
            }
        }

        println(-1)
    }

    private fun drawLine(count: Int, x: Int, y: Int, max: Int) {
        if (count == max) {
            if (search()) {
                minCount = max
            }
            return
        }

        for (i in x until h) {
            for (j in 0 until n - 1) {
                if (i == x && j <= y && (i != 0 && j != 0)) continue
                val preDraw = if (j - 1 < 0) false else visited[i][j - 1]
                if (visited[i][j].not() && preDraw.not() && visited[i][j + 1].not()) {
                    visited[i][j] = true
                    drawLine(count = count + 1, i, j, max)
                    visited[i][j] = false
                }
            }
        }
    }

    private fun search(): Boolean {
        for (start in 0 until n) { // 기준 선
            var now = start
            for (row in 0 until h) {
                val preLine = if (now - 1 < 0) false else visited[row][now - 1]
                if (visited[row][now]) {
                    now++
                } else if (preLine) {
                    now--
                }
            }
            if (now != start) {
                return false
            }
        }
        return true
    }
}


fun main() {
    `사다리 조작`().solve()
}