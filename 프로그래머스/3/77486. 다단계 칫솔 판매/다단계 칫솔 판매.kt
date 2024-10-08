class Solution {
    fun solution(enroll: Array<String>, referral: Array<String>, seller: Array<String>, amount: IntArray): IntArray {
        val answer: MutableList<Int> = mutableListOf()
        // key 의 부모는 value
        val parents = mutableMapOf<String, String>()
        val revenues = mutableMapOf<String, Int>()

        for (i in enroll.indices) {
            parents[enroll[i]] = referral[i]
        }

        for (i in seller.indices) {
            var current = seller[i]
            var currentRevenue = amount[i] * 100

            while (true) {
                val tenPercentRevenue = currentRevenue / 10
                revenues[current] = (revenues[current] ?: 0) + (currentRevenue - tenPercentRevenue)
                currentRevenue = tenPercentRevenue
                if (currentRevenue == 0) break
                current = parents[current] ?: break
            }
        }
        for (name in enroll) {
            answer.add(revenues[name] ?: 0)
        }
        return answer.toIntArray()
    }
}