import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    var answer = 0
    repeat(readln().toInt()) {
        if (isGroupWord(readln())) answer += 1
    }
    println(answer)
}

fun isGroupWord(word: String) : Boolean {
    val tmp = arrayListOf<Char>()
    word.forEach {
        if (tmp.isEmpty()) tmp.add(it)
        if (it == tmp.last()) return@forEach
        else if (tmp.contains(it)) return false
        else tmp.add(it)
    }
    return true
}