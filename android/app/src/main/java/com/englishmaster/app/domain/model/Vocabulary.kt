package com.englishmaster.app.domain.model

/**
 * Represents a vocabulary word in the English learning system
 */
data class Vocabulary(
    val id: Long,
    val word: String,
    val meaning: String,
    val partOfSpeech: PartOfSpeech,
    val pronunciation: String = "",
    val ipa: String = "",
    val difficulty: Int = 1, // 1-10 scale
    val frequency: Int = 1, // 1-10 scale (1 = most common)
    val exampleSentence: String = "",
    val exampleTranslation: String = "",
    val synonyms: List<String> = emptyList(),
    val antonyms: List<String> = emptyList(),
    val relatedWords: List<String> = emptyList(),
    val plural: String? = null,
    val pastForm: String? = null,
    val pastParticiple: String? = null,
    val presentParticiple: String? = null,
    val tags: List<String> = emptyList(),
    val categoryId: Long? = null
)

enum class PartOfSpeech {
    NOUN,
    VERB,
    ADJECTIVE,
    ADVERB,
    PRONOUN,
    PREPOSITION,
    CONJUNCTION,
    INTERJECTION,
    DETERMINER,
    PHRASAL_VERB,
    IDIOM,
    EXPRESSION
}
