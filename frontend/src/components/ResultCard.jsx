import React from "react"
import ConfidenceBar from "./ConfidenceBar";

export default function ResultCard({ sentiment, confidenceScores }) {
    const [negativeScore, positiveScore] = confidenceScores;
    const confidence = Math.max(negativeScore, positiveScore)

    return (
        // <div className="result-card" style = {{ borderColor: sentimentColor}}>
        <div className="result-card">
            <ConfidenceBar sentiment={sentiment} confidence={confidence}/>
        </div>
    )
}