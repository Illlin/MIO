// Define The Socket Object
var ws = new WebSocket("ws://127.0.0.1:5678/"),
name = window.prompt("enter name","");
// Send the name to the server through the socket
ws.send(name)
// Event holds the page until  message is received
ws.onmessage = function (event) {
alert(event.data)
};