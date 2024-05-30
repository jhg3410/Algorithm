package heejik.`65week`

import java.io.BufferedReader
import java.io.InputStreamReader

private class 사과나무 {

    fun solve() = with(BufferedReader(InputStreamReader(System.`in`))) {
        val n = this.readLine().toInt()
        val appleCounts = readLine().split(' ').map { it.toInt() } as MutableList
        val appleSum = appleCounts.sum()
        var count1 = 0
        var count2 = 0

        if (appleSum % 3 != 0) {
            println("NO")
            return
        }

        for (apple in appleCounts) {
            count2 += apple / 2
            count1 += apple % 2
        }

        if (count2 >= count1) {
            println("YES")
        } else {
            println("NO")
        }
    }
}

fun main() {
    사과나무().solve()
}