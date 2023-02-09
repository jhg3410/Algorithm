package heejik.`22week`

import kotlin.properties.Delegates

class 여왕벌 {

    data class Pos(
        val x: Int,
        val y: Int
    ) {
        fun getLeftPos() = Pos(x = this.x + Direction.LEFT.pos.x, y = this.y + Direction.LEFT.pos.y)
        fun getLeftUpPos() = Pos(x = this.x + Direction.LEFT_UP.pos.x, y = this.y + Direction.LEFT_UP.pos.y)
        fun getUpPos() = Pos(x = this.x + Direction.UP.pos.x, y = this.y + Direction.UP.pos.y)
    }

    enum class Direction(val pos: Pos) {
        LEFT(Pos(0, -1)), LEFT_UP(Pos(-1, -1)), UP(Pos(-1, 0))
    }

    data class FirstGrowth(
        var zeroCnt: Int,
        var oneCnt: Int,
        var twoCnt: Int
    ) {
        fun getFirstGrowthAndReduceCnt(): Int {
            listOf(zeroCnt, oneCnt, twoCnt).forEachIndexed { number, cnt ->
                if (cnt <= 0) return@forEachIndexed
                when (number) {
                    0 -> zeroCnt --
                    1 -> oneCnt --
                    2 -> twoCnt --
                }
                return number
            }
            throw IndexOutOfBoundsException()
        }
    }

    private fun List<Int>.toFirstGrowth() = FirstGrowth(this[0], this[1], this[2])


    var m by Delegates.notNull<Int>()
    var n by Delegates.notNull<Int>()
    private lateinit var beeHome: List<MutableList<Int>>
    private val fakeBeeHome = mutableListOf<MutableList<Int>>()

    fun solve() {

        readln().split(' ').map { it.toInt() }.run {
            m = this.first()
            n = this.last()
            beeHome = List(m) { MutableList(m) { 1 } }
        }

        repeat(n) {
            val firstGrowth = readln().split(' ').map { it.toInt() }.toFirstGrowth()
            growth(firstGrowth)
        }

        beeHome.forEach {
            println(it.joinToString(" "))
        }
    }

    private fun growth(firstGrowth: FirstGrowth) {
        fakeBeeHome.clear()
        beeHome.forEach {
            fakeBeeHome.add(it.toMutableList())
        }

        // 왼쪽 제일 아래부터 오른쪽 제일 위까지

        for (x in m - 1 downTo 1) {
            fakeBeeHome[x][0] += firstGrowth.getFirstGrowthAndReduceCnt()
        }
        fakeBeeHome[0][0] += firstGrowth.getFirstGrowthAndReduceCnt()
        for (y in 1 until m) {
            fakeBeeHome[0][y] += firstGrowth.getFirstGrowthAndReduceCnt()
        }

        // 왼쪽, 왼위, 위의 최댓값으로 값 증가시키기

        for (i in 1 until m) {
            growOneLine(offset = i)
        }

        fakeBeeHome.forEachIndexed { x, row ->
            row.forEachIndexed { y, size ->
                beeHome[x][y] = size
            }
        }
    }

    private fun growOneLine(offset: Int) {
        fakeBeeHome[offset][offset] += getAroundIncrease(Pos(offset, offset))

        for (x in offset + 1 until m) {
            fakeBeeHome[x][offset] += getAroundIncrease(Pos(x, offset))
        }
        for (y in offset + 1 until m) {
            fakeBeeHome[offset][y] += getAroundIncrease(Pos(offset, y))
        }
    }

    private fun getAroundIncrease(pos: Pos): Int {
        val leftPos = pos.getLeftPos()
        val leftUpPos = pos.getLeftUpPos()
        val upPos = pos.getUpPos()
        return listOf(
            fakeBeeHome[leftPos.x][leftPos.y] - beeHome[leftPos.x][leftPos.y],
            fakeBeeHome[leftUpPos.x][leftUpPos.y] - beeHome[leftUpPos.x][leftUpPos.y],
            fakeBeeHome[upPos.x][upPos.y] - beeHome[upPos.x][upPos.y]
        ).max()
    }
}


fun main() {
    `여왕벌`().solve()
}