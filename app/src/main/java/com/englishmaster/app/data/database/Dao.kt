package com.englishmaster.app.data.database

import androidx.room.*
import kotlinx.coroutines.flow.Flow

@Dao
interface CourseDao {
    @Query("SELECT * FROM courses")
    fun getAllCourses(): Flow<List<CourseEntity>>
    
    @Query("SELECT * FROM courses WHERE id = :id")
    suspend fun getCourseById(id: Long): CourseEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(course: CourseEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(courses: List<CourseEntity>)
}

@Dao
interface LevelDao {
    @Query("SELECT * FROM levels ORDER BY `order`")
    fun getAllLevels(): Flow<List<LevelEntity>>
    
    @Query("SELECT * FROM levels WHERE courseId = :courseId ORDER BY `order`")
    fun getLevelsByCourse(courseId: Long): Flow<List<LevelEntity>>
    
    @Query("SELECT * FROM levels WHERE id = :id")
    suspend fun getLevelById(id: Long): LevelEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(level: LevelEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(levels: List<LevelEntity>)
}

@Dao
interface UnitDao {
    @Query("SELECT * FROM units ORDER BY levelId, `order`")
    fun getAllUnits(): Flow<List<UnitEntity>>
    
    @Query("SELECT * FROM units WHERE levelId = :levelId ORDER BY `order`")
    fun getUnitsByLevel(levelId: Long): Flow<List<UnitEntity>>
    
    @Query("SELECT * FROM units WHERE id = :id")
    suspend fun getUnitById(id: Long): UnitEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(unit: UnitEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(units: List<UnitEntity>)
}

@Dao
interface LessonDao {
    @Query("SELECT * FROM lessons WHERE unitId = :unitId ORDER BY `order`")
    fun getLessonsByUnit(unitId: Long): Flow<List<LessonEntity>>
    
    @Query("SELECT * FROM lessons WHERE id = :id")
    suspend fun getLessonById(id: Long): LessonEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(lesson: LessonEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(lessons: List<LessonEntity>)
}

@Dao
interface VocabularyDao {
    @Query("SELECT * FROM vocabulary ORDER BY frequency")
    fun getAllVocabulary(): Flow<List<VocabularyEntity>>
    
    @Query("SELECT * FROM vocabulary WHERE categoryId = :categoryId")
    fun getVocabularyByCategory(categoryId: Long): Flow<List<VocabularyEntity>>
    
    @Query("SELECT * FROM vocabulary WHERE id = :id")
    suspend fun getVocabularyById(id: Long): VocabularyEntity?
    
    @Query("SELECT * FROM vocabulary WHERE word LIKE :query || '%' LIMIT 20")
    suspend fun searchVocabulary(query: String): List<VocabularyEntity>
    
    @Query("SELECT * FROM vocabulary WHERE difficulty <= :maxDifficulty ORDER BY frequency LIMIT 50")
    suspend fun getVocabularyByDifficulty(maxDifficulty: Int): List<VocabularyEntity>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(vocabulary: VocabularyEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(vocabulary: List<VocabularyEntity>)
}

@Dao
interface GrammarDao {
    @Query("SELECT * FROM grammar ORDER BY difficulty")
    fun getAllGrammar(): Flow<List<GrammarEntity>>
    
    @Query("SELECT * FROM grammar WHERE categoryId = :categoryId")
    fun getGrammarByCategory(categoryId: Long): Flow<List<GrammarEntity>>
    
    @Query("SELECT * FROM grammar WHERE id = :id")
    suspend fun getGrammarById(id: Long): GrammarEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(grammar: GrammarEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(grammar: List<GrammarEntity>)
}

@Dao
interface ExerciseDao {
    @Query("SELECT * FROM exercises WHERE lessonId = :lessonId ORDER BY `order`")
    fun getExercisesByLesson(lessonId: Long): Flow<List<ExerciseEntity>>
    
    @Query("SELECT * FROM exercises WHERE id = :id")
    suspend fun getExerciseById(id: Long): ExerciseEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(exercise: ExerciseEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(exercises: List<ExerciseEntity>)
    
    @Query("DELETE FROM exercises WHERE lessonId = :lessonId")
    suspend fun deleteByLessonId(lessonId: Long)
}

@Dao
interface UserDao {
    @Query("SELECT * FROM users WHERE id = 1")
    fun getCurrentUser(): Flow<UserEntity?>
    
    @Query("SELECT * FROM users WHERE id = 1")
    suspend fun getUserById(id: Long = 1): UserEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(user: UserEntity)
    
