package heejik.`63week`

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

class `도시 건설` {

    data class Edge(
        val a: Int,
        val b: Int,
        val cost: Int
    )

    fun solve() = BufferedReader(InputStreamReader(System.`in`)).run {
        val (n, m) = readln().split(' ').map { it.toInt() }
        var allCost = 0L
        var minimumCost = 0L
        val edges = MutableList(size = m) { Edge(0, 0, 0) }
        val parents = MutableList(size = n + 1) { it }

        repeat(m) { idx ->
            val (a, b, cost) = readln().split(' ').map { it.toInt() }
            allCost += cost
            edges[idx] = Edge(a, b, cost)
        }

        for ((a, b, cost) in edges.sortedBy { it.cost }) {
            var parentA = a
            var parentB = b

            while (parentA != parents[parentA]) {
                parentA = parents[parentA]
            }
            while (parentB != parents[parentB]) {
                parentB = parents[parentB]
            }

            if (parentA == parentB) continue

            if (parentA < parentB) {
                parents[parentB] = parentA
            } else {
                parents[parentA] = parentB
            }
            minimumCost += cost
        }
        
        for (node in 2..n) {
            var parentNode = node
            while (parentNode != parents[parentNode]) {
                parentNode = parents[parentNode]
            }
            if (parentNode != 1) {
                println(-1)
                return
            }
        }
        println(allCost - minimumCost)
    }
}

fun main() {
    `도시 건설`().solve()
}