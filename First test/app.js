$('#clickMe').click(function () {
    $.ajax({
        url: 'http://localhost:8888/characters.json',
        dataType: 'json',
        success: function (data) {
            var content = data;
            var i = 0;
            data.forEach(element => {
                content = data[i];
                $('#tableau').append('<tr>\
                <td>' + content["character"] + '</td>\
                </tr>');
                i++;
            });
        },
        error: {
            404: function () {
                alert('Erreur !');
            }
        }
    });
})