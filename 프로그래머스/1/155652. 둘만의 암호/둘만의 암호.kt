class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        var answer: String = ""

        s.forEach {
            var changeAlpha = it
            repeat(index) {
                changeAlpha = getNextAlpha(changeAlpha)
                println(changeAlpha)
                while (changeAlpha in skip) {
                    changeAlpha = getNextAlpha(changeAlpha)
                }
            }
            answer += changeAlpha
        }

        return answer
    }

    private fun getNextAlpha(stand: Char): Char {
        return stand.inc().run {
            if (this == '{') 'a'
            else this
        }
    }
}