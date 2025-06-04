function doPost(e) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
 
// ✅ CORS headers allow cross-origin requests, enabling API access from different domains
.setHeader("Access-Control-Allow-Origin", "*")
.setHeader("Access-Control-Allow-Methods", "POST")
.setHeader("Access-Control-Allow-Headers", "Content-Type");return ContentService.createTextOutput("Hello World")
    .setMimeType(ContentService.MimeType.JSON)
    .setHeader("Access-Control-Allow-Origin", "*");
}
    // ✅ Ensure request contains valid data
    if (!e || !e.postData || !e.postData.contents) {
        return ContentService.createTextOutput(
            JSON.stringify({ status: "Error", message: "No data received" })
        ).setMimeType(ContentService.MimeType.JSON)
        .setHeader("Access-Control-Allow-Origin", "*") // ✅ Fix CORS issue
        .setHeader("Access-Control-Allow-Methods", "POST")
        .setHeader("Access-Control-Allow-Headers", "Content-Type");
    }

    var data = JSON.parse(e.postData.contents);
    sheet.appendRow([data.name, data.email, new Date()]);

    // ✅ Send response back to client
    return ContentService.createTextOutput(
        JSON.stringify({ status: "Success!", message: "Data saved to spreadsheet." })
    ).setMimeType(ContentService.MimeType.JSON)
    .setHeader("Access-Control-Allow-Origin", "*") // ✅ Allows requests from anywhere
    .setHeader("Access-Control-Allow-Methods", "POST")
    .setHeader("Access-Control-Allow-Headers", "Content-Type");
}