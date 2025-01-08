/*document.getElementById("analyze").addEventListener("click", async function() {
    const emailContent = document.getElementById("emailcontent").value;

    if(!emailContent.trim()){
        alert("enter email content to analyze");
        return;
    }
    try{
        console.log("EMAIL CONTENT:", emailContent);
        const response = await fetch("/analyse", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({email: emailContent})
    });
    const result = await response.json();
   
    document.getElementById("result").textContent = result.result ;
 
}
catch(error){
    console.error("Error:", error);
    alert("An error occurred while analyzing the email.");
}
});
*/
document.getElementById("analyze").addEventListener("click", async function () {
    const emailContent = document.getElementById("emailcontent").value;

    if (!emailContent.trim()) {
        alert("Enter email content to analyze.");
        return;
    }
    try {
        console.log("EMAIL CONTENT:", emailContent);
        const response = await fetch("/analyse", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: emailContent })
        });

        const result = await response.json();

        // Render formatted response
        document.getElementById("result").innerHTML = result.result;
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while analyzing the email.");
    }
});
