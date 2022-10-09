package heejik.`4week`

import java.util.Collections.min


var n: Int = 0
val li = arrayListOf<MutableList<Int>>()
val score_li = arrayListOf<Int>()

fun main() {

    n = readln().toInt()
    repeat(n) {
        li.add(readln().split(' ').map { it.toInt() }.toMutableList())
    }
    li.forEachIndexed { x, ints ->
        ints.forEachIndexed { y, i ->
            if (i != 0) {
                solve(x, x, y, mutableListOf(y), i)
            }
        }
    }
    println(min(score_li))
}

fun solve(start: Int, from: Int, to: Int, city: MutableList<Int>, score: Int, cnt: Int = 2) {
    if (cnt == n) {
        if (li[to][start] != 0 ) {
            score_li.add(score + li[to][start])
        }
        return
    }

    for (i in 0 until n) {
        if (i !in city && i != from && i != start && li[to][i] != 0) {
            solve(start, to ,i, city.plus(i).toMutableList(), score + li[to][i], cnt + 1)
        }
    }
}