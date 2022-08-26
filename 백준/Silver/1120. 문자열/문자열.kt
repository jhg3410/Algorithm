import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.Collections.min


val li = arrayListOf<Int>()

fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (a,b) = readln().split(" ")
    solve(a,b)
    println(min(li) - (b.length - a.length))
}

fun solve(a:String,b:String){
    if (a.length == b.length)
        countDiff(a,b)

    for (i in 0 .. (b.length - a.length)){
        var newA : String = ""

        for (j in 0 until i) {
            newA = "1$newA"
        }
        newA += a
        for (j in i until (b.length - a.length)){
            newA += '1'
        }
        
        countDiff(newA,b)

    }
}

fun countDiff(a:String, b:String){
    li.add(a.filterIndexed { index, c -> a[index] != b[index] }.run {
        if (this.isEmpty()) 0
        else this.length
    })
}