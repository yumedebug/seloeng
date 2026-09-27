package com.englishmaster.app.data.repository

import com.englishmaster.app.data.database.*
import com.englishmaster.app.domain.model.*
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class GrammarRepository(private val database: AppDatabase) {
    private val dao = database.grammarDao()
    
    val allGrammar: Flow<List<Grammar>> = dao.getAllGrammar().map { entities ->
        entities.map { it.toDomain() }
    }
    
    fun getGrammarByCategory(categoryId: Long): Flow<List<Grammar>> {
        return dao.getGrammarByCategory(categoryId).map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    suspend fun getGrammarById(id: Long): Grammar? {
        return dao.getGrammarById(id)?.toDomain()
    }
    
    suspend fun insertAll(grammar: List<Grammar>) {
        dao.insertAll(grammar.map { it.toEntity() })
    }
}

private fun GrammarEntity.toDomain(): Grammar {
    val examplesList = if (examples.isEmpty()) emptyList()
    else examples.split("|||").map { parts ->
        val p = parts.split("::")
        GrammarExample(p[0], p.getOrElse(1) { "" }, p.getOrElse(2) { "" })
    }
    
    return Grammar(
        id = id,
        name = name,
        description = description,
        explanation = explanation,
        structure = structure,
        usage = usage,
        examples = examplesList,
        notes = notes,
        difficulty = difficulty,
        relatedGrammarIds = relatedGrammarIds.split("|").filter { it.isNotEmpty() }.map { it.toLong() },
        categoryId = categoryId
    )
}

private fun Grammar.toEntity(): GrammarEntity = GrammarEntity(
    id = id,
    name = name,
    description = description,
    explanation = explanation,
    structure = structure,
    usage = usage,
    examples = examples.joinToString("|||") { "${it.sentence}::${it.translation}::${it.highlight}" },
    notes = notes,
    difficulty = difficulty,
    relatedGrammarIds = relatedGrammarIds.joinToString("|"),
    categoryId = categoryId
)
