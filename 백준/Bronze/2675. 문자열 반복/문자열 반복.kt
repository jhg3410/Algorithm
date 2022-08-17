import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readln().toInt()
    repeat(t) {
        val (R, S) = readln().split(' ')
        S.forEach { chr -> repeat(R.toInt()) { print(chr) } }.apply {
            println()
        }
    }
}