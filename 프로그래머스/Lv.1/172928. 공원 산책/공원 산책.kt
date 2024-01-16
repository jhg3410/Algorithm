

enum class Direction(val pos: Pos) {
    N(pos = Pos(-1, 0)),
    S(pos = Pos(1, 0)),
    W(pos = Pos(0, -1)),
    E(pos = Pos(0, 1))
}

data class Pos(
    var x: Int,
    var y: Int
)

data class Route(
    val direction: Direction,
    val distance: Int
)


val dx = listOf(1, -1, 0, 0)
val dy = listOf(0, 0, 1, -1)

class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        val startPos = Pos(0, 0)
        park.forEachIndexed { x, s ->
            s.forEachIndexed { y, c ->
                if (c == 'S') startPos.run { this.x = x; this.y = y }
            }
        }

        routes.forEach {
            val (direction, distance) = it.split(' ')
            val route = Route(Direction.valueOf(direction), distance.toInt())

            val tmpPos = startPos.copy()
            repeat(route.distance) {
                tmpPos.x += route.direction.pos.x
                tmpPos.y += route.direction.pos.y
                if (tmpPos.x !in park.indices || tmpPos.y !in park.first().indices) return@forEach
                if (park[tmpPos.x][tmpPos.y] == 'X') return@forEach
            }
            startPos.x = tmpPos.x
            startPos.y = tmpPos.y
        }

        var answer: IntArray = intArrayOf(startPos.x, startPos.y)
        return answer
    }
}