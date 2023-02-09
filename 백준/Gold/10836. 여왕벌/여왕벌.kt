package heejik.`22week`

import kotlin.properties.Delegates

class 여왕벌 {

    data class Space(
        var size: Int,
        var growth: Int
    )

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
                    0 -> zeroCnt--
                    1 -> oneCnt--
                    2 -> twoCnt--
                }
                return number
            }
            throw IndexOutOfBoundsException()
        }
    }

    private fun List<Int>.toFirstGrowth() = FirstGrowth(this[0], this[1], this[2])


    var m by Delegates.notNull<Int>()
    var n by Delegates.notNull<Int>()
    private lateinit var beeHome: MutableList<MutableList<Space>>

    fun solve() {

        readln().split(' ').map { it.toInt() }.run {
            m = this.first()
            n = this.last()
            beeHome = MutableList(m) { MutableList(m) { Space(1, 0) } }
        }

        repeat(n) {
            val firstGrowth = readln().split(' ').map { it.toInt() }.toFirstGrowth()
            grow(firstGrowth)
        }

        beeHome.forEach {
            println(it.map { space -> space.size }.joinToString(" "))
        }
    }

    private fun grow(firstGrowth: FirstGrowth) {

        // 왼쪽 제일 아래부터 오른쪽 제일 위까지

        for (x in m - 1 downTo 1) {
            firstGrowth.getFirstGrowthAndReduceCnt().run {
                beeHome[x][0].size += this
                beeHome[x][0].growth = this
            }
        }
        firstGrowth.getFirstGrowthAndReduceCnt().run {
            beeHome[0][0].size += this
            beeHome[0][0].growth = this
        }


        for (y in 1 until m) {
            firstGrowth.getFirstGrowthAndReduceCnt().run {
                beeHome[0][y].size += this
                beeHome[0][y].growth = this
            }
        }

        // 왼쪽, 왼위, 위의 최댓값으로 값 증가시키기

        for (i in 1 until m) {
            growOneLine(offset = i)
        }
    }

    private fun growOneLine(offset: Int) {
        getAroundIncrease(Pos(offset, offset)).run {
            beeHome[offset][offset].size += this
            beeHome[offset][offset].growth = this
        }

        for (x in offset + 1 until m) {
            getAroundIncrease(Pos(x, offset)).run {
                beeHome[x][offset].size += this
                beeHome[x][offset].growth = this
            }
        }
        for (y in offset + 1 until m) {
            getAroundIncrease(Pos(offset, y)).run {
                beeHome[offset][y].size += this
                beeHome[offset][y].growth = this
            }
        }
    }

    private fun getAroundIncrease(pos: Pos): Int {
        val leftPos = pos.getLeftPos()
        val leftUpPos = pos.getLeftUpPos()
        val upPos = pos.getUpPos()
        return listOf(
            beeHome[leftPos.x][leftPos.y].growth,
            beeHome[leftUpPos.x][leftUpPos.y].growth,
            beeHome[upPos.x][upPos.y].growth
        ).max()
    }
}


fun main() {
    `여왕벌`().solve()
}