data class Job(
    val waitingTime: Int,
    var burstTime: Int
)

fun IntArray.toJob() = Job(waitingTime = this[0], burstTime = this[1])

class Solution {
    fun solution(_jobs: Array<IntArray>): Int {
        val jobs = _jobs.map {
            it.toJob()
        }.toMutableList()
        var sumOfTurnaroundTime = 0
        var workJob : Job? = null
        var time = 0
    
        while(jobs.isNotEmpty() || workJob != null) {
            if (workJob == null) {
                val playJob = jobs.filter { it.waitingTime <= time }.minByOrNull { it.burstTime }
                jobs.remove(playJob)
                workJob = playJob
            } 
            time++
            if (workJob != null && --workJob.burstTime == 0) {
                sumOfTurnaroundTime += time - workJob.waitingTime
                workJob = null
            }
        }
        
        
        return sumOfTurnaroundTime / _jobs.size
    }
}