    @Update
    suspend fun update(user: UserEntity)
}

@Dao
interface LessonProgressDao {
    @Query("SELECT * FROM lesson_progress WHERE userId = :userId")
    fun getProgressByUser(userId: Long): Flow<List<LessonProgressEntity>>
    
    @Query("SELECT * FROM lesson_progress WHERE userId = :userId AND lessonId = :lessonId")
    suspend fun getProgress(userId: Long, lessonId: Long): LessonProgressEntity?
    
    @Query("SELECT * FROM lesson_progress WHERE lessonId = :lessonId")
    suspend fun getProgressByLesson(lessonId: Long): LessonProgressEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(progress: LessonProgressEntity)
    
    @Update
    suspend fun update(progress: LessonProgressEntity)
}

@Dao
interface UnitProgressDao {
    @Query("SELECT * FROM unit_progress WHERE userId = :userId")
    fun getProgressByUser(userId: Long): Flow<List<UnitProgressEntity>>
    
    @Query("SELECT * FROM unit_progress WHERE userId = :userId AND unitId = :unitId")
    suspend fun getProgress(userId: Long, unitId: Long): UnitProgressEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(progress: UnitProgressEntity)
    
    @Update
    suspend fun update(progress: UnitProgressEntity)
}

@Dao
interface VocabularyProgressDao {
    @Query("SELECT * FROM vocabulary_progress WHERE userId = :userId")
    fun getProgressByUser(userId: Long): Flow<List<VocabularyProgressEntity>>
    
    @Query("SELECT * FROM vocabulary_progress WHERE userId = :userId AND vocabularyId = :vocabularyId")
    suspend fun getProgress(userId: Long, vocabularyId: Long): VocabularyProgressEntity?
    
    @Query("SELECT * FROM vocabulary_progress WHERE userId = :userId AND nextReviewDate IS NOT NULL AND nextReviewDate <= :now ORDER BY nextReviewDate")
    suspend fun getDueForReview(userId: Long, now: String): List<VocabularyProgressEntity>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(progress: VocabularyProgressEntity)
    
    @Update
    suspend fun update(progress: VocabularyProgressEntity)
}

@Dao
interface GrammarProgressDao {
    @Query("SELECT * FROM grammar_progress WHERE userId = :userId")
    fun getProgressByUser(userId: Long): Flow<List<GrammarProgressEntity>>
    
    @Query("SELECT * FROM grammar_progress WHERE userId = :userId AND grammarId = :grammarId")
    suspend fun getProgress(userId: Long, grammarId: Long): GrammarProgressEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(progress: GrammarProgressEntity)
    
    @Update
    suspend fun update(progress: GrammarProgressEntity)
}

@Dao
interface AchievementDao {
    @Query("SELECT * FROM achievements")
    fun getAllAchievements(): Flow<List<AchievementEntity>>
    
    @Query("SELECT * FROM achievements WHERE id = :id")
    suspend fun getAchievementById(id: Long): AchievementEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(achievement: AchievementEntity)
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(achievements: List<AchievementEntity>)
}

@Dao
interface UserAchievementDao {
    @Query("SELECT * FROM user_achievements WHERE userId = :userId")
    fun getUserAchievements(userId: Long): Flow<List<UserAchievementEntity>>
    
    @Query("SELECT * FROM user_achievements WHERE userId = :userId AND achievementId = :achievementId")
    suspend fun hasAchievement(userId: Long, achievementId: Long): UserAchievementEntity?
    
    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun insert(userAchievement: UserAchievementEntity)
}

@Dao
interface StudySessionDao {
    @Query("SELECT * FROM study_sessions WHERE userId = :userId ORDER BY startTime DESC LIMIT 30")
    fun getRecentSessions(userId: Long): Flow<List<StudySessionEntity>>
    
    @Insert
    suspend fun insert(session: StudySessionEntity)
    
    @Update
    suspend fun update(session: StudySessionEntity)
}

@Dao
interface DailyGoalDao {
    @Query("SELECT * FROM daily_goals WHERE userId = :userId AND date = :date")
    suspend fun getDailyGoal(userId: Long, date: String): DailyGoalEntity?
    
    @Query("SELECT * FROM daily_goals WHERE userId = :userId ORDER BY date DESC LIMIT 7")
    fun getRecentGoals(userId: Long): Flow<List<DailyGoalEntity>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(goal: DailyGoalEntity)
    
    @Update
    suspend fun update(goal: DailyGoalEntity)
}
