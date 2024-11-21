import java.util.*
import kotlin.math.*

class Solution {
    fun solution(a: IntArray): Int {
        var answer = 0
        
        val idxMap = mutableMapOf<Int, MutableSet<Int>>()
        for (i in a.indices) {
            idxMap[i] = mutableSetOf<Int>()
        }
        
        for ((idx, number) in a.withIndex()) {
            idxMap[number]!!.add(idx)
        }
        for (number in a.indices) {
        
            if (idxMap[number]!!.isEmpty()) continue
            val consumed = mutableSetOf<Int>()
            val idxs = idxMap[number]!!
            for (idx in idxs) {
                if (idx == 0) {
                    if (1 !in idxs && a.size > 1) {
                        consumed.add(1)    
                    }
                    continue
                }
                if (idx -1 !in idxs && idx -1 !in consumed) {
                    consumed.add(idx-1)
                } else if (idx + 1 !in idxs && idx +1 !in consumed &&  idx != a.lastIndex) {
                    consumed.add(idx+1)
                }
            }
            answer = max(answer, consumed.size * 2)
        }
        
        return answer
    }
}