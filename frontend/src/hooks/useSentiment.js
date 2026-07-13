import { useState } from 'react';
import { predictSentiment } from '../api/sentiment';

export function useSentiment() {
    const [sentiment, setSentiment] = useState(null);
    const [confidenceScores, setConfidenceScores] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    async function analyzeSentiment(text) {
        setLoading(true);
        setError(null);

        try {
            const result = await predictSentiment(text);
            setSentiment(result.sentiment);
            setConfidenceScores(result.confidence_scores);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    return {
        sentiment,
        confidenceScores,
        loading,
        error,
        analyzeSentiment
    }
}