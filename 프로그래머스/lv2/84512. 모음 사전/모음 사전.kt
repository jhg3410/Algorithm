class Solution {
    fun solution(word: String): Int {
        val vowel = arrayListOf<String>("A", "E", "I", "O", "U")
        val li = arrayListOf<String>("A", "E", "I", "O", "U")
        val tmp = arrayListOf<String>()

        repeat(4) {
            li.forEach {
                vowel.forEach { v ->
                    tmp.add(it + v)
                }
            }
            li += tmp
            tmp.clear()
        }
        return li.sorted().toSet().indexOf(word)+1
    }
}