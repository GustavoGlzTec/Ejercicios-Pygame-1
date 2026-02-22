const residencias = [
  {
    nombre: "Casa Mirador del Lago",
    tipo: "Residencia · 2 habitaciones",
    ciudad: "Guatapé, Colombia",
    precio: "$210.000 / noche",
    imagen:
      "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&w=1200&q=80",
  },
  {
    nombre: "Villa Brisa Serena",
    tipo: "Residencia · 4 habitaciones",
    ciudad: "Santa Marta, Colombia",
    precio: "$420.000 / noche",
    imagen:
      "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
  },
];

const container = document.getElementById("cards-container");

residencias.forEach((item) => {
  const card = document.createElement("article");
  card.className = "card";

  card.innerHTML = `
    <img class="card__image" src="${item.imagen}" alt="${item.nombre}" />
    <div class="card__content">
      <h3 class="card__title">${item.nombre}</h3>
      <p class="card__meta">${item.tipo}</p>
      <p class="card__meta">${item.ciudad}</p>
      <p class="card__price">${item.precio}</p>
      <button class="card__button" type="button">Reservar</button>
    </div>
  `;

  container.appendChild(card);
});
