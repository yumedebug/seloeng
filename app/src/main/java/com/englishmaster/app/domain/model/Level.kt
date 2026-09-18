package com.englishmaster.app.domain.model

/**
 * Represents a learning level (e.g., Starter, Beginner, Intermediate)
 */
data class Level(
    val id: Long,
    val courseId: Long,
    val name: String,
    val description: String = "",
    val order: Int = 0,
    val icon: String = "",
    val color: String = ""
)

enum class LevelType(val displayName: String, val order: Int) {
    STARTER("Starter", 0),
    BEGINNER("Beginner", 1),
    ELEMENTARY("Elementary", 2),
    PRE_INTERMEDIATE("Pre-Intermediate", 3),
    INTERMEDIATE("Intermediate", 4),
    UPPER_INTERMEDIATE("Upper-Intermediate", 5),
    ADVANCED("Advanced", 6),
    EXPERT("Expert", 7);
    
    companion object {
        fun fromOrder(order: Int): LevelType {
            return values().find { it.order == order } ?: BEGINNER
        }
    }
}
