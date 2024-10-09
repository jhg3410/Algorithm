class Solution {
    private val links = mutableListOf<String>()
    private val linkToDefaultScore = mutableMapOf<String, Int>()
    private val linkToOuterLinks = mutableMapOf<String, List<String>>()
    private val linkToLinkScore = mutableMapOf<String, Double>()

    fun solution(word: String, pages: Array<String>): Int {

        for (html in pages) {
            val url = getUrl(html = html)
            val defaultScore = getDefaultScore(html = html, word = word)
            val outerLinks = getOuterLinks(html = html)
            links.add(url)
            linkToDefaultScore[url] = defaultScore
            linkToOuterLinks[url] = outerLinks
        }

        // 링크 점수 세팅
        for (url in links) {
            val defaultScore = linkToDefaultScore[url] ?: 0
            val outerLinkCount = linkToOuterLinks[url]?.count() ?: 0
            for (outerLink in linkToOuterLinks[url]!!) {
                linkToLinkScore[outerLink] = (linkToLinkScore[outerLink] ?: 0.0) + (defaultScore.toDouble() / outerLinkCount)
            }
        }

        var answer = 0
        var maxScore = -1.0

        for ((index, url) in links.withIndex()) {
            val matchingScore = (linkToLinkScore[url] ?: 0.0) + linkToDefaultScore[url]!!
            if (matchingScore > maxScore) {
                answer = index
                maxScore = matchingScore
            }
        }

        return answer
    }


    private fun getUrl(html: String): String {
        val urlTag = "<meta property=\"og:url\" content=\""
        return html.substringAfter(delimiter = urlTag).substringBefore(delimiter = "\"/>")
    }

    private fun getDefaultScore(html: String, word: String): Int {
        var defaultScore = 0
        val store = StringBuilder()

        for (char in html) {
            if (store.length < word.length + 2) {
                store.append(char)
            } else {
                store.deleteCharAt(0)
                store.append(char)
            }
            if (store.length == word.length + 2) {
                if (!store.first().isLetter() && !store.last().isLetter()) {
                    if (word.lowercase() == store.substring(startIndex = 1, endIndex = word.length + 1).lowercase()) {
                        defaultScore += 1
                    }
                }
            }
        }
        return defaultScore
    }

    private fun getOuterLinks(html: String): List<String> {
        val outerLinks = mutableListOf<String>()
        val outerTag = "<a href=\""
        var currentHtml = html

        while (true) {
            currentHtml = currentHtml.substringAfter(delimiter = outerTag, missingDelimiterValue = "")
            if (currentHtml.isEmpty()) break
            val outerLink = currentHtml.substringBefore("\"")
            outerLinks.add(outerLink)
        }

        return outerLinks
    }
}