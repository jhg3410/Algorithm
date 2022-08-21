import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    var word = readln()
    croatia.forEach {
        if (word.contains(it)) {
            word = word.replace(it, "0")
        }
    }
    println(word.length)
}


val croatia = listOf<String>("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")