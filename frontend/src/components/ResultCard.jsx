export default function ResultCard({ sentiment, confidenceScores }) {
    const [negativeScore, positiveScore] = confidenceScores;
    const sentimentColor = {
        positive: "#4CAF50",
        negative: "#F44336",
        neutral: "#9E9E9E"
    }[sentiment];

    return (
        <div className="result-card" style = {{ borderColor: sentimentColor}}>
            <h2 style={{ color: sentimentColor}}>
                Sentiment: {sentiment.toUpperCase()}
            </h2>

            <div className="confidence-section">
                <p>Confidence Scores</p>

                <div className="bar">
                    <span>Negative</span>
                    <div className="bar-fill" style={{
                        width: `${negativeScore * 100}%`,
                        background: "#F44336" 
                    }} />
                </div>

                <div className="bar">
                    <span>Positive</span>
                    <div className="bar-fill" style ={{
                        width: `${positiveScore * 100}%`,
                        background: "#4CAF50"
                    }} />
                </div>
            </div>
        </div>
    )
}