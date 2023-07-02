const imagenPrincipal = document.querySelector('#imagen-principal');
const imagenesSecundarias = document.querySelectorAll('.imagen-secundaria');

imagenesSecundarias.forEach(imagen => {
  imagen.addEventListener('click', () => {
    const imagenSeleccionada = imagen.src;
    imagen.src = imagenPrincipal.src;
    imagenPrincipal.src = imagenSeleccionada;
  });
});




// Obtener el botón y la ventana modal por sus identificadores
const abrirModalBtn = document.getElementById('abrirModal');
const cerrarModalBtn = document.getElementById('cerrarModal');
const miModal = document.getElementById('miModal');

// Definir una función para mostrar la ventana modal
function mostrarModal() {
  miModal.style.display = 'block';
}

// Definir una función para ocultar la ventana modal
function ocultarModal() {
  miModal.style.display = 'none';
}

// Asignar los eventos de clic a los botones correspondientes
abrirModalBtn.addEventListener('click', mostrarModal);
cerrarModalBtn.addEventListener('click', ocultarModal);

function borrarDatos() {
  console.log("estes es le candealsdlas")
  document.getElementById("cerrarModal").addEventListener("click", function() {
    document.getElementById("formularioRegistro").reset();
    var invalidFields = document.querySelectorAll(".is-invalid");
  invalidFields.forEach(function(field) {
    field.classList.remove("is-invalid");
  });
  });
}