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

  /*codigo para visualizar los detalles de la celda ocupada*/
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

  /*codigo para crear parqueo*/
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cell.libre").forEach(cell => {
      cell.addEventListener("click", () => {
        const celdaId = cell.dataset.id;
  
        fetch(`/parqueos/formulario/${celdaId}/`)
          .then(res => res.text())
          .then(html => {
            document.getElementById("formularioParqueoBody").innerHTML = html;
            const modal = new bootstrap.Modal(document.getElementById("crearParqueoModal"));
            modal.show();
  
            document.getElementById("crearParqueoForm").addEventListener("submit", function (e) {
              e.preventDefault();
              const formData = new FormData(this);
  
              fetch(`/parqueos/crear/${celdaId}/`, {
                method: "POST",
                body: formData,
                headers: {
                  'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
              })
                .then(res => res.json())
                .then(data => {
                  if (data.success) {
                    modal.hide();
                    location.reload();
                  } else {
                    alert("Errores en el formulario");
                    console.log(data.errors);
                  }
                });
            });
          });
      });
    });
  });