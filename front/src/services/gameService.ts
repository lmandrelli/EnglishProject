import axios from 'axios';

const API_URL = import.meta.env.PROD ? '/api/game' : 'http://localhost:8000/api/game';

export interface CrosswordItem {
    _id: string;
    word: string;
    definition: string;
    difficulty: number;
}

export interface GapFillItem {
    _id: string;
    text: string;
    words: string[];
    definitions: string[];
    difficulty: number;
}

export interface SynonymMatchItem {
    _id: string;
    word: string;
    synonym: string;
    difficulty: number;
}

export interface OddOneOutItem {
    _id: string;
    words: string[];
    correct_index: number;
    explanation: string;
    difficulty: number;
}

export interface VerbConjugationItem {
    _id: string;
    sentence: string;
    verb: string;
    tense: string;
    correct_form: string;
    difficulty: number;
}

export interface PhrasalVerbItem {
    _id: string;
    verb: string;
    particle: string;
    meaning: string;
    example: string;
    difficulty: number;
}

export interface RegionalVariantItem {
    _id: string;
    uk_word: string;
    us_word: string;
    meaning: string;
    difficulty: number;
}

export interface FoodOriginItem {
    _id: string;
    dish_name: string;
    origin_country: string;
    description: string;
    difficulty: number;
}

export interface IdiomItem {
    _id: string;
    expressions: string[];
    fake_index: number;
    explanation: string;
    difficulty: number;
}

export const getVocabularyCrossword = async (difficulty?: number): Promise<CrosswordItem> => {
    const params = difficulty ? { difficulty } : {};
    const response = await axios.get<CrosswordItem>(`${API_URL}/vocabulary/crossword`, { params });
    return response.data;
};

export const getVocabularyGapFill = async (difficulty?: number): Promise<GapFillItem> => {
    const params = difficulty ? { difficulty } : {};
    const response = await axios.get<GapFillItem>(`${API_URL}/vocabulary/gap-fill`, { params });
    return response.data;
};

export const getVocabularySynonyms = async (difficulty?: number, count: number = 5): Promise<SynonymMatchItem[]> => {
    const params: any = { count };
    if (difficulty) params.difficulty = difficulty;
    const response = await axios.get<SynonymMatchItem[]>(`${API_URL}/vocabulary/synonyms`, { params });
    return response.data;
};

export const getGrammarOddOneOut = async (difficulty?: number): Promise<OddOneOutItem> => {
    const params = difficulty ? { difficulty } : {};
    const response = await axios.get<OddOneOutItem>(`${API_URL}/grammar/odd-one-out`, { params });
    return response.data;
};

export const getGrammarVerbConjugation = async (difficulty?: number): Promise<VerbConjugationItem> => {
    const params = difficulty ? { difficulty } : {};
    const response = await axios.get<VerbConjugationItem>(`${API_URL}/grammar/verb-conjugation`, { params });
    return response.data;
};

export const getGrammarPhrasalVerbs = async (difficulty?: number, count: number = 5): Promise<PhrasalVerbItem[]> => {
    const params: any = { count };
    if (difficulty) params.difficulty = difficulty;
    const response = await axios.get<PhrasalVerbItem[]>(`${API_URL}/grammar/phrasal-verbs`, { params });
    return response.data;
};

export const getCultureRegionalVariants = async (difficulty?: number, count: number = 5): Promise<RegionalVariantItem[]> => {
    const params: any = { count };
    if (difficulty) params.difficulty = difficulty;
    const response = await axios.get<RegionalVariantItem[]>(`${API_URL}/culture/regional-variants`, { params });
    return response.data;
};

export const getCultureFoodOrigins = async (difficulty?: number, count: number = 5): Promise<FoodOriginItem[]> => {
    const params: any = { count };
    if (difficulty) params.difficulty = difficulty;
    const response = await axios.get<FoodOriginItem[]>(`${API_URL}/culture/food-origins`, { params });
    return response.data;
};

export const getCultureIdioms = async (difficulty?: number): Promise<IdiomItem> => {
    const params = difficulty ? { difficulty } : {};
    const response = await axios.get<IdiomItem>(`${API_URL}/culture/idioms`, { params });
    return response.data;
};

export const loadGameContent = async (gameMode: string, gameType: string, difficulty?: number): Promise<any> => {
    switch(gameMode) {
        case 'vocabulary':
            switch(gameType) {
                case 'word_puzzle':
                    return getVocabularyCrossword(difficulty);
                case 'word_completion':
                    return getVocabularyGapFill(difficulty);
                case 'word_matching':
                    return getVocabularySynonyms(difficulty);
                default:
                    throw new Error(`Unknown vocabulary game type: ${gameType}`);
            }

        case 'grammar':
            switch(gameType) {
                case 'error_detection':
                    return getGrammarOddOneOut(difficulty);
                case 'verb_forms':
                    return getGrammarVerbConjugation(difficulty);
                case 'verb_combinations':
                    return getGrammarPhrasalVerbs(difficulty);
                default:
                    throw new Error(`Unknown grammar game type: ${gameType}`);
            }
        
        case 'culture':
            switch(gameType) {
                case 'regional_variants':
                    return getCultureRegionalVariants(difficulty);
                case 'cultural_origins':
                    return getCultureFoodOrigins(difficulty);
                case 'expression_mastery':
                    return getCultureIdioms(difficulty);
                default:
                    throw new Error(`Unknown culture game type: ${gameType}`);
            }
        
        default:
            throw new Error(`Unknown game mode: ${gameMode}`);
    }
};
