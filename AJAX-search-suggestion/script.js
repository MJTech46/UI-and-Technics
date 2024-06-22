const InputElement = document.getElementById("searchInput");

InputElement.addEventListener("input", function (event){
    const data = InputElement.value;
    console.log(data);
    const xhr = new XMLHttpRequest();

    xhr.addEventListener('readystatechange', function () {
        if (xhr.readyState === xhr.DONE) {
            console.log(xhr.responseText);
        }
    });

    xhr.open('GET', 'https://suggestqueries.google.com/complete/search?client=youtube&q='+data);

    xhr.send(data);
});
