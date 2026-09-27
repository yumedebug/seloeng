package com.englishmaster.app.data.database

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.room.TypeConverters

@Database(
    entities = [
        CourseEntity::class,
        LevelEntity::class,
        UnitEntity::class,
        LessonEntity::class,
        VocabularyCategoryEntity::class,
        GrammarCategoryEntity::class,
        VocabularyEntity::class,
        GrammarEntity::class,
        ExerciseEntity::class,
        UserEntity::class,
        LessonProgressEntity::class,
        UnitProgressEntity::class,
        VocabularyProgressEntity::class,
        GrammarProgressEntity::class,
        AchievementEntity::class,
        UserAchievementEntity::class,
        StudySessionEntity::class,
        DailyGoalEntity::class
    ],
    version = 1,
    exportSchema = false
)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun courseDao(): CourseDao
    abstract fun levelDao(): LevelDao
    abstract fun unitDao(): UnitDao
    abstract fun lessonDao(): LessonDao
    abstract fun vocabularyDao(): VocabularyDao
    abstract fun grammarDao(): GrammarDao
    abstract fun exerciseDao(): ExerciseDao
    abstract fun userDao(): UserDao
    abstract fun lessonProgressDao(): LessonProgressDao
    abstract fun unitProgressDao(): UnitProgressDao
    abstract fun vocabularyProgressDao(): VocabularyProgressDao
    abstract fun grammarProgressDao(): GrammarProgressDao
    abstract fun achievementDao(): AchievementDao
    abstract fun userAchievementDao(): UserAchievementDao
    abstract fun studySessionDao(): StudySessionDao
    abstract fun dailyGoalDao(): DailyGoalDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        fun getDatabase(context: Context): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "english_master_database"
                )
                    .fallbackToDestructiveMigration()
                    .build()
                INSTANCE = instance
                instance
            }
        }
    }
}
