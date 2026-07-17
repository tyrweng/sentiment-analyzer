import React from "react"
import SentimentPage from "./pages/SentimentPage"

export default function App() {
    return (
        <div className="app-container">
            <header className="app-header">
                <h1>Sentiment Analyzer</h1>
            </header>

            <main className="app-main">
                <SentimentPage />
            </main>
        </div>
    )
} 