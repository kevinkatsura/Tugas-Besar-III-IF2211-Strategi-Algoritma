$(document).ready(function() {
    $("form").on('submit',function(event) {
        $.ajax({
            data: {
                message: $('#masukan').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data){
            // Menampilkan pesan yang baru saja dikirim oleh user
            var new_entry = document.createElement("div");
            new_entry.id = "pesan";
            new_entry.innerHTML = data.message;
            document.getElementById("middle").appendChild(new_entry);
            document.getElementById("masukan").value = "";
        }).done(function(data){
            // Pesan dari BOT
            var new_bot_message = document.createElement("div");
            new_bot_message.id = "BOT";
            if(data.error){
                new_bot_message.innerHTML = data.error;
            } else{
                new_bot_message.innerHTML = data.BOT
            }
            document.getElementById("middle").appendChild(new_bot_message);
        });
        event.preventDefault();
    });

    window.setInterval(function() {
          var scroll_box = document.getElementById('middle');
          scroll_box.scrollTop = scroll_box.scrollHeight;
        }, 1);
});



