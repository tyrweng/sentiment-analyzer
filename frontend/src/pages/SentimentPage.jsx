import { useState } from 'react';
import { useSentiment } from '../hooks/useSentiment';
import InputBox from '../components/InputBox';
import ResultCard from '../components/ResultCard';
import ConfidenceBar from '../components/ConfidenceBar';

export default function SentimentPage() {
    const [text, setText] = useState('');
    const {
        sentiment,
        confidenceScores,
        loading,
        error,
        debouncedAnalyzeSentiment
    } = useSentiment();

    return (
        <div className="sentiment-page">
            <h1>Sentiment Analyzer</h1>

            <InputBox
                value={text}
                onChange={(t) => {
                    setText(t);
                    debouncedAnalyzeSentiment(t);
                }}
            />

            {loading && <p>Analyzing sentiment...</p>}
            {error && <p className="error">Error: {error}</p>}
            
            {sentiment && confidenceScores && (
                <ResultCard
                    sentiment={sentiment}
                    confidenceScores={confidenceScores}
                />
            )}
        </div>
    )
}