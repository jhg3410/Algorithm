package heejik.`54week`

class 우체국 {

    fun solve() {
        val n = readln().toInt()
        val populations: MutableList<Pair<Long, Long>> = mutableListOf()
        var s = 0L
        var allSum = 0L
        repeat(n) {
            val (x, a) = readln().split(' ').map { it.toLong() }
            populations.add(x to a)
            allSum += a
        }

        populations.sortedBy { it.first }.forEach {
            s += it.second
            if (s >= allSum - s) {
                println(it.first)
                return
            }
        }
    }
}

fun main() {
    우체국().solve()
}