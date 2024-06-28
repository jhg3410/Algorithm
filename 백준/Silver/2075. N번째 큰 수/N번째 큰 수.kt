import java.io.*
import java.util.PriorityQueue

private val br = BufferedReader(InputStreamReader(System.`in`))
private val bw = BufferedWriter(OutputStreamWriter(System.`out`))
private fun readln() = br.readLine()


fun main() {
    val numbers = PriorityQueue<Int> { number1, number2 ->
        number2 - number1
    }
    
    val n = readln().toInt()
    repeat(n) {
        readln().split(" ").map{ it.toInt() }.forEach { num ->
            numbers.add(num)
        }
    }

    repeat(n-1) {
        numbers.poll()
    }
    println(numbers.poll())
}