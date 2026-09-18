package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class LevelRepository(private val database: AppDatabase) {
    private val dao = database.levelDao()
    
    fun getLevelsByCourse(courseId: Long): Flow<List<Level>> {
        return dao.getLevelsByCourse(courseId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getLevelById(id: Long): Level? {
        return dao.getLevelById(id)?.toDomain()
    }
    
    suspend fun insertAll(levels: List<Level>) {
        dao.insertAll(levels.map { it.toEntity() })
    }
}

private fun LevelEntity.toDomain(): Level = Level(id, courseId, name, description, order, icon, color)
private fun Level.toEntity(): LevelEntity = LevelEntity(id, courseId, name, description, order, icon, color)
