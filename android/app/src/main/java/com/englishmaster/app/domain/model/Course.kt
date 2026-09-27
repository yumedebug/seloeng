package com.englishmaster.app.domain.model

/**
 * Represents a course (English is the only course for now)
 */
data class Course(
    val id: Long,
    val name: String,
    val description: String = "",
    val language: String = "en",
    val icon: String = ""
)
