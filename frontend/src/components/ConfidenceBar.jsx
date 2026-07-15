export default function ConfidenceBar({ sentiment, confidences }){
    const sentimentColor = {
        positive: "#4CAF50",
        negative: "#F44336",
        neutral: "#9E9E9E"
    }[sentiment];

    const percent = Math.round(confidence * 100);

    return (
        <div className="sentiment-bar">
            <div className="sentiment-label" style={{ color: sentimentColor}}>
                {sentiment.toUpperCase()} - {percent}%
            </div>

            <div className="bar-track">
                <div className="bar-fill" style={{ width: `${percent}`, background: sentimentColor}}/>            </div>
        </div>
    )
}