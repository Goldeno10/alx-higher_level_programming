window.onload = () => {
    $('INPUT#btn_translate').click(() => {
      const lan = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, (data, textStatus) => {
        $('DIV#hello').text(data.hello);
      });
    });
  };