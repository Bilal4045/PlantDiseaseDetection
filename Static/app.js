const fileInput = document.querySelector("#file-input");
const dropzone = document.querySelector("#dropzone");
const preview = document.querySelector("#image-preview");
const dropContent = document.querySelector("#dropzone-content");
const replaceHint = document.querySelector("#replace-hint");
const analyzeButton = document.querySelector("#analyze-button");
const form = document.querySelector("#upload-form");
const message = document.querySelector("#message");
const result = document.querySelector("#result");

let selectedFile = null;

function showMessage(text, loading = false) {
  message.textContent = text;
  message.classList.toggle("is-loading", loading);
}

function selectFile(file) {
  if (!file) return;
  if (!/image\/(jpeg|png)/.test(file.type)) {
    showMessage("Choose a JPG or PNG image.");
    return;
  }
  if (file.size > 10 * 1024 * 1024) {
    showMessage("That image is larger than 10 MB. Choose a smaller file.");
    return;
  }

  selectedFile = file;
  preview.src = URL.createObjectURL(file);
  preview.hidden = false;
  dropContent.hidden = true;
  replaceHint.hidden = false;
  analyzeButton.disabled = false;
  result.hidden = true;
  showMessage("");
}

dropzone.addEventListener("click", () => fileInput.click());
fileInput.addEventListener("change", () => selectFile(fileInput.files[0]));

for (const eventName of ["dragenter", "dragover"]) {
  dropzone.addEventListener(eventName, (event) => {
    event.preventDefault();
    dropzone.classList.add("is-over");
  });
}

for (const eventName of ["dragleave", "drop"]) {
  dropzone.addEventListener(eventName, (event) => {
    event.preventDefault();
    dropzone.classList.remove("is-over");
  });
}

dropzone.addEventListener("drop", (event) => selectFile(event.dataTransfer.files[0]));

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!selectedFile) return;

  analyzeButton.disabled = true;
  showMessage("Examining leaf image...", true);
  result.hidden = true;

  const formData = new FormData();
  formData.append("file", selectedFile);

  try {
    const response = await fetch("/api/predict", { method: "POST", body: formData });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Analysis failed. Try another image.");

    const [plant, ...condition] = data.class_name.split("___");
    const confidence = Math.max(0, Math.min(100, Number(data.confidence)));
    document.querySelector("#condition-name").textContent = condition.join(" ").replaceAll("_", " ") || "Unknown condition";
    document.querySelector("#plant-name").textContent = plant.replaceAll("_", " ").replaceAll(",", ", ");
    document.querySelector("#confidence-value").textContent = `${confidence.toFixed(2)}%`;
    document.querySelector("#confidence-bar").style.width = `${confidence}%`;
    result.hidden = false;
    showMessage("");
  } catch (error) {
    showMessage(error.message || "Could not reach the analysis service. Check that the server is running.");
  } finally {
    analyzeButton.disabled = false;
  }
});