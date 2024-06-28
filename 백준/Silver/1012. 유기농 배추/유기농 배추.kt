import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
val bw = BufferedWriter(OutputStreamWriter(System.`out`))
fun readln() = br.readLine()

val dx = listOf(1,-1,0,0)
val dy = listOf(0,0,1,-1)

lateinit var board: List<BooleanArray>

@kotlin.ExperimentalStdlibApi
private fun solve() {
    var needWormCount = 0
    val (n, m, k) = readln().split(" ").map { it.toInt() }
    board = List(size = n) { BooleanArray(size = m) { false } }

    repeat(k) {
        val (x, y) = readln().split(" ").map { it.toInt() }
        board[x][y] = true
    }

    for (i in 0 until n) {
        for (j in 0 until m) {
            if (board[i][j]) {
                spreadWorm(x = i, y = j, n = n, m = m)
                needWormCount += 1
            }
        }
    }

    bw.write("$needWormCount\n")
}

@kotlin.ExperimentalStdlibApi
fun spreadWorm(x: Int, y: Int, n: Int, m: Int) {
    val deque = ArrayDeque<Pair<Int, Int>>()
    deque.add(x to y)

    while (deque.isNotEmpty()) {
        val (currentX, currentY) = deque.removeFirst()
        repeat(4) { i ->
            val nx = currentX + dx[i]
            val ny = currentY + dy[i]
            if (nx !in 0 until n || ny !in 0 until m) return@repeat
            if (board[nx][ny] == false) return@repeat
            board[nx][ny] = false
            deque.add(nx to ny)
        }
    }
}


@kotlin.ExperimentalStdlibApi
fun main() {
    val t = readln().toInt()
    repeat(t) {
        solve()
    }

    bw.flush()
    bw.close()
    br.close()
}