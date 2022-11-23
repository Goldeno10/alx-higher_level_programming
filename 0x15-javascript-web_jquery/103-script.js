window.onload = () => {
    $('INPUT#btn_translate').click(() => {
      sayHello();
    });
    $('INPUT#language_code').keypress((event) => {
      if (event.keyCode === 13) {
        sayHello();
      }
    });
  };
  
  const sayHello =  () => {
    const lan = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  }