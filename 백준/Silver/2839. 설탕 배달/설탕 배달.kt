import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readln().toInt()
    var cnt = 0
    while (n > 0) {
        if (n % 5 == 0) {
            cnt += n / 5
            n = 0
        } else {
            cnt += 1
            n -= 3
        }
    }
    println(if (n == 0) cnt else -1)
}
