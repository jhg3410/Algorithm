import java.io.BufferedReader
import java.io.InputStreamReader

fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val a = readln()
    val b = readln()
    var s = ""
    repeat(a.length) {
        s += a[it] + b[it].toString()
    }
    while (s.length != 2) {
        var tmp = ""
        for (i in 0..s.length-2) {
            tmp += (s[i].digitToInt() + s[i+1].digitToInt()).toString().last()
        }
        s = tmp
    }
    println(s)
}