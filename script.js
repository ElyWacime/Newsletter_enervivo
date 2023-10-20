let container = document.getElementById("article");


const response = fetch("https://api.enervivo.fr/get")
    .then(res => res.json())
    .then(data => {
        data.map(obj => {
            console.log(obj)
            const arrOfObj = Object.entries(obj);
            arrOfObj.map(([key, value]) => {
                console.log(key)
                const valueArr = Object.entries(value);
                valueArr.map(([key, value]) => {
                    const h2 = document.createElement('h2');
                    h2.innerHTML = `<h2>${key}</h2>`;
                    container.append(h2);
                    const valueArr2 = Object.entries(value);
                    valueArr2.map(([key, value]) => {
                        container.append(display(value))
                    })
                })
            })
        })
        }
    )

console.log(response)

function display({title, image, description}){
    let article = document.createElement('div');
    article.innerHTML = `
    <div class="img"><img src="${image}"></div>
    <div class="title">${title}</div>
    <div class="date_link"></div>
    <div class="description">${description}</div>
    <div class="read_more"><a href="">Lire la suite</a></div>`;

    return article;
}