package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class UnitProgressRepository(private val database: AppDatabase) {
    private val dao = database.unitProgressDao()
    
    fun getProgressByUser(userId: Long): Flow<List<UnitProgress>> {
        return dao.getProgressByUser(userId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getProgress(userId: Long, unitId: Long): UnitProgress? {
        return dao.getProgress(userId, unitId)?.toDomain()
    }
    
    suspend fun updateProgress(progress: UnitProgress) {
        val existing = dao.getProgress(progress.userId, progress.unitId)
        if (existing != null) {
            dao.update(progress.toEntity(existing.id))
        } else {
            dao.insert(progress.toEntity(0))
        }
    }
}

private fun UnitProgressEntity.toDomain(): UnitProgress = UnitProgress(
    id = id,
    userId = userId,
    unitId = unitId,
    status = status,
    completedLessons = completedLessons,
    totalLessons = totalLessons,
    xpEarned = xpEarned,
    completedAt = completedAt?.let { java.time.Instant.parse(it) }
)

private fun UnitProgress.toEntity(existingId: Long): UnitProgressEntity = UnitProgressEntity(
    id = if (existingId > 0) existingId else System.currentTimeMillis(),
    userId = userId,
    unitId = unitId,
    status = status,
    completedLessons = completedLessons,
    totalLessons = totalLessons,
    xpEarned = xpEarned,
    completedAt = completedAt?.toString()
)
