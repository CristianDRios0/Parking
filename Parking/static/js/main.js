/*document.addEventListener("DOMContentLoaded", function () {
    const btnAbrirModal = document.getElementById("btnAbrirModalCelda");  // El botón debe tener este ID
    const modalBody = document.getElementById("modal-body-content");

    btnAbrirModal.addEventListener("click", function () {
      fetch("/celdas/crear/")
        .then(response => {
          if (!response.ok) {
            throw new Error("Error al cargar el formulario");
          }
          return response.text();
        })
        .then(html => {
          console.log("Formulario recibido:");
          console.log(html);
          modalBody.innerHTML = html;

          const modal = new bootstrap.Modal(document.getElementById("modalCrearCelda"));
          modal.show();
        })
        .catch(error => {
          console.error("Error:", error);
          modalBody.innerHTML = "<p class='text-danger'>No se pudo cargar el formulario.</p>";
        });
    });
  });*/

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cell.ocupado").forEach(cell => {
      cell.addEventListener("click", () => {
        const celdaId = cell.dataset.id;
  
        fetch(`/celdas/detalle/${celdaId}/`)
          .then(response => response.text())
          .then(html => {
            document.getElementById("detalleCeldaContent").innerHTML = html;
            const modal = new bootstrap.Modal(document.getElementById("infoCeldaModal"));
            modal.show();
          })
          .catch(error => console.error("Error cargando la info de la celda:", error));
      });
    });
  });
