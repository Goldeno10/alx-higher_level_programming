const url = "https://fourtonfish.com/hellosalut/?lang=fr";
$.get(url, (data, txStatus) => {
    $("DIV#hello").text(data.hello);
});