package com.englishmaster.app.data.database

import androidx.room.*
import com.englishmaster.app.domain.model.*
import java.time.Instant
import java.time.LocalDate

// ==================== Converters ====================
class Converters {
    @TypeConverter
    fun fromStringList(value: List<String>): String {
        return value.joinToString("|")
    }

    @TypeConverter
    fun toStringList(value: String): List<String> {
        return if (value.isEmpty()) emptyList() else value.split("|")
    }

    @TypeConverter
    fun fromGrammarExampleList(value: List<GrammarExample>): String {
        return value.joinToString("|||") { "${it.sentence}::${it.translation}::${it.highlight}" }
    }

    @TypeConverter
    fun toGrammarExampleList(value: String): List<GrammarExample> {
        return if (value.isEmpty()) emptyList()
        else value.split("|||").map { parts ->
            val p = parts.split("::")
            GrammarExample(p[0], p.getOrElse(1) { "" }, p.getOrElse(2) { "" })
        }
    }

    @TypeConverter
    fun fromPartOfSpeech(value: PartOfSpeech): String = value.name

    @TypeConverter
    fun toPartOfSpeech(value: String): PartOfSpeech = PartOfSpeech.valueOf(value)

    @TypeConverter
    fun fromLessonType(value: LessonType): String = value.name

    @TypeConverter
    fun toLessonType(value: String): LessonType = LessonType.valueOf(value)

    @TypeConverter
    fun fromUnitStatus(value: UnitStatus): String = value.name

    @TypeConverter
    fun toUnitStatus(value: String): UnitStatus = UnitStatus.valueOf(value)

    @TypeConverter
    fun fromLessonStatus(value: LessonStatus): String = value.name

    @TypeConverter
    fun toLessonStatus(value: String): LessonStatus = LessonStatus.valueOf(value)

    @TypeConverter
    fun fromAchievementCategory(value: AchievementCategory): String = value.name

    @TypeConverter
    fun toAchievementCategory(value: String): AchievementCategory = AchievementCategory.valueOf(value)

    @TypeConverter
    fun fromAchievementRequirementType(value: AchievementRequirementType): String = value.name

    @TypeConverter
    fun toAchievementRequirementType(value: String): AchievementRequirementType =
        AchievementRequirementType.valueOf(value)

    @TypeConverter
    fun fromUserExperienceLevel(value: UserExperienceLevel): String = value.name

    @TypeConverter
    fun toUserExperienceLevel(value: String): UserExperienceLevel =
        UserExperienceLevel.valueOf(value)

    @TypeConverter
    fun fromLocalDate(value: LocalDate): String = value.toString()

    @TypeConverter
    fun toLocalDate(value: String): LocalDate = LocalDate.parse(value)

    @TypeConverter
    fun fromInstant(value: Instant?): String? = value?.toString()

    @TypeConverter
    fun toInstant(value: String?): Instant? = value?.let { Instant.parse(it) }

    @TypeConverter
    fun fromVocabularyNoteList(value: List<VocabularyNote>): String {
        return value.joinToString("|||") { "${it.word}::${it.meaning}::${it.pronunciation}" }
    }

    @TypeConverter
    fun toVocabularyNoteList(value: String): List<VocabularyNote> {
        return if (value.isEmpty()) emptyList()
        else value.split("|||").map { parts ->
            val p = parts.split("::")
            VocabularyNote(p[0], p.getOrElse(1) { "" }, p.getOrElse(2) { "" })
        }
    }

    @TypeConverter
    fun fromReadingQuestionList(value: List<ReadingQuestion>): String {
        return value.joinToString("|||") { q ->
            "${q.question}::${q.correctIndex}::${q.options.joinToString("|")}"
        }
    }

    @TypeConverter
    fun toReadingQuestionList(value: String): List<ReadingQuestion> {
        return if (value.isEmpty()) emptyList()
        else value.split("|||").map { parts ->
            val p = parts.split("::")
            val options = p.getOrElse(2) { "" }.split("|")
            ReadingQuestion(p[0], options, p.getOrElse(1) { "0" }.toInt())
        }
    }
}
