package com.englishmaster.app.domain.model

/**
 * Represents a vocabulary category (e.g., Daily Life, Business, Technology)
 */
data class VocabularyCategory(
    val id: Long,
    val name: String,
    val description: String = "",
    val icon: String = "",
    val order: Int = 0
)

/**
 * Represents a grammar category (e.g., Tenses, Parts of Speech)
 */
data class GrammarCategory(
    val id: Long,
    val name: String,
    val description: String = "",
    val icon: String = "",
    val order: Int = 0
)
