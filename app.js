$('#clickMe').click(function (){

    $.ajax({
        url: 'http://localhost:8888/project.json',
        dataType: 'json',
        success: function (data) {
            var content = data;
            var i = 0;
            data.forEach(element => {
                content = data[i];
                $('#tableau').append('<tr>\
                <td><img src="' + content["Image du projet"] + '"></td>\
                <td>' + content["Nom de projet"] + '</td>\
                <td>' + content["Montant recherche"] + '</td>\
                <td>' + content["Nombre de commentaires"] + '</td>\
                <td>' + content["Nombre d'interesses"] + '</td>\
                <td>' + content["Statut de la collecte"] + '</td>\
                </tr>');
                console.log(content["Nom de projet"]);
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