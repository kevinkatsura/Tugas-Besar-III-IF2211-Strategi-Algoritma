$(document).ready(function() {
        console.log("Checkpoint1");

    $("form").on('submit',function(event) {
        $.ajax({
            data: {
                message: $('#masukan').val()
            },
            type : 'POST',
            url : '/proccess'
        })
        .done(function(data){
            var new_entry = document.createElement("div");
            new_entry.id = "pesan";
            if(data.error){
                new_entry.innerHTML = data.error;
            } else {
                new_entry.innerHTML = data.message;
            }
            if (document.getElementById("middle") == null){
                console.log("Null")
            } else{
                console.log("ga null")
            }
            document.getElementById("middle").appendChild(new_entry);
            document.getElementById("masukan").value = "";
        });
        event.preventDefault();
        console.log("Checkpoint2");
    });

    window.setInterval(function() {
          var scroll_box = document.getElementById('middle');
          scroll_box.scrollTop = scroll_box.scrollHeight;
        }, 1);

});

