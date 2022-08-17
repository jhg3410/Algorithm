fun main() {
    val n = readln().toInt()
    repeat(n) {
        val answer = arrayListOf<Int>()
        val result = readln()
        result.forEach {
            if (it == 'O') {
                answer.apply {
                    if (this.isNotEmpty()) add(last() + 1)
                    else add(1)
                }
            } else answer.add(0)
        }
        println(answer.sum())
    }
}