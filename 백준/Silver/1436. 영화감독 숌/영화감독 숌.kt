import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readln().toInt()
    var start = 666
    while (n != 0){
        if (isMovie(start.toString())) n -= 1
        start += 1
    }
    println(start-1)
}

fun isMovie(num:String): Boolean {
    return num.contains("666")
}