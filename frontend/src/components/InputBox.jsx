export default function InputBox({ value, onChange }) {
    return (
        <div className="input-box">
            <textarea
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder="Type something..."
                rows={5}
            />
        </div>
    )
}