import kotlin.math.*

class Solution {
    fun solution(wallpaper: Array<String>): IntArray {
        var lux = Int.MAX_VALUE
        var luy = Int.MAX_VALUE
        var rdx = 0
        var rdy = 0

        wallpaper.forEachIndexed { x, row ->
            row.forEachIndexed { y, c ->
                if (c == '#') {
                    lux = min(lux, x)
                    luy = min(luy, y)
                    rdx = max(rdx, x)
                    rdy = max(rdy, y)
                }
            }
        }

        val answer: IntArray = intArrayOf(lux, luy, rdx + 1, rdy + 1)
        return answer
    }
}
