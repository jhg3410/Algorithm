import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val li = ArrayList<Pair<String, List<Int>>>()

    repeat(readln().toInt()) {
        val (name, korean, english, math) = readln().split(" ")
        li.add(Pair(name, mutableListOf(korean, english, math).map { it.toInt() }))
    }
    li.sortedWith(
        compareBy(
            { -(it.second[0]) },
            { it.second[1] },
            { -(it.second[2]) },
            { it.first }
        )
    ).forEach { println(it.first) }
}