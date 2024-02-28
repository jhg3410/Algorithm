import kotlin.math.*

class Solution {
    fun solution(cap: Int, n: Int, deliveries: IntArray, pickups: IntArray): Long {

        var distance = 0L
        var saveDelivery = 0
        var savePickup = 0

        for (i in n - 1 downTo 0) {
            if (deliveries[i] <= saveDelivery && pickups[i] <= savePickup) {
                saveDelivery -= deliveries[i]
                savePickup -= pickups[i]
                continue
            }

            var visit = 1
            while (visit * cap + saveDelivery < deliveries[i] || visit * cap + savePickup < pickups[i]) {
                visit++
            }

            saveDelivery = visit * cap + saveDelivery - deliveries[i]
            savePickup = visit * cap + savePickup - pickups[i]

            distance += 2 * visit * (i + 1)
        }

        return distance
    }
}