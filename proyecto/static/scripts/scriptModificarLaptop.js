$(document).ready(function() {
    console.log("punto de prueba para saber si esta funcionando la script");
    var registroForm = $('#formularioRegistro');
    var botonGuardar = $('#btnGuardar');
  
    botonGuardar.prop('disabled', true);
  
    registroForm.on('change', function() {
      botonGuardar.prop('disabled', false);
    });

    registroForm.on('reset', function() {
        botonGuardar.prop('disabled', true);
      });
  });

  function borrarMensajesError(){
    var invalidFields = document.querySelectorAll(".is-invalid");
        invalidFields.forEach(function(field) {
          field.classList.remove("is-invalid");
    });
      var myButton = document.getElementById("btnGuardar");
      myButton.click(); 
      
  }

  