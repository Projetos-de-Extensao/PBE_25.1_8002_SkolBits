const API_URL = "http://localhost:8000/api/moradores/"; // ajuste conforme sua API

async function carregarMoradores() {
    const resp = await fetch(API_URL);
    const moradores = await resp.json();
    const tbody = document.querySelector("#moradoresTable tbody");
    tbody.innerHTML = "";
    moradores.forEach(m => {
        tbody.innerHTML += `
            <tr>
                <td>${m.nome_morador}</td>
                <td>${m.sobrenome_morador}</td>
                <td>${m.sexo === "M" ? "Masculino" : "Feminino"}</td>
                <td>${m.relacao_com_responsavel}</td>
                <td>${m.quantidade_moradores31_07_2025}</td>
                <td>${m.quantidade_criancas_0a9_31_07_2025}</td>
            </tr>
        `;
    });
}

document.getElementById("moradorForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = Object.fromEntries(new FormData(form).entries());
    data.quantidade_moradores31_07_2025 = String(data.quantidade_moradores31_07_2025);
    data.quantidade_criancas_0a9_31_07_2025 = String(data.quantidade_criancas_0a9_31_07_2025);

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    form.reset();
    carregarMoradores();
});

carregarMoradores();