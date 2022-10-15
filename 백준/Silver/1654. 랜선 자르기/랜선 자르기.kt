package heejik.`5week`

import kotlin.system.exitProcess

val lines = mutableListOf<Long>()

fun main() {

    var answer = 0L
    val (k, n) = readln().split(' ').map { it.toInt() }
    var s = 0L

    repeat(k) {
        val line = readln().toLong()
        lines.add(line)
        s += line
    }

    var start = 0L
    var end = s / n
    if (end == 1L) {
        println(1)
        exitProcess(0)
    }
    while (start <= end) {
        val mid = (end + start) / 2
        val cnt = isCorrect(mid)
        if (cnt >= n) {
            answer = mid
            start = mid + 1
        } else {
            end = mid - 1
        }
    }

    println(answer)
}

fun isCorrect(length: Long): Long {
    var cnt = 0L
    lines.forEach {
        cnt += it / length
    }
    return cnt
}