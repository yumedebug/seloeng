package com.englishmaster.app.domain.model

/**
 * Represents a grammar lesson in the English learning system
 */
data class Grammar(
    val id: Long,
    val name: String,
    val description: String,
    val explanation: String,
    val structure: String = "",
    val usage: String = "",
    val examples: List<GrammarExample> = emptyList(),
    val notes: String = "",
    val difficulty: Int = 1, // 1-10 scale
    val relatedGrammarIds: List<Long> = emptyList(),
    val categoryId: Long? = null
)

data class GrammarExample(
    val sentence: String,
    val translation: String = "",
    val highlight: String = "" // Part to emphasize
)
