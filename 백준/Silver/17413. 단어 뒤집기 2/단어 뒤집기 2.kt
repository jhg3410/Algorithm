import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*


fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {

    val s = readln()
    val sb = StringBuilder()
    var stack = Stack<Char>()
    var isTag = false
    s.forEach {
        when (it) {
            ' ' -> {
                stackAddToSb(stack, sb, it)
            }

            '<' -> {
                isTag = true
                stackAddToSb(stack, sb, it)
            }

            '>' -> {
                isTag = false
                stackAddToSb(stack, sb, it)
            }

            else -> {
                if (isTag) sb.append(it)
                else stack.push(it)
            }
        }
    }
    stackAddToSb(stack,sb,)

    println(sb.toString())
}

fun stackAddToSb(stack: Stack<Char>, sb: StringBuilder, c:Char=' ') {
    while (stack.isNotEmpty()) {
        sb.append(stack.pop())
    }
    sb.append(c)
}
