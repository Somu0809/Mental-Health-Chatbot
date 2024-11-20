document.getElementById("send-btn").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value;
  
    if (userInput.trim() === "") return; // Ensure user input is not empty
  
    // Append user message to chat history
    const chatHistory = document.getElementById("chat-history");
    const userMessage = document.createElement("p");
    userMessage.classList.add("user");
    userMessage.textContent = `User: ${userInput}`; // Corrected template literal usage
    chatHistory.appendChild(userMessage);
  
    // Fetch bot response from the backend
    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
      });
  
      if (!response.ok) {
        throw new Error("Failed to fetch chatbot response.");
      }
  
      const data = await response.json();
  
      // Append bot response to chat history
      const botMessage = document.createElement("p");
      botMessage.classList.add("bot");
      botMessage.textContent = `Chatbot: ${data.response}`; // Corrected template literal usage
      chatHistory.appendChild(botMessage);
  
      // Scroll to the bottom of chat history
      chatHistory.scrollTop = chatHistory.scrollHeight;
    } catch (error) {
      console.error("Error fetching chatbot response:", error);
  
      // Append error message to chat history
      const errorMessage = document.createElement("p");
      errorMessage.classList.add("bot");
      errorMessage.textContent = "Chatbot: Sorry, something went wrong.";
      chatHistory.appendChild(errorMessage);
    }
  
    // Clear user input
    document.getElementById("user-input").value = "";
  });
  