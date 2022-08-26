import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    var doc = readln()
    val word = readln()
    var cnt = 0

    while (doc.contains(word)){
        doc = doc.substringAfter(word)
        cnt += 1
    }

    println(cnt)
}