package com.englishmaster.app.domain.model

/**
 * Base interface for all exercise types
 */
sealed class Exercise {
    abstract val id: Long
    abstract val lessonId: Long
    abstract val order: Int
    abstract val question: String
    abstract val instruction: String
    abstract val xpReward: Int
    abstract val difficulty: Int
}

/**
 * Multiple choice question
 */
data class MultipleChoiceExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Select the correct answer",
    override val xpReward: Int = 5,
    override val difficulty: Int = 1,
    val options: List<String>,
    val correctIndex: Int,
    val explanation: String = ""
) : Exercise()

/**
 * Word selection exercise (select words to form a sentence)
 */
data class WordSelectionExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Select the correct words",
    override val xpReward: Int = 5,
    override val difficulty: Int = 2,
    val wordBank: List<String>,
    val correctSequence: List<String>,
    val explanation: String = ""
) : Exercise()

/**
 * Word ordering exercise (arrange words to form a sentence)
 */
data class WordOrderingExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Arrange the words in correct order",
    override val xpReward: Int = 7,
    override val difficulty: Int = 3,
    val scrambledWords: List<String>,
    val correctOrder: List<String>,
    val explanation: String = ""
) : Exercise()

/**
 * Fill in the blank exercise
 */
data class FillInBlankExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String, // Sentence with blank (use ___ for blank)
    override val instruction: String = "Fill in the blank",
    override val xpReward: Int = 5,
    override val difficulty: Int = 2,
    val correctAnswers: List<String>, // Accept multiple correct answers
    val hint: String = "",
    val explanation: String = ""
) : Exercise()

/**
 * Translation exercise
 */
data class TranslationExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String, // Source language sentence
    override val instruction: String = "Translate this sentence",
    override val xpReward: Int = 10,
    override val difficulty: Int = 4,
    val sourceLanguage: String = "ja",
    val targetLanguage: String = "en",
    val correctTranslations: List<String>,
    val acceptableVariations: List<String> = emptyList(),
    val explanation: String = ""
) : Exercise()

/**
 * Listening exercise
 */
data class ListeningExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Listen and select what you hear",
    override val xpReward: Int = 7,
    override val difficulty: Int = 3,
    val audioUrl: String = "", // Can be local resource or TTS
    val audioText: String = "", // Text for TTS
    val options: List<String>,
    val correctIndex: Int,
    val explanation: String = ""
) : Exercise()

/**
 * Spelling exercise
 */
data class SpellingExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Spell the word correctly",
    override val xpReward: Int = 5,
    override val difficulty: Int = 2,
    val correctSpelling: String,
    val hint: String = "",
    val explanation: String = ""
) : Exercise()

/**
 * Matching exercise (match pairs)
 */
data class MatchingExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Match the pairs",
    override val xpReward: Int = 8,
    override val difficulty: Int = 3,
    val pairs: List<Pair<String, String>>, // Left item to Right item
    val explanation: String = ""
) : Exercise()

/**
 * True/False exercise
 */
data class TrueFalseExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Is this statement true or false?",
    override val xpReward: Int = 3,
    override val difficulty: Int = 1,
    val isTrue: Boolean,
    val explanation: String = ""
) : Exercise()

/**
 * Sentence completion exercise
 */
data class SentenceCompletionExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String, // Partial sentence
    override val instruction: String = "Complete the sentence",
    override val xpReward: Int = 7,
    override val difficulty: Int = 3,
    val completions: List<String>, // Acceptable completions
    val hint: String = "",
    val explanation: String = ""
) : Exercise()

/**
 * Speaking exercise (uses speech recognition)
 */
data class SpeakingExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Speak the sentence",
    override val xpReward: Int = 10,
    override val difficulty: Int = 4,
    val targetPhrase: String,
    val acceptableVariations: List<String> = emptyList(),
    val explanation: String = ""
) : Exercise()

/**
 * Reading comprehension exercise
 */
data class ReadingExercise(
    override val id: Long,
    override val lessonId: Long,
    override val order: Int,
    override val question: String,
    override val instruction: String = "Read and answer the question",
    override val xpReward: Int = 10,
    override val difficulty: Int = 5,
    val passage: String,
    val vocabulary: List<VocabularyNote> = emptyList(), // Words that can be tapped for definition
    val questions: List<ReadingQuestion>,
    val explanation: String = ""
) : Exercise()

data class VocabularyNote(
    val word: String,
    val meaning: String,
    val pronunciation: String = ""
)

data class ReadingQuestion(
    val question: String,
    val options: List<String>,
    val correctIndex: Int
)
