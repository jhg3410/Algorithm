import kotlin.math.*

class Solution {
    var diceSize = -1
    var dices = mutableListOf<List<Int>>()
    var maxWin = Int.MIN_VALUE
    var winDice = emptyList<Int>()

    fun solution(dice: Array<IntArray>): IntArray {
        diceSize = dice.size
        for (row in dice) {
            dices.add(row.toList())
        }
        getAllCase(selected = mutableListOf(), start = 1)
        return winDice.sorted().toIntArray()
    }

    private fun getAllCase(selected: MutableList<Int>, start: Int) {
        if (selected.size == diceSize / 2) {
            val winCount = calculation(selected)
            if (winCount > maxWin) {
                maxWin = winCount
                winDice = selected.toList()
            }
            return
        }

        for (i in start..diceSize) {
            selected.add(i)
            getAllCase(selected = selected, start = i + 1)
            selected.removeLast()
        }
    }

    private fun calculation(selectDice: List<Int>): Int {
        val partialDiceSize = diceSize / 2
        val otherDice = (1..diceSize).filter { it !in selectDice }
        val selectScore = MutableList(size = 100 * partialDiceSize + 1) { 0 }
        val otherScore = MutableList(size = 100 * partialDiceSize + 1) { 0 }
        val store = MutableList(size = 100 * partialDiceSize + 1) { 0 }
        // 선택된 주사위 경우의 수 구하기
        for (number in dices[selectDice.first() - 1]) {
            selectScore[number] += 1
        }
        for (dice in selectDice.drop(1).map { dices[it - 1] }) {
            for (i in 1..(100 * partialDiceSize)) {
                if (selectScore[i] == 0) continue
                for (number in dice) {
                    if (i + number > (100 * partialDiceSize)) continue
                    store[i + number] += selectScore[i]
                }
            }
            for (i in store.indices) {
                selectScore[i] = store[i]
            }
            store.fill(0)
        }
        // 반대되는 주사위 경우의 수 구하기
        for (number in dices[otherDice.first() - 1]) {
            otherScore[number] += 1
        }
        for (dice in otherDice.drop(1).map { dices[it - 1] }) {
            for (i in 1..(100 * partialDiceSize)) {
                if (otherScore[i] == 0) continue
                for (number in dice) {
                    if (i + number > (100 * partialDiceSize)) continue
                    store[i + number] += otherScore[i]
                }
            }
            for (i in store.indices) {
                otherScore[i] = store[i]
            }
            store.fill(0)
        }

        var winCount = 0
        for (i in 1..(100 * (diceSize / 2))) {
            if (selectScore[i] == 0) continue
            for (j in 1 until i) {
                if (otherScore[j] == 0) continue
                winCount += selectScore[i] * otherScore[j]
            }
        }

        return winCount
    }
}