data class YearnMan(
    val name: String,
    val yearning: Int
)

class Solution {
    fun solution(names: Array<String>, yearnings: IntArray, photos: Array<Array<String>>): IntArray {
        val answer = mutableListOf<Int>()
        val yearnmans = mutableListOf<YearnMan>()
        for ((name, yearning) in names.zip(yearnings.toTypedArray())) {
            yearnmans.add(YearnMan(name = name, yearning = yearning))
        }
        
        photos.forEach { photo ->
            var score = 0
            photo.forEach { man ->
                score += yearnmans.find { it.name == man }?.yearning ?: 0
            }
            answer.add(score)
        }


        return answer.toIntArray()
    }
}