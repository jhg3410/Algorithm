class Solution {
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        val mutableCards1 = cards1.toMutableList()
        val mutableCards2 = cards2.toMutableList()

        goal.forEach { word ->
            when (word) {
                mutableCards1.firstOrNull() -> {
                    mutableCards1.removeFirst()
                }

                mutableCards2.firstOrNull() -> {
                    mutableCards2.removeFirst()
                }

                else -> {
                    return "No"
                }
            }
        }


        return "Yes"
    }
}