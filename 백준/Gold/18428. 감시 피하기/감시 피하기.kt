package heejik.`22week`

import kotlin.properties.Delegates
import kotlin.system.exitProcess

class `감시 피하기` {

    private val hall = mutableListOf<MutableList<String>>()
    var n by Delegates.notNull<Int>()


    enum class Move(val pos: Pos) {
        TOP(pos = Pos(x = -1, y = 0)),
        BOTTOM(pos = Pos(x = +1, y = 0)),
        LEFT(pos = Pos(x = 0, y = -1)),
        RIGHT(pos = Pos(x = 0, y = +1))
    }

    data class Pos(
        val x: Int,
        val y: Int
    ) {
        infix fun plus(other: Pos) = Pos(x = this.x + other.x, y = this.y + other.y)
        infix fun isInHall(hallSize: Int) = x in 0 until hallSize && y in 0 until hallSize
    }


    fun solve() {
        setting()
        start()
    }

    private fun setting() {
        n = readln().toInt()
        repeat(n) {
            hall.add(readln().split(' ').toMutableList())
        }
    }

    private fun start() {
        pick(selectedPos = listOf())
        print("NO")
    }

    private fun pick(selectedPos: List<Pos>) {
        if (selectedPos.size == 3) {
            if (check()) {
                println("YES")
                exitProcess(0)
            }
            return
        }

        for (x in 0 until n) {
            for (y in 0 until n) {
                if (hall[x][y] == "X") {
                    hall[x][y] = "O"
                    pick(selectedPos.plus(Pos(x, y)))
                    hall[x][y] = "X"
                }
            }
        }
    }

    private fun check(): Boolean {
        hall.forEachIndexed { x, row ->
            row.forEachIndexed { y, s ->
                if (s == "T") {
                    if (checkByTeacher(teacherPos = Pos(x, y)).not()) return false
                }
            }
        }
        return true
    }

    private fun checkByTeacher(teacherPos: Pos): Boolean {

        var topPos = teacherPos plus Move.TOP.pos
        var bottomPos = teacherPos plus Move.BOTTOM.pos
        var leftPos = teacherPos plus Move.LEFT.pos
        var rightPos = teacherPos plus Move.RIGHT.pos

        // 위
        while (topPos.isInHall(n)) {
            when (hall[topPos.x][topPos.y]) {
                "O" -> break
                "S" -> return false
            }
            topPos = topPos plus Move.TOP.pos
        }
        // 아래
        while (bottomPos.isInHall(n)) {
            when (hall[bottomPos.x][bottomPos.y]) {
                "O" -> break
                "S" -> return false
            }
            bottomPos = bottomPos plus Move.BOTTOM.pos
        }
        // 왼
        while (leftPos.isInHall(n)) {
            when (hall[leftPos.x][leftPos.y]) {
                "O" -> break
                "S" -> return false
            }
            leftPos = leftPos plus Move.LEFT.pos
        }
        // 오
        while (rightPos.isInHall(n)) {
            when (hall[rightPos.x][rightPos.y]) {
                "O" -> break
                "S" -> return false
            }
            rightPos = rightPos plus Move.RIGHT.pos
        }
        return true
    }
}

fun main() {
    `감시 피하기`().solve()
}