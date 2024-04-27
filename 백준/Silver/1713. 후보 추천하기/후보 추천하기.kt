package heejik.`59week`

import java.util.*


data class Candidate(
    val number: Int,
    var round: Int,
    var recommendCount: Int = 0
) : Comparable<Candidate> {
    override fun compareTo(other: Candidate): Int {
        return if (this.recommendCount == other.recommendCount) {
            this.round - other.round
        } else {
            this.recommendCount - other.recommendCount
        }
    }
}

class `후보 추천하기` {
    fun solve() {
        val n = readln().toInt()

        val pq = PriorityQueue<Candidate>()

        val cardCount = readln().toInt()
        val numbers = readln().split(' ').map { it.toInt() }

        numbers.forEachIndexed { round, number ->
            val candidate = pq.find { it.number == number } ?: run {
                if (pq.size < n) {
                    pq.add(Candidate(number = number, round = round))
                    return@run null
                }
                pq.poll()
                pq.add(Candidate(number = number, round = round))
                null
            }


            candidate?.let { hi ->
                val can = pq.find { it == hi }!!
                pq.remove(can)
                pq.add(can.copy(recommendCount = can.recommendCount + 1))
            }
        }

        println(pq.map { it.number }.sorted().joinToString(" "))
    }
}

fun main() {
    `후보 추천하기`().solve()
}