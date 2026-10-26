const DEFAULTS = [
  { name: "Claude", url: "https://claude.ai" },
  { name: "ChatGPT", url: "https://chatgpt.com" },
  { name: "Gemini", url: "https://gemini.google.com" },
  { name: "Perplexity", url: "https://www.perplexity.ai" },
  { name: "Copilot", url: "https://copilot.microsoft.com" },
  { name: "Grok", url: "https://grok.com" },
  { name: "DeepSeek", url: "https://chat.deepseek.com" },
  { name: "Mistral", url: "https://chat.mistral.ai" },
  { name: "Meta AI", url: "https://www.meta.ai" },
  { name: "Poe", url: "https://poe.com" },
  { name: "NotebookLM", url: "https://notebooklm.google.com" },
  { name: "Midjourney", url: "https://www.midjourney.com" }
];

const $ = (id) => document.getElementById(id);
const grid = $("grid");
const editBtn = $("editBtn");
const editPanel = $("editPanel");
const msg = $("msg");

let links = [];
let editing = false;

function withIds(list) {
  return list.map((l) => ({ id: l.id || crypto.randomUUID(), name: l.name, url: l.url }));
}

async function load() {
  try {
    const data = await chrome.storage.sync.get("links");
    links = Array.isArray(data.links) ? data.links : withIds(DEFAULTS);
  } catch (e) {
    links = withIds(DEFAULTS);
  }
  render();
}

async function save() {
  try {
    await chrome.storage.sync.set({ links });
  } catch (e) {
    setMsg("Could not save. Storage is full or unavailable.", "err");
  }
}

function setMsg(text, type) {
  msg.textContent = text || "";
  msg.className = "msg" + (type ? " " + type : "");
}

function normalizeUrl(raw) {
  let value = raw.trim();
  if (!value) return null;
  if (!/^[a-z][a-z0-9+.-]*:\/\//i.test(value)) value = "https://" + value;
  try {
    const u = new URL(value);
    if (u.protocol !== "https:" && u.protocol !== "http:") return null;
    if (!u.hostname.includes(".") && u.hostname !== "localhost") return null;
    return u.href;
  } catch (e) {
    return null;
  }
}

function makeIcon(link) {
  let host = "";
  try { host = new URL(link.url).hostname; } catch (e) {}
  const img = document.createElement("img");
  img.className = "ico";
  img.alt = "";
  img.src = "https://www.google.com/s2/favicons?domain=" + encodeURIComponent(host) + "&sz=64";
  img.addEventListener("error", () => {
    const fb = document.createElement("div");
    fb.className = "fallback";
    fb.textContent = (link.name[0] || "?").toUpperCase();
    img.replaceWith(fb);
  });
  return img;
}

function render() {
  grid.textContent = "";
  grid.classList.toggle("editing", editing);

  if (!links.length) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "No buttons yet. Press Edit to add your first link.";
    grid.appendChild(empty);
    return;
  }

  links.forEach((link) => {
    const a = document.createElement("a");
    a.className = "tile";
    a.href = link.url;
    a.title = link.url;

    a.appendChild(makeIcon(link));

    const name = document.createElement("span");
    name.className = "name";
    name.textContent = link.name;
    a.appendChild(name);

    const del = document.createElement("button");
    del.className = "del";
    del.type = "button";
    del.title = "Remove " + link.name;
    del.setAttribute("aria-label", "Remove " + link.name);
    del.textContent = "\u00d7";
    del.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      links = links.filter((l) => l.id !== link.id);
      save();
      render();
    });
    a.appendChild(del);

    a.addEventListener("click", (e) => {
      e.preventDefault();
      if (editing) return;
      chrome.tabs.create({ url: link.url });
      window.close();
    });

    grid.appendChild(a);
  });
}

function toggleEdit() {
  editing = !editing;
  editBtn.textContent = editing ? "Done" : "Edit";
  editBtn.setAttribute("aria-pressed", String(editing));
  editPanel.hidden = !editing;
  setMsg("");
  render();
}

async function addLink() {
  const name = $("nameInput").value.trim();
  const url = normalizeUrl($("urlInput").value);

  if (!name) return setMsg("Enter a name for the button.", "err");
  if (!url) return setMsg("Enter a valid link, like suno.com.", "err");
  if (links.some((l) => l.url === url)) return setMsg("That link is already on your list.", "err");

  links.push({ id: crypto.randomUUID(), name, url });
  await save();
  $("nameInput").value = "";
  $("urlInput").value = "";
  setMsg(name + " added.", "ok");
  render();
}

async function resetDefaults() {
  links = withIds(DEFAULTS);
  await save();
  setMsg("Defaults restored.", "ok");
  render();
}

editBtn.addEventListener("click", toggleEdit);
$("addBtn").addEventListener("click", addLink);
$("resetBtn").addEventListener("click", resetDefaults);
$("urlInput").addEventListener("keydown", (e) => { if (e.key === "Enter") addLink(); });
$("nameInput").addEventListener("keydown", (e) => { if (e.key === "Enter") $("urlInput").focus(); });

$("starBtn").addEventListener("click", (e) => {
  e.preventDefault();
  chrome.tabs.create({ url: "https://github.com/MUdevelops/AIBuddy" });
});

load();
