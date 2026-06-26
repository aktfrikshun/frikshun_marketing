/*
  Static-site note:
  This form needs a real endpoint to receive submissions/files.

  Recommended options:
  1. Formspree
  2. Netlify Forms
  3. Basin
  4. A small FrikShun backend endpoint
  5. GitHub Issues via a serverless function

  Set ARTIFACT_FORM_ENDPOINT below.
*/

const ARTIFACT_FORM_ENDPOINT = ""; // Example: "https://formspree.io/f/your-form-id"

const form = document.getElementById("artifactForm");
const statusEl = document.getElementById("formStatus");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!ARTIFACT_FORM_ENDPOINT) {
    statusEl.textContent =
      "Artifact staged locally. Connect ARTIFACT_FORM_ENDPOINT in js/artifact-upload.js to receive submissions.";
    return;
  }

  const formData = new FormData(form);

  try {
    statusEl.textContent = "Transmitting artifact...";
    const response = await fetch(ARTIFACT_FORM_ENDPOINT, {
      method: "POST",
      body: formData,
      headers: { Accept: "application/json" }
    });

    if (!response.ok) throw new Error("Submission failed");

    form.reset();
    statusEl.textContent = "Artifact received. Chloe will review the echo.";
  } catch (error) {
    statusEl.textContent = "Transmission failed. Try again or contact the archive custodian.";
  }
});
