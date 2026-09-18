package com.englishmaster.app.domain.model

import java.time.LocalDate

/**
 * Represents the user's learning profile and progress
 */
data class User(
    val id: Long = 1,
    val name: String = "Learner",
    val createdAt: LocalDate = LocalDate.now(),
    val currentLevelId: Long = 1,
    val currentUnitId: Long = 1,
    val totalXp: Int = 0,
    val currentStreak: Int = 0,
    val longestStreak: Int = 0,
    val lastStudyDate: LocalDate? = null,
    val lives: Int = 5,
    val maxLives: Int = 5,
    val dailyGoalXp: Int = 20,
    val dailyGoalProgress: Int = 0,
    val isOnboardingComplete: Boolean = false,
    val experienceLevel: UserExperienceLevel = UserExperienceLevel.BEGINNER
)

enum class UserExperienceLevel {
    BEGINNER,           // First time learning English
    ELEMENTARY,         // Knows basic English
    INTERMEDIATE,       // Can communicate somewhat
    ADVANCED,           // Comfortable with English
    NATIVE              // Native speaker (for review purposes)
}

/**
 * User's progress in a lesson
 */
data class LessonProgress(
    val id: Long,
    val userId: Long,
    val lessonId: Long,
    val status: LessonStatus = LessonStatus.NOT_STARTED,
    val completedAt: java.time.Instant? = null,
    val score: Int = 0, // 0-100
    val xpEarned: Int = 0,
    val attempts: Int = 0,
    val bestScore: Int = 0
)

enum class LessonStatus {
    NOT_STARTED,
    IN_PROGRESS,
    COMPLETED,
    MASTERED
}

/**
 * User's progress in a unit
 */
data class UnitProgress(
    val id: Long,
    val userId: Long,
    val unitId: Long,
    val status: UnitStatus = UnitStatus.LOCKED,
    val completedLessons: Int = 0,
    val totalLessons: Int = 0,
    val xpEarned: Int = 0,
    val completedAt: java.time.Instant? = null
)

enum class UnitStatus {
    LOCKED,
    AVAILABLE,
    IN_PROGRESS,
    COMPLETED,
    MASTERED
}

/**
 * User's vocabulary progress (for spaced repetition)
 */
data class VocabularyProgress(
    val id: Long,
    val userId: Long,
    val vocabularyId: Long,
    val strength: Float = 0f, // 0.0 to 1.0
    val timesCorrect: Int = 0,
    val timesIncorrect: Int = 0,
    val lastReviewed: java.time.Instant? = null,
    val nextReviewDate: java.time.Instant? = null,
    val easeFactor: Float = 2.5f, // SM-2 algorithm factor
    val interval: Int = 0, // Days until next review
    val isLearned: Boolean = false
)

/**
 * User's grammar progress
 */
data class GrammarProgress(
    val id: Long,
    val userId: Long,
    val grammarId: Long,
    val understanding: Float = 0f, // 0.0 to 1.0
    val timesPracticed: Int = 0,
    val timesCorrect: Int = 0,
    val timesIncorrect: Int = 0,
    val lastPracticed: java.time.Instant? = null,
    val isMastered: Boolean = false
)

/**
 * Achievement definition
 */
data class Achievement(
    val id: Long,
    val name: String,
    val description: String,
    val icon: String = "",
    val category: AchievementCategory,
    val requirementType: AchievementRequirementType,
    val requirementValue: Int,
    val xpReward: Int = 0
)

enum class AchievementCategory {
    LESSONS,
    XP,
    STREAK,
    VOCABULARY,
    GRAMMAR,
    LISTENING,
    SPEAKING,
    READING,
    WRITING,
    SPECIAL
}

enum class AchievementRequirementType {
    COMPLETE_LESSONS,
    EARN_XP,
    MAINTAIN_STREAK,
    LEARN_WORDS,
    MASTER_GRAMMAR,
    PERFECT_SCORE,
    CONSECUTIVE_DAYS
}

/**
 * User's unlocked achievements
 */
data class UserAchievement(
    val id: Long,
    val userId: Long,
    val achievementId: Long,
    val unlockedAt: java.time.Instant
)

/**
 * Study session record
 */
data class StudySession(
    val id: Long,
    val userId: Long,
    val startTime: java.time.Instant,
    val endTime: java.time.Instant?,
    val xpEarned: Int = 0,
    val lessonsCompleted: Int = 0,
    val exercisesAttempted: Int = 0,
    val exercisesCorrect: Int = 0
)

/**
 * Daily goal configuration
 */
data class DailyGoal(
    val id: Long,
    val userId: Long,
    val targetXp: Int,
    val date: LocalDate,
    val progress: Int = 0,
    val isCompleted: Boolean = false
)
