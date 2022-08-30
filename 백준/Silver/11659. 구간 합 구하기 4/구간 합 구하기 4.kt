import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val (n, m) = this.readLine().split(' ').map { it.toInt() }

    val li = this.readLine().split(' ').map { it.toInt() }

    var s = 0
    val prefix = arrayListOf<Int>(0)

    li.forEach {
        prefix.add(it + s)
        s += it
    }
    repeat(m){
        val (i, j) = this.readLine().split(' ').map { it.toInt() }
        bw.write("${prefix[j] - prefix[i-1]}\n")
    }
    this.close()
    bw.close()
}

