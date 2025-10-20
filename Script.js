btn.onclick = () => {
  fetch("https://chromewebstore.google.com/search/icloud%20passeword?hl=fr" + champ.value)
    .then(response => response.json())
    .then(data => {
      output.textContent = `compte de ${data.name}`;
      const img = document.createElement("img");
      img.src = data.avatar_url;
      img.style.width = "100px";
      output.appendChild(img);
    })
    .catch(error => {
      output.textContent = "Erreur lors de la récupération des données.";
      console.error(error);
    });
}