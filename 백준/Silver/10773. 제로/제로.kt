import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val stack = Stack<Int>()
    repeat(readln().toInt()) {
        when (val num = readln().toInt()) {
            0 -> {
                stack.pop()
            }
            else -> {
                stack.push(num)
            }
        }
    }
    println(stack.sum())
}