class Solution {
    fun solution(s: Array<String>): Array<String> {
        var answer = MutableList<String>(size = s.size) {""}

        for ((idx, str) in s.withIndex()) {
            answer[idx] = getSortedS(s = str)
        }

        return answer.toTypedArray()
    }

    fun getSortedS(s: String): String {
        val stack = mutableListOf<Char>()
        var count110 = 0
        for (char in s) {
            if (stack.size < 2 || char == '1') {
                stack.add(char)
                continue
            }
            val stackLastIndex = stack.lastIndex
            if (stack[stackLastIndex] == '1' && stack[stackLastIndex-1] == '1') {
                repeat(2) {
                    stack.removeLast()
                }
                count110 += 1
            } else {
                stack.add(char)
            }
        }

        var answer = StringBuilder()
        for (i in stack.indices) {
            if (i <= stack.lastIndex -2 && stack[i] == '1' && stack[i+1] == '1' && stack[i+2] == '1') {
                while (count110 >0) {
                    answer.append("110")
                    count110 -=1
                }
            }
            answer.append(stack[i])
        }

        var oneCount = 0
        while (answer.isNotEmpty() && answer.last() == '1') {
            oneCount += 1
            answer.deleteAt(answer.lastIndex)
        }
        while (count110 >0) {
            answer.append("110")
            count110 -=1
        }
        repeat(oneCount) {
            answer.append('1')
        }
        
        return answer.toString()
    }
}