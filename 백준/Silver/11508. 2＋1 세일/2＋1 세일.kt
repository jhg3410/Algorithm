import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    val n = readln().toInt()
    val drink = arrayListOf<Int>()

    repeat(n){
        drink.add(readln().toInt())
    }

    println(drink.sortedDescending().run {
        this.filterIndexed { index, i ->   (index+1) % 3 != 0}
    }.sum())
}