package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class LessonProgressRepository(private val database: AppDatabase) {
    private val dao = database.lessonProgressDao()
    
    fun getProgressByUser(userId: Long): Flow<List<LessonProgress>> {
        return dao.getProgressByUser(userId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getProgress(userId: Long, lessonId: Long): LessonProgress? {
        return dao.getProgress(userId, lessonId)?.toDomain()
    }
    
    suspend fun updateProgress(progress: LessonProgress) {
        val existing = dao.getProgress(progress.userId, progress.lessonId)
        if (existing != null) {
            dao.update(progress.toEntity(existing.id))
        } else {
            dao.insert(progress.toEntity(0))
        }
    }
}

private fun LessonProgressEntity.toDomain(): LessonProgress = LessonProgress(
    id = id,
    userId = userId,
    lessonId = lessonId,
    status = status,
    completedAt = completedAt?.let { java.time.Instant.parse(it) },
    score = score,
    xpEarned = xpEarned,
    attempts = attempts,
    bestScore = bestScore
)

private fun LessonProgress.toEntity(existingId: Long): LessonProgressEntity = LessonProgressEntity(
    id = if (existingId > 0) existingId else System.currentTimeMillis(),
    userId = userId,
    lessonId = lessonId,
    status = status,
    completedAt = completedAt?.toString(),
    score = score,
    xpEarned = xpEarned,
    attempts = attempts,
    bestScore = bestScore
)
