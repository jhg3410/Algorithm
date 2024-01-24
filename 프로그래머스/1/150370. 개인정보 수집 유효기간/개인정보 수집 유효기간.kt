
class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        val answer = mutableListOf<Int>()
        
        val (year, month, day) = today.split('.').map { it.toInt() }
        val sumOfTodays: Int = year * 336 + month * 28 + day
        val termMap = mutableMapOf<String, Int>()
        
        terms.forEach { 
            val (name, monthOfTerm) = it.split(' ')
            termMap[name]= monthOfTerm.toInt() * 28
        }
        
        privacies.forEachIndexed { idx, privacy ->
            val (date, term) = privacy.split(' ')
            val (yearOfPrivacy, monthOfPrivacy, dayOfPrivacy) = date.split('.').map { it.toInt() }
            val sumOfDaysOfPrivacy: Int = yearOfPrivacy * 336 + monthOfPrivacy * 28 + dayOfPrivacy
    
            if (sumOfTodays >= termMap[term]!! + sumOfDaysOfPrivacy) {
                answer.add(idx+1)
            }
        }
        
        
        return answer.toIntArray()
    }
}