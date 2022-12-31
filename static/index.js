var btn = document.querySelector('.searchButton')
btn.addEventListener('click', func)

function func() {
    console.log(document.querySelector(".searchTerm").value)
}