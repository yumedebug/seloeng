package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class LessonRepository(private val database: AppDatabase) {
    private val dao = database.lessonDao()
    
    fun getLessonsByUnit(unitId: Long): Flow<List<Lesson>> {
        return dao.getLessonsByUnit(unitId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getLessonById(id: Long): Lesson? {
        return dao.getLessonById(id)?.toDomain()
    }
    
    suspend fun insertAll(lessons: List<Lesson>) {
        dao.insertAll(lessons.map { it.toEntity() })
    }
}

private fun LessonEntity.toDomain(): Lesson = 
    Lesson(id, unitId, name, description, order, lessonType, requiredXp, estimatedDuration)

private fun Lesson.toEntity(): LessonEntity = 
    LessonEntity(id, unitId, name, description, order, lessonType, requiredXp, estimatedDuration)
