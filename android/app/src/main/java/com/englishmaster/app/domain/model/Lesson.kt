package com.englishmaster.app.domain.model

/**
 * Represents a lesson within a unit
 */
data class Lesson(
    val id: Long,
    val unitId: Long,
    val name: String,
    val description: String = "",
    val order: Int = 0,
    val lessonType: LessonType = LessonType.NORMAL,
    val requiredXp: Int = 0,
    val estimatedDuration: Int = 5 // minutes
)

enum class LessonType {
    NORMAL,       // Regular lesson
    REVIEW,       // Review lesson
    TEST,         // Unit test
    PRACTICE,     // Practice session
    READING,      // Reading comprehension
    LISTENING,    // Listening practice
    SPEAKING,     // Speaking practice
    WRITING       // Writing practice
}
