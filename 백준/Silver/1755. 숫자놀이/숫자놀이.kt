import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    val li = arrayListOf<Int>()

    val (m, n) = readln().split(' ').map { it.toInt() }

    li.apply {
        addAll(m .. n)
        sortBy {
            it.toString().map { chr -> dic[chr.digitToInt()] }.joinToString(" ")
        }
    }

    li.forEachIndexed { index, i ->
        print("$i ")
        if ((index+1) % 10 == 0) println()
    }

}

val dic = mutableMapOf<Int, String>(
    1 to "one",
    2 to "two",
    3 to "three",
    4 to "four",
    5 to "five",
    6 to "six",
    7 to "seven",
    8 to "eight",
    9 to "nine",
    0 to "zero",
)