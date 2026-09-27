package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class UserRepository(private val database: AppDatabase) {
    private val dao = database.userDao()
    
    val currentUser: Flow<User> = dao.getCurrentUser().map { entity ->
        entity?.toDomain() ?: User()
    }
    
    suspend fun getUser(): User {
        return dao.getUserById()?.toDomain() ?: User()
    }
    
    suspend fun updateUser(user: User) {
        dao.update(user.toEntity())
    }
    
    suspend fun initializeUser() {
        if (dao.getUserById() == null) {
            dao.insert(User().toEntity())
        }
    }
}

private fun UserEntity.toDomain(): User = User(
    id = id,
    name = name,
    createdAt = java.time.LocalDate.parse(createdAt),
    currentLevelId = currentLevelId,
    currentUnitId = currentUnitId,
    totalXp = totalXp,
    currentStreak = currentStreak,
    longestStreak = longestStreak,
    lastStudyDate = lastStudyDate?.let { java.time.LocalDate.parse(it) },
    lives = lives,
    maxLives = maxLives,
    dailyGoalXp = dailyGoalXp,
    dailyGoalProgress = dailyGoalProgress,
    isOnboardingComplete = isOnboardingComplete,
    experienceLevel = experienceLevel
)

private fun User.toEntity(): UserEntity = UserEntity(
    id = id,
    name = name,
    createdAt = createdAt.toString(),
    currentLevelId = currentLevelId,
    currentUnitId = currentUnitId,
    totalXp = totalXp,
    currentStreak = currentStreak,
    longestStreak = longestStreak,
    lastStudyDate = lastStudyDate?.toString(),
    lives = lives,
    maxLives = maxLives,
    dailyGoalXp = dailyGoalXp,
    dailyGoalProgress = dailyGoalProgress,
    isOnboardingComplete = isOnboardingComplete,
    experienceLevel = experienceLevel
)
