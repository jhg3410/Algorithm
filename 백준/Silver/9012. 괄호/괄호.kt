import java.io.BufferedReader
import java.io.InputStreamReader


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    repeat(readln().toInt()) {
        val par = readln()
        println(if (isVPS(par)) "YES" else "NO")
    }
}


fun isVPS(par:String) :Boolean{
    val tmp = arrayListOf<Char>()
    par.forEach {
        if (it == '('){
            tmp.add(it)
        }
        else {
            if (tmp.isEmpty()) return false
            if (tmp.last() == '(') tmp.removeLast()
        }
    }
    return tmp.isEmpty()
}