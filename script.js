// Espaço reservado para interações futuras (ex.: analytics de clique no CTA).
document.addEventListener("DOMContentLoaded", () => {
  const cta = document.querySelector(".cta-button");
  if (cta) {
    cta.addEventListener("click", () => {
      console.log("CTA 'Ver meu site' clicado");
    });
  }
});
