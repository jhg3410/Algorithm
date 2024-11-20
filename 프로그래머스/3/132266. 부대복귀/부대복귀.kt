import java.util.*

class Solution {
    fun solution(n: Int, roads: Array<IntArray>, sources: IntArray, destination: Int): IntArray {
        val roadInfo = List(size = n+1) { mutableListOf<Int>() }
        
        for ((road1, road2) in roads) {
            roadInfo[road1].add(road2)
            roadInfo[road2].add(road1)
        }
        
        val pq = PriorityQueue<Pair<Int, Int>> { a1, b1 ->
            a1.first - b1.first
        }
        pq.add(0 to destination)
        val distances = MutableList<Int>(size = n+1) { Int.MIN_VALUE }
        distances[destination] = 0
        
        while (pq.isNotEmpty()) {
            val (time, currentRoad) = pq.poll()
            for (road in roadInfo[currentRoad]) {
                if (distances[road] == Int.MIN_VALUE) {
                    distances[road] = time+1
                    pq.add(time+1 to road)
                }
            }
        }
        
    
        return sources.map { 
            if (distances[it] == Int.MIN_VALUE) -1
            else distances[it]
        }.toIntArray()
    }
}