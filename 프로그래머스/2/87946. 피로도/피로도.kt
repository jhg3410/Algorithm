class Solution {
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        var maxN = 0
        for (i in 0 until dungeons.count()) {
            var d = dungeons[i]
            if (k >= d[0]) {
                var subN = solution(
                    k - d[1], 
                    dungeons.sliceArray(0 .. i - 1) + 
                        dungeons.sliceArray(i + 1 .. dungeons.count() - 1))
                if (subN + 1 > maxN) maxN = subN + 1
            }
        }
        return maxN
    }
}