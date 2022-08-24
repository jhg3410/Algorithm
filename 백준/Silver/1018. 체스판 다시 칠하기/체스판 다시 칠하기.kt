import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (n, m) = readln().split(' ').map { it.toInt() }

    var answer = 10000
    val li = arrayListOf<String>().apply {
        repeat(n) {
            add(readln())
        }
    }

    for (i in 0..(n - 8)) {
        for (j in 0..(m - 8)) {
            answer = min(answer, findCntOfPaint(li.subList(0 + i, 8 + i).map {
                it.substring(j, j + 8)
            }))
        }
    }

    println(if (answer == 10000) 0 else answer)
}

fun findCntOfPaint(li: List<String>): Int {
    val cnt = IntArray(2) { 0 }
    for (i in 0..7) {
        for (j in 0..7) {
            if (one[i][j] != li[i][j]) {
                cnt[0] += 1
            }
            if (two[i][j] != li[i][j]) {
                cnt[1] += 1
            }
        }
    }
    return min(cnt.first(),cnt.last())
}

val one = arrayListOf<String>(
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
)
val two = arrayListOf<String>(
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
)