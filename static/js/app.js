$(function() {
    $('#submit').click(function() {
        event.preventDefault();
        var form_data = new FormData($('#uploadform')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function(data, textStatus, jqXHR){
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
            console.log('Success!');
            $(".upload").hide();
            $(".tableResult").show();
            $("#back").css('display', 'initial');

            $("#resultFileName").text(data['name']);
            $("#resultFileSize").text(data['size']);
            $("#resultFileChannel").text(data['channel']);
            $("#resultFileSample").text(data['sample']);
            $("#resultFileByte").text(data['byte']);
            $("#resultFileCodec").text(data['codec']);

            $(".music").attr("src",(data['path']));


        }).fail(function(data){
            alert('coś coś sie popsuło');
        });
    });
});

$('#back').click(function() {
    location.reload();
});