const moodMap = {
    happy: {emoji: "😊", color: "yellow"},
    sad: {emoji: "😢", color: "blue"},
    angry: {emoji: "😡", color: "red"},
    confused: {emoji: "🤔", color: "grey"},
    // ... add more moods and their respective emojis and colors
};

const moodInput = document.getElementById('moodInput');
const emojiOutput = document.getElementById('emojiOutput');

moodInput.addEventListener('input', function() {
    let mood = moodInput.value.toLowerCase();
    if(moodMap[mood]) {
        emojiOutput.textContent = moodMap[mood].emoji;
        document.body.style.backgroundColor = moodMap[mood].color;
    } else {
        emojiOutput.textContent = "🤷"; // Default if mood is not found
        document.body.style.backgroundColor = "white";
    }
});