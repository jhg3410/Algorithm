import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    val n = readln().toInt()
    val n_li = readln().split(' ').map { it.toInt() }.sorted()
    val m = readln().toInt()
    val m_li = readln().split(' ').map { it.toInt() }

    m_li.forEach {
        if (n_li.binarySearch(it) < 0){
            print("0 ")
        }
        else {
            print("1 ")
        }
    }
}
