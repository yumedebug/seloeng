package com.englishmaster.app.domain.model

/**
 * Represents a unit within a level (e.g., Unit 1, Unit 2)
 */
data class Unit(
    val id: Long,
    val levelId: Long,
    val name: String,
    val description: String = "",
    val order: Int = 0,
    val requiredXp: Int = 0, // XP needed to unlock
    val icon: String = ""
)
