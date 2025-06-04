fetch("https://script.google.com/macros/s/YOUR-SCRIPT-ID/exec", { 
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        name: "John Doe",
        email: "john@example.com"
    })  // ✅ Closes JSON.stringify()
})  // ✅ Closes fetch options object
.then(response => response.json())
.then(data => console.log("✅ API response:", data))
.catch(error => console.error("❌ API error:", error));