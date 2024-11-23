// Función para registrar un usuario
document.getElementById("registroForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await axios.post("http://localhost:8000/register/", { username, password });
        alert("Usuario registrado exitosamente!");
    } catch (error) {
        console.error(error);
        alert("Error al registrar el usuario");
    }
});

// Función para hacer login
document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    try {
        const response = await axios.post("http://localhost:8000/login/", { username, password });
        const token = response.data.access_token;
        localStorage.setItem("access_token", token);  // Guardar el token en el localStorage
        alert("Login exitoso");
        loadProducts();  // Cargar productos si el login es exitoso
    } catch (error) {
        alert("Error al iniciar sesión");
    }
});

// Función para cargar los productos
const loadProducts = async () => {
    try {
        const response = await axios.get("http://localhost:8000/products/");
        const products = response.data;

        const productList = document.getElementById("productList");
        productList.innerHTML = "";  // Limpiar la lista

        products.forEach(product => {
            const productCard = document.createElement("div");
            productCard.classList.add("product-card");

            const productImage = document.createElement("img");
            productImage.src = `images/${product.image}`;  // Ruta de la imagen
            productCard.appendChild(productImage);

            const productName = document.createElement("h3");
            productName.innerText = product.name;
            productCard.appendChild(productName);

            const productPrice = document.createElement("p");
            productPrice.innerText = `$${product.price}`;
            productCard.appendChild(productPrice);

            productList.appendChild(productCard);
        });
    } catch (error) {
        console.error("Error al cargar los productos", error);
    }
};

// Cargar productos al iniciar
loadProducts();
