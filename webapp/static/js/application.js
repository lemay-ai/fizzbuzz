
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    // var socket = io.connect('http://' + 'localhost' + ':' + '5000' + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 1){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<h1>' + numbers_received[i].toString() + '</h1>';
        }
        $('#log').html(numbers_string);
    });

    socket.on('newnumber2', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 1){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<h1>' + numbers_received[i].toString() + '</h1>';
        }
        $('#log1').html(numbers_string);
    });

});