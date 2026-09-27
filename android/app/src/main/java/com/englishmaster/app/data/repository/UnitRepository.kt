package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class UnitRepository(private val database: AppDatabase) {
    private val dao = database.unitDao()
    
    fun getUnitsByLevel(levelId: Long): Flow<List<Unit>> {
        return dao.getUnitsByLevel(levelId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getUnitById(id: Long): Unit? {
        return dao.getUnitById(id)?.toDomain()
    }
    
    suspend fun insertAll(units: List<Unit>) {
        dao.insertAll(units.map { it.toEntity() })
    }
}

private fun UnitEntity.toDomain(): Unit = Unit(id, levelId, name, description, order, requiredXp, icon)
private fun Unit.toEntity(): UnitEntity = UnitEntity(id, levelId, name, description, order, requiredXp, icon)
