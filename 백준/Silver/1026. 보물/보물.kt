package heejik.`4week`

fun main() {
    val n = readln().toInt()

    var s = 0

    val a = readln().split(' ').map { it.toInt() }.sorted()
    val b = readln().split(' ').map { it.toInt() }.sortedDescending()

    a.forEachIndexed { index, i ->
        s += a[index] * b[index]
    }

    println(s)
}