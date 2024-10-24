import kotlin.math.min

private fun List<List<Int>>.deepCopy(): List<MutableList<Int>> {
    val newList = List(size = 4) { MutableList(size = 4) { 0 } }

    for (i in 0..3) {
        for (j in 0..3) {
            newList[i][j] = this[i][j]
        }
    }
    return newList
}

class Solution {
    val dxs = listOf(-1, 0, 1, 0)
    val dys = listOf(0, 1, 0, -1)
    val cards = mutableListOf<Int>()
    var answer = Int.MAX_VALUE
    val originBoard = List(size = 4) { MutableList(size = 4) { 0 } }
    var startX = 0
    var startY = 0

    private fun isInBoard(x: Int, y: Int): Boolean {
        return (x in 0..3) && (y in 0..3)
    }

    fun solution(board: Array<IntArray>, r: Int, c: Int): Int {
        startX = r
        startY = c

        for (i in 0..3) {
            for (j in 0..3) {
                val number = board[i][j]
                if (number > 0) {
                    originBoard[i][j] = board[i][j]

                    if (number in cards) continue
                    cards.add(number)
                }
            }
        }

        getCase(stored = mutableListOf())

        return answer
    }

    private fun getCase(stored: MutableList<Int>) {
        if (stored.size == cards.size) {
            answer = min(answer, getControlCount(orders = stored))
            return
        }

        for (card in cards) {
            if (card in stored) continue

            stored.add(card)
            getCase(stored = stored)
            stored.removeLast()
        }
    }

    private fun getControlCount(orders: List<Int>): Int {
        val board = originBoard.deepCopy()
        return move(orders, startX, startY, 0, false, board)
    }

    private fun move(
        findNumbers: List<Int>,
        currentX: Int,
        currentY: Int,
        ctrlCount: Int,
        isReversed: Boolean,
        board: List<MutableList<Int>>
    ): Int {
        var minCount = Int.MAX_VALUE
        if (findNumbers.isEmpty()) return ctrlCount

        val findNumber = findNumbers.first()
        val newBoard = board.deepCopy()

        // 이미 찾는 카드 하나가 뒤집혀 있으면
        if (isReversed) {
            val (nx, ny, dist) = getMinDistance(currentX, currentY, newBoard, findCard = findNumber)
            newBoard[nx][ny] = 0
            minCount = min(minCount, move(findNumbers.drop(1), nx, ny, ctrlCount + dist + 1, false, newBoard))
        } else {
            val (firstX, firstY, firstDist) = getMinDistance(currentX, currentY, newBoard, findCard = findNumber)
            newBoard[firstX][firstY] = 0
            val (secondX, secondY, secondDist) = getMinDistance(currentX, currentY, newBoard, findCard = findNumber)

            minCount =
                min(minCount, move(findNumbers.toList(), firstX, firstY, ctrlCount + firstDist + 1, true, newBoard))
            val newNewBoard = board.deepCopy()
            newNewBoard[secondX][secondY] = 0
            minCount = min(
                minCount,
                move(findNumbers.toList(), secondX, secondY, ctrlCount + secondDist + 1, true, newNewBoard)
            )
        }

        return minCount
    }


    // 특정 카드로 가는 최단 길
    private fun getMinDistance(
        currentX: Int,
        currentY: Int,
        board: List<List<Int>>,
        findCard: Int
    ): Triple<Int, Int, Int> {

        var minX = -1
        var minY = -1
        var minDistance = 0
        val visited = List(size = 4) { BooleanArray(size = 4) { false } }

        val queue = ArrayDeque<Triple<Int, Int, Int>>()
        queue.add(Triple(currentX, currentY, 0))

        while (queue.isNotEmpty()) {
            val (x, y, moveCount) = queue.removeFirst()
            if (board[x][y] == findCard) {
                minX = x
                minY = y
                minDistance = moveCount
                break
            }

            for (i in 0..3) {
                var nx = x + dxs[i]
                var ny = y + dys[i]
                if (isInBoard(nx, ny) && visited[nx][ny].not()) {
                    queue.add(Triple(nx, ny, moveCount + 1))
                }
                getCtrlMovePos(i, x, y, board).let {
                    nx = it.first
                    ny = it.second
                }
                // 컨트롤 이동해도 해당 위치 그대로면 무시
                if (nx == x && ny == y) continue
                if (visited[nx][ny].not()) {
                    queue.add(Triple(nx, ny, moveCount + 1))
                }
            }
        }
        return Triple(minX, minY, minDistance)
    }

    private fun getCtrlMovePos(
        direction: Int, x: Int, y: Int,
        board: List<List<Int>>
    ): Pair<Int, Int> {
        var nx = x
        var ny = y
        while (true) {
            val nextX = nx + dxs[direction]
            val nextY = ny + dys[direction]
            if (isInBoard(nextX, nextY).not()) break
            if (board[nextX][nextY] != 0) {
                nx = nextX
                ny = nextY
                break
            }
            nx = nextX
            ny = nextY
        }

        return nx to ny
    }
}