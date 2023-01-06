function sendReview() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let content = document.getElementById("content").value;

    let webhookUrl = "https://discord.com/api/webhooks/1060726075681951834/jFfC6mrMROk4MKreMH68TGAHA-qqO57aF4MNR9961YOQpNCeyDLYBCOSUjkSf1my80fH";

    var request = new XMLHttpRequest();
    request.open("POST", webhookUrl.toString());
    request.setRequestHeader('Content-type', 'application/json');

    var myEmbed = {
        title: "New Review!",
        color: hexToDecimal("#ffffff"),
        fields: [
            {
                name: "Name",
                value: name
            },
            {
                name: "Email",
                value: email
            },
            {
                name: "Review",
                value: content
            }
        ]
    }

    var params = {
        username: "Review Hook",
        embeds: [ myEmbed ]
    }

    request.send(JSON.stringify(params));

}

function hexToDecimal(hex) {
    return parseInt(hex.replace("#",""), 16)
  }