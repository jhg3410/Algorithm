import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.system.exitProcess

fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val li = arrayListOf<Int>()
    repeat(9){
        li.add(readln().toInt())
    }
    for (i in li.indices){
        for (j in li.indices) {
            if (j == i) continue
            li.filterIndexed { index, q -> index != i && index != j }.apply {
                if (this.sum() == 100){
                    this.sorted().forEach { println(it) }
                    exitProcess(0)
                }
            }
        }
    }
}