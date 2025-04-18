const API_KEY = "your-openai-api-key-here"; // 🔒 Move this to .env if deploying

async function sendPrompt() {
  const prompt = document.getElementById("promptInput").value;
  const responseBox = document.getElementById("responseBox");

  responseBox.textContent = "⏳ Loading...";

  try {
    const res = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: prompt }]
      })
    });

    const data = await res.json();
    const reply = data.choices[0].message.content;

    responseBox.textContent = reply;
  } catch (error) {
    responseBox.textContent = "❌ Error: " + error.message;
  }
}
