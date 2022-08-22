import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readln()
    var answer = 0
    var tmpCnt = 0
    for (i in 0..9) {
        val cnt = n.count{ it.toString() == i.toString() }
        if (i == 6 || i == 9){
            tmpCnt += cnt
        }else{
            answer = max(answer,cnt)
        }
    }
    println(max(answer,tmpCnt.run { if (this %2 == 1) (tmpCnt/2)+1 else tmpCnt/2 }))
}
