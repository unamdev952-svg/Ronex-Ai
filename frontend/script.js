const API_BASE_URL = "http://127.0.0.1:8000/api/v1";

// Application State Tracking Variables
let currentUser = null;
let sessionToken = null;
let conversationHistory = [];

// DOM Elements
const loginOverlay = document.getElementById("login-overlay");
const appContainer = document.getElementById("app-container");
const usernameInput = document.getElementById("username-input");
const loginBtn = document.getElementById("login-btn");
const loginError = document.getElementById("login-error");
const userDisplayName = document.getElementById("user-display-name");
const logoutBtn = document.getElementById("logout-btn");
const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");

// Handle Application Login Event Sequence
loginBtn.addEventListener("click", async () => {
    const username = usernameInput.value.trim();
    if (!username) {
        loginError.textContent = "Please provide a valid name to sign in.";
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username })
        });

        if (!response.ok) {
            throw new Error("Authentication failed at server cluster level.");
        }

        const data = await response.json();
        
        // Cache session tokens
        currentUser = data.username;
        sessionToken = data.token;

        // UI Transitions
        userDisplayName.textContent = `Welcome, ${currentUser}`;
        loginOverlay.classList.add("hidden");
        appContainer.classList.remove("hidden");
        
        // Push initial greeting from the dynamic runtime identity
        appendMessage("bot", `Hello ${currentUser}, I am Ronex AI. How can I help you today?`);
        
    } catch (err) {
        loginError.textContent = "Could not reach Ronex Backend. Make sure Uvicorn is running.";
        console.error(err);
    }
});

// Appending Messages cleanly directly inside the view viewport window DOM tree
function appendMessage(sender, text) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", sender === "user" ? "user-msg" : "bot-msg");
    
    const p = document.createElement("p");
    p.textContent = text;
    
    msgDiv.appendChild(p);
    chatBox.appendChild(msgDiv);
    
    // Auto-scroll layout to latest messages instantly
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Handling Chat Submissions to Ronex Backend Engine Core API
chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const messageText = messageInput.value.trim();
    if (!messageText) return;

    // Display client input instantaneously
    appendMessage("user", messageText);
    messageInput.value = "";

    // Track thread stack history array matrix parameters
    conversationHistory.push({ role: "user", content: messageText });

    try {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${sessionToken}`
            },
            body: JSON.stringify({
                messages: conversationHistory,
                stream: false
            })
        });

        if (!response.ok) {
            throw new Error("Failed to receive context frame token back from application server.");
        }

        const data = await response.json();
        
        // Render system answer and commit back onto processing logs stack arrays
        appendMessage("bot", data.answer);
        conversationHistory.push({ role: "assistant", content: data.answer });

    } catch (err) {
        appendMessage("bot", "Error: Connection lost with Ronex AI API backend gateway router components.");
        console.error(err);
    }
});

// Handling Logout Events
logoutBtn.addEventListener("click", () => {
    currentUser = null;
    sessionToken = null;
    conversationHistory = [];
    chatBox.innerHTML = '<div class="message system-msg"><p>System secure connection established. Welcome to Ronex AI platform interface.</p></div>';
    usernameInput.value = "";
    loginError.textContent = "";
    appContainer.classList.add("hidden");
    loginOverlay.classList.remove("hidden");
});
      
