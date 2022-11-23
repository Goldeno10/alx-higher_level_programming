const url = "https://swapi-api.hbtn.io/api/films/?format=json";
$.get(url, (data, txStatus) => {
    let res = data.results;
    $.each(res, (i, res) => {
        $("UL#list_movies").append("<li>" + res.title + "</li>");
    });
});