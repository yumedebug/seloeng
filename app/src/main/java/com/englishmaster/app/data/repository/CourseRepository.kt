package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class CourseRepository(private val database: AppDatabase) {
    private val dao = database.courseDao()
    
    val allCourses: Flow<List<Course>> = dao.getAllCourses().map { entities ->
        entities.map { it.toDomain() }
    }
    
    suspend fun getCourseById(id: Long): Course? {
        return dao.getCourseById(id)?.toDomain()
    }
    
    suspend fun insertAll(courses: List<Course>) {
        dao.insertAll(courses.map { it.toEntity() })
    }
}

private fun CourseEntity.toDomain(): Course = Course(id, name, description, language, icon)
private fun Course.toEntity(): CourseEntity = CourseEntity(id, name, description, language, icon)
