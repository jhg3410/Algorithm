import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.Collections.max


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val map = mutableMapOf<String,Int>()
    repeat(readln().toInt()){
        val book = readln()
        if (map.containsKey(book)) map[book] = map[book]!! + 1
        else map[book] = 0
    }
    println(map.filterValues {
        it == max(map.values)
    }.keys.minOf { it })
}