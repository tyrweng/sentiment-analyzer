import ConfidenceBar from "./ConfidenceBar";

export default function ResultCard({ sentiment, confidenceScores }) {
    const [negativeScore, positiveScore] = confidenceScores;
    const confidence = Math.max(confidenceScores)

    return (
        <div className="result-card" style = {{ borderColor: sentimentColor}}>
            <SentimentBar sentiment={sentiment} confidence={confidence}/>
        </div>
    )
}