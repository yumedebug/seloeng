package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class VocabularyRepository(private val database: AppDatabase) {
    private val dao = database.vocabularyDao()
    
    val allVocabulary: Flow<List<Vocabulary>> = dao.getAllVocabulary().map { entities ->
        entities.map { it.toDomain() }
    }
    
    fun getVocabularyByCategory(categoryId: Long): Flow<List<Vocabulary>> {
        return dao.getVocabularyByCategory(categoryId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getVocabularyById(id: Long): Vocabulary? {
        return dao.getVocabularyById(id)?.toDomain()
    }
    
    suspend fun searchVocabulary(query: String): List<Vocabulary> {
        return dao.searchVocabulary(query).map { it.toDomain() }
    }
    
    suspend fun getVocabularyByDifficulty(maxDifficulty: Int): List<Vocabulary> {
        return dao.getVocabularyByDifficulty(maxDifficulty).map { it.toDomain() }
    }
    
    suspend fun insertAll(vocabulary: List<Vocabulary>) {
        dao.insertAll(vocabulary.map { it.toEntity() })
    }
}

private fun VocabularyEntity.toDomain(): Vocabulary = Vocabulary(
    id = id,
    word = word,
    meaning = meaning,
    partOfSpeech = partOfSpeech,
    pronunciation = pronunciation,
    ipa = ipa,
    difficulty = difficulty,
    frequency = frequency,
    exampleSentence = exampleSentence,
    exampleTranslation = exampleTranslation,
    synonyms = synonyms.split("|").filter { it.isNotEmpty() },
    antonyms = antonyms.split("|").filter { it.isNotEmpty() },
    relatedWords = relatedWords.split("|").filter { it.isNotEmpty() },
    plural = plural,
    pastForm = pastForm,
    pastParticiple = pastParticiple,
    presentParticiple = presentParticiple,
    tags = tags.split("|").filter { it.isNotEmpty() },
    categoryId = categoryId
)

private fun Vocabulary.toEntity(): VocabularyEntity = VocabularyEntity(
    id = id,
    word = word,
    meaning = meaning,
    partOfSpeech = partOfSpeech,
    pronunciation = pronunciation,
    ipa = ipa,
    difficulty = difficulty,
    frequency = frequency,
    exampleSentence = exampleSentence,
    exampleTranslation = exampleTranslation,
    synonyms = synonyms.joinToString("|"),
    antonyms = antonyms.joinToString("|"),
    relatedWords = relatedWords.joinToString("|"),
    plural = plural,
    pastForm = pastForm,
    pastParticiple = pastParticiple,
    presentParticiple = presentParticiple,
    tags = tags.joinToString("|"),
    categoryId = categoryId
)
