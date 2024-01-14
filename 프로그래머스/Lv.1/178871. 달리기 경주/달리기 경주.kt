class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        val playerToRank = mutableMapOf<String, Int>()
        
        players.forEachIndexed { index, name ->
            playerToRank[name] = index
        }

        callings.forEach {
            val rank = playerToRank[it]!!       // 랭크 파악
            val preRank = rank - 1

            val tmp = players[preRank]  // 해당 랭크로 이전 플레이어를 찾아
            players[preRank] = it   //  이전 플레이어 랭크에 지금 애를 넣고
            players[rank] = tmp    // 해당 랭크에 이전 애를 넣어

            //랭크를 파악하기 위해 최신화 필요
            playerToRank[tmp] = rank    // 추월당한 친구의 rank 를 지금 rank 로
            playerToRank[it] = preRank  // 추월한 애의 rank 를 이전 rank 로
        }

        return players
    }
}
