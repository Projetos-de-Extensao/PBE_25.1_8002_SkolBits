const API_URL = "http://localhost:8000/api/moradores/"; // ajuste conforme sua API

async function carregarMoradores() {
    try {
        const resp = await fetch(API_URL);
        if (!resp.ok) throw new Error("Erro ao buscar moradores");
        const moradores = await resp.json();
        const tbody = document.querySelector("#moradoresTable tbody");
        tbody.innerHTML = "";
        moradores.forEach(m => {
            tbody.innerHTML += `
                <tr>
                    <td>${m.nome_morador}</td>
                    <td>${m.sobrenome_morador}</td>
                    <td>${m.sexo === "M" ? "Masculino" : "Feminino"}</td>
                    <td>${relacaoDescricao(m.relacao_com_responsavel)}</td>
                    <td>${m.quantidade_moradores31_07_2025}</td>
                    <td>${m.quantidade_criancas_0a9_31_07_2025}</td>
                </tr>
            `;
        });
    } catch (error) {
        alert("Erro ao carregar moradores: " + error.message);
    }
}

function relacaoDescricao(codigo) {
    const opcoes = {
        "001": "Pessoa responsável pelo domicílio",
        "002": "Conjuge ou companheiro(a) de sexo diferente",
        "003": "Conjuge ou companheiro(a) de mesmo sexo",
        "004": "Filho(a) do responsável e conjugue",
        "005": "Filho(a) somente do responsável",
        "006": "Enteado(a)",
        "007": "Genro ou nora",
        "008": "Pai, Mãe, Padrasto ou Madrasta",
        "009": "Sogro(a)",
        "010": "Neto(a)",
        "011": "Bisneto(a)",
        "012": "Irmão ou irmã",
        "013": "Avô ou avó",
        "014": "Outro parente",
        "015": "Agregado(a)",
        "016": "Convivente",
        "017": "Pensionista",
        "018": "Empregado(a) doméstico(a)",
        "019": "Parente do(a) empregado(a) doméstico(a)",
        "020": "Indiviual em domicílio coletivo"
    };
    return opcoes[codigo] || codigo;
}

document.getElementById("moradorForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = Object.fromEntries(new FormData(form).entries());
    data.quantidade_moradores31_07_2025 = String(data.quantidade_moradores31_07_2025);
    data.quantidade_criancas_0a9_31_07_2025 = String(data.quantidade_criancas_0a9_31_07_2025);

    try {
        const resp = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
        if (!resp.ok) {
            const erro = await resp.json();
            alert("Erro ao adicionar morador: " + JSON.stringify(erro));
            return;
        }
        form.reset();
        carregarMoradores();
    } catch (error) {
        alert("Erro ao adicionar morador: " + error.message);
    }
});

carregarMoradores();