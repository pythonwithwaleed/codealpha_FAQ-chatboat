const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const messages = document.getElementById("messages");
const suggestions = document.getElementById("suggestions");
const sendButton = form.querySelector("button");

function scrollToBottom() {
  messages.scrollTop = messages.scrollHeight;
}

// Adds a message to the chat. Uses textContent so user text is never run as HTML.
function addMessage(text, sender, meta, isError) {
  const wrapper = document.createElement("div");
  wrapper.className = "msg msg--" + sender + (isError ? " msg--error" : "");

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  wrapper.appendChild(bubble);

  if (meta) {
    const metaEl = document.createElement("div");
    metaEl.className = "meta";
    metaEl.textContent = meta;
    wrapper.appendChild(metaEl);
  }

  messages.appendChild(wrapper);
  scrollToBottom();
  return wrapper;
}

function addTyping() {
  const wrapper = document.createElement("div");
  wrapper.className = "msg msg--bot";
  wrapper.innerHTML =
    '<div class="bubble typing" aria-label="Bot is typing"><span></span><span></span><span></span></div>';
  messages.appendChild(wrapper);
  scrollToBottom();
  return wrapper;
}

async function sendMessage(text) {
  addMessage(text, "user");
  suggestions.hidden = true;
  sendButton.disabled = true;
  const typing = addTyping();

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await response.json();
    typing.remove();

    if (!response.ok) {
      addMessage(data.error || "Something went wrong. Please try again.", "bot", null, true);
    } else {
      const meta = data.matched ? "Matched: " + data.matched : null;
      addMessage(data.answer, "bot", meta);
    }
  } catch (err) {
    typing.remove();
    addMessage("Can't reach the server. Check that app.py is running, then try again.", "bot", null, true);
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  input.value = "";
  sendMessage(text);
});

suggestions.addEventListener("click", (event) => {
  const chip = event.target.closest(".chip");
  if (chip) sendMessage(chip.textContent.trim());
});
