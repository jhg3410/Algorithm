import java.io.BufferedReader
import java.io.InputStreamReader

fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val word = readln().uppercase()
    val wordMap = mutableMapOf<Char, Int>()
    word.forEach {
        wordMap[it] = wordMap[it].run {
            this?.plus(1) ?: 1
        }
    }
    wordMap.filter {
        it.value == wordMap.maxOf { m -> m.value }
    }.apply {
        if (this.count() > 1) println('?')
        else println(this.keys.first())
    }

}