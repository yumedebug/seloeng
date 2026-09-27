package com.englishmaster.app.data.database

import androidx.room.*
import com.englishmaster.app.domain.model.*

// ==================== Entity Classes ====================

@Entity(tableName = "courses")
data class CourseEntity(
    @PrimaryKey val id: Long,
    val name: String,
    val description: String = "",
    val language: String = "en",
    val icon: String = ""
)

@Entity(tableName = "levels")
data class LevelEntity(
    @PrimaryKey val id: Long,
    val courseId: Long,
    val name: String,
    val description: String = "",
    val order: Int = 0,
    val icon: String = "",
    val color: String = ""
)

@Entity(tableName = "units")
data class UnitEntity(
    @PrimaryKey val id: Long,
    val levelId: Long,
    val name: String,
    val description: String = "",
    val order: Int = 0,
    val requiredXp: Int = 0,
    val icon: String = ""
)

@Entity(tableName = "lessons")
data class LessonEntity(
    @PrimaryKey val id: Long,
    val unitId: Long,
    val name: String,
    val description: String = "",
    val order: Int = 0,
    val lessonType: LessonType = LessonType.NORMAL,
    val requiredXp: Int = 0,
    val estimatedDuration: Int = 5
)

@Entity(tableName = "vocabulary_categories")
data class VocabularyCategoryEntity(
    @PrimaryKey val id: Long,
    val name: String,
    val description: String = "",
    val icon: String = "",
    val order: Int = 0
)

@Entity(tableName = "grammar_categories")
data class GrammarCategoryEntity(
    @PrimaryKey val id: Long,
    val name: String,
    val description: String = "",
    val icon: String = "",
    val order: Int = 0
)

@Entity(tableName = "vocabulary")
data class VocabularyEntity(
    @PrimaryKey val id: Long,
    val word: String,
    val meaning: String,
    val partOfSpeech: PartOfSpeech,
    val pronunciation: String = "",
    val ipa: String = "",
    val difficulty: Int = 1,
    val frequency: Int = 1,
    val exampleSentence: String = "",
    val exampleTranslation: String = "",
    val synonyms: String = "", // Stored as delimited string
    val antonyms: String = "",
    val relatedWords: String = "",
    val plural: String? = null,
    val pastForm: String? = null,
    val pastParticiple: String? = null,
    val presentParticiple: String? = null,
    val tags: String = "",
    val categoryId: Long? = null
)

@Entity(tableName = "grammar")
data class GrammarEntity(
    @PrimaryKey val id: Long,
    val name: String,
    val description: String,
    val explanation: String,
    val structure: String = "",
    val usage: String = "",
    val examples: String = "", // Stored as delimited string
    val notes: String = "",
    val difficulty: Int = 1,
    val relatedGrammarIds: String = "",
    val categoryId: Long? = null
)

@Entity(tableName = "exercises")
data class ExerciseEntity(
    @PrimaryKey val id: Long,
    val lessonId: Long,
    val exerciseType: String, // Type discriminator
    val order: Int,
    val question: String,
    val instruction: String,
    val xpReward: Int,
    val difficulty: Int,
    val data: String // JSON-like string for type-specific data
)

@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: Long = 1,
    val name: String = "Learner",
    val createdAt: String, // LocalDate as string
    val currentLevelId: Long = 1,
    val currentUnitId: Long = 1,
    val totalXp: Int = 0,
    val currentStreak: Int = 0,
    val longestStreak: Int = 0,
    val lastStudyDate: String? = null, // LocalDate as string
    val lives: Int = 5,
    val maxLives: Int = 5,
    val dailyGoalXp: Int = 20,
    val dailyGoalProgress: Int = 0,
    val isOnboardingComplete: Boolean = false,
    val experienceLevel: UserExperienceLevel = UserExperienceLevel.BEGINNER
)

@Entity(tableName = "lesson_progress")
data class LessonProgressEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val lessonId: Long,
    val status: LessonStatus = LessonStatus.NOT_STARTED,
    val completedAt: String? = null, // Instant as string
    val score: Int = 0,
    val xpEarned: Int = 0,
    val attempts: Int = 0,
    val bestScore: Int = 0
)

@Entity(tableName = "unit_progress")
data class UnitProgressEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val unitId: Long,
    val status: UnitStatus = UnitStatus.LOCKED,
    val completedLessons: Int = 0,
    val totalLessons: Int = 0,
    val xpEarned: Int = 0,
    val completedAt: String? = null
)

@Entity(tableName = "vocabulary_progress")
data class VocabularyProgressEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val vocabularyId: Long,
    val strength: Float = 0f,
    val timesCorrect: Int = 0,
    val timesIncorrect: Int = 0,
    val lastReviewed: String? = null,
    val nextReviewDate: String? = null,
    val easeFactor: Float = 2.5f,
    val interval: Int = 0,
    val isLearned: Boolean = false
)

@Entity(tableName = "grammar_progress")
data class GrammarProgressEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val grammarId: Long,
    val understanding: Float = 0f,
    val timesPracticed: Int = 0,
    val timesCorrect: Int = 0,
    val timesIncorrect: Int = 0,
    val lastPracticed: String? = null,
    val isMastered: Boolean = false
)

@Entity(tableName = "achievements")
data class AchievementEntity(
    @PrimaryKey val id: Long,
    val name: String,
    val description: String,
    val icon: String = "",
    val category: AchievementCategory,
    val requirementType: AchievementRequirementType,
    val requirementValue: Int,
    val xpReward: Int = 0
)

@Entity(tableName = "user_achievements")
data class UserAchievementEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val achievementId: Long,
    val unlockedAt: String // Instant as string
)

@Entity(tableName = "study_sessions")
data class StudySessionEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val startTime: String, // Instant as string
    val endTime: String?,
    val xpEarned: Int = 0,
    val lessonsCompleted: Int = 0,
    val exercisesAttempted: Int = 0,
    val exercisesCorrect: Int = 0
)

@Entity(tableName = "daily_goals")
data class DailyGoalEntity(
    @PrimaryKey val id: Long,
    val userId: Long,
    val targetXp: Int,
    val date: String, // LocalDate as string
    val progress: Int = 0,
    val isCompleted: Boolean = false
)
