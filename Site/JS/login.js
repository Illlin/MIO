function validatePassword(form) {
    // Connect to server:
    var ws = new WebSocket("ws://127.0.0.1:5678/");
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var login_packet = {
        0:{
            "ID":04, //ID for login
            "DATA":{
                "email":email,
                "password":password
            }
        }
    };
    /*
    var handshake_packet = {
        0:{
            "ID":00, //ID for shortcut
            "DATA":""
        }
    }
    */ // Don't hand shake yet. Just send password to test login
    ws.send(login_packet)

